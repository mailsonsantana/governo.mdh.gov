# -*- coding: utf-8 -*-
from governo.mdh.portal.config import PROJECTNAME
from plone import api
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer

from Products.CMFPlone.utils import _createObjectByType, getToolByName
from plone.i18n.normalizer import idnormalizer
from unicodedata import normalize

import transaction
import logging


logger = logging.getLogger(PROJECTNAME)


@implementer(INonInstallable)
class NonInstallable(object):

    def getNonInstallableProfiles(self):  # pragma: no cover
        """Do not show on Plone's list of installable profiles."""
        return [
            u'governo.mdh.portal:uninstall',
        ]


class Empty:
    pass


def add_catalog_indexes():
    """Method to add our wanted indexes to the portal_catalog.
    For more information see:
    http://maurits.vanrees.org/weblog/archive/2009/12/catalog
    """
    def extras(title, index_type='Okapi BM25 Rank', lexicon_id='plone_lexicon'):
        # See http://old.zope.org/Members/dedalu/ZCTextIndex_python
        extras = Empty()
        extras.doc_attr = title
        extras.index_type = index_type
        extras.lexicon_id = lexicon_id
        return extras

    profile = 'profile-{0}:default'.format(PROJECTNAME)
    setup = api.portal.get_tool('portal_setup')
    setup.runImportStepFromProfile(profile, 'catalog')

    catalog = api.portal.get_tool('portal_catalog')
    indexes = catalog.indexes()

    wanted = (
        ('document_type', 'FieldIndex'),
    )

    indexables = []
    for name, meta_type in wanted:
        if name not in indexes:
            if meta_type == 'ZCTextIndex':
                catalog.addIndex(name, meta_type, extras(name))
            else:
                catalog.addIndex(name, meta_type)
            indexables.append(name)
            logger.info('Added %s for field %s.', meta_type, name)

    if len(indexables) > 0:
        logger.info('Indexing new indexes %s.', ', '.join(indexables))
        catalog.manage_reindexIndex(ids=indexables)


def normalizerId(text):

    text_id = idnormalizer.normalize(
        normalize('NFKD',
                  text.decode('utf-8')).encode('ASCII', 'ignore').lower())
    return text_id


def add_content_central_menu():
    """Add new menu option to folders"""
    types_tool = api.portal.get_tool('portal_types')
    types_tool['Folder'].view_methods += ('centrais-de-conteudo',)


def add_content_portalmdh(context):
    """Add new menu for content PortalMDH"""

    site = getToolByName(context, "portal_url").getPortalObject()
    wtool = getToolByName(site, 'portal_workflow')
    existing = site.keys()

    menus = ['Navegue por temas',
             'Informação ao cidadão',
             ]
    conteudos_navegue = ['Criança e Adolescente',
                        'Igualdade Racial',
                        'Pessoa Idosa',
                        'Pessoa Com Deficiência',
                        'LGBT',
                        'Programas de Proteção'
                        'Educação em Direitos Humanos',
                        'Prevenção e Combate à Tortura',
                        'Combate ao Trabalho Escravo',
                        'Diversidade Religiosa',
                        'População em Situação de Rua',
                        'Registro Civil do Nascimento',
                        'Refugiados',
                        'Empresas e Direitos Humanos',
                        'Atuação Internacional',]

    conteudos_informacao = ['Ações e Programas',
                           'Auditorias',
                           'Biblioteca Virtual',
                           'Convênios e Transferências',
                           'Dados Abertos',
                           'Informações Qualificadas',
                           'Institucional',
                           'Licitações e Contratos',
                           'Participação Social',
                           'Receitas e Despesas',
                           'Serviço de Informação ao Cidadão - SIC',
                           'Servidores',]

    # Cria as pastas principais
    for menu in menus:
        menu_id = normalizerId(menu)
        if menu_id not in existing:
            title = menu
            _createObjectByType('Folder',
                               site,
                               id=menu_id,
                               title=title
                               )
            folder_navegue = site['navegue-por-temas']
            folder_navegue.reindexObject()
            if folder_navegue not in existing:
                for conteudo in conteudos_navegue:
                    title = menu
                    _createObjectByType('Folder',
                                       folder_navegue,
                                       id=menu_id,
                                       title=title
                                       )
                    transaction.commit()
 
            folder_informacao = site['navegue-por-temas']
            folder_informacao.reindexObject()
            folder_informacao = getattr(site, 'navegue-por-temas')


def update_menu():
    """Add new menu option to collection."""
    types_tool = api.portal.get_tool('portal_types')
    types_tool['Collection'].view_methods += ('filter-results',)


def post_install(context):
    """Post install script."""
    add_catalog_indexes()
    add_content_central_menu()
    #add_content_portalmdh(context)
    update_menu()


def post_uninstall(context):
    """Post uninstall script."""
