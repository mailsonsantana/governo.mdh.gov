# -*- coding: utf-8 -*-
from governo.mdh.portal.config import PROJECTNAME
from plone import api
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer

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


def add_content_central_menu():
    """Add new menu option to folders"""
    types_tool = api.portal.get_tool('portal_types')
    types_tool['Folder'].view_methods += ('centrais-de-conteudo',)


def update_menu():
    """Add new menu option to collection."""
    types_tool = api.portal.get_tool('portal_types')
    types_tool['Collection'].view_methods += ('filter-results',)


def post_install(context):
    """Post install script."""
    add_catalog_indexes()
    add_content_central_menu()
    update_menu()


def post_uninstall(context):
    """Post uninstall script."""
