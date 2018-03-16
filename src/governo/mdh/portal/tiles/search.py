# -*- coding: utf-8 -*-
from collective.cover import _
from collective.cover.tiles.base import IPersistentCoverTile
from collective.cover.tiles.base import PersistentCoverTile
from plone import api
from zope.interface import implementer
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.interfaces import IVocabularyFactory
from zope.interface import provider
from zope import schema


class ISearchTile(IPersistentCoverTile):
    """Displays a list tags in Search"""

    field_path = schema.TextLine(title=_(u'Informe o caminho da pasta'),
                                 required=False)


@implementer(ISearchTile)
class SearchTile(PersistentCoverTile):
    """Displays a list of tags."""

    is_configurable = True
    is_droppable = False
    is_editable = True
    short_name = _(u'msg_short_library', default=u'Search')

    @property
    def field_path(self):
        return self.data['field_path']

    def subjects_under_context(self, path, indexname=''):
        """valid subjects under the given context
        """

        pcat = api.portal.get_tool('portal_catalog')
        cat = pcat._catalog
        path_idx = cat.indexes['path']
        tags_idx = cat.indexes[indexname]
        portal = api.portal.getSite().id
        result = []
        # query all oids of path - low level
        pquery = {
            'path': {
                'query': '/'.join(portal+str(path)),
                'depth': -1,
            }
        }
        path_result, info = path_idx._apply_index(pquery)
        for tag in tags_idx.uniqueValues():
            tquery = {indexname: tag}
            tags_result, info = tags_idx._apply_index(tquery)
            D={}
            D['value'] = tag.lower()
            D['title'] = tag.capitalize()
            result.append(D)
        terms = [SimpleTerm(value=pair['value'], title=pair['title']) for pair in result]
        return SimpleVocabulary(terms)

    @provider(IVocabularyFactory)
    def subject_factory(self):
        return self.subjects_under_context(self.field_path,indexname='Subject')

    def get_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    catalog = property(get_catalog)

    @property
    def portal_catalog(self):
        return self.context.portal_catalog


    def get_dados(self):
        """ Obtem os dados que serão usados no template
        """
        brains = []
        request = self.request
        form = request.form
        results = {}
        query = {
            'portal_type': 'collective.nitf.content',
        }

        if form.get('submitted', False):
            indexes = self.portal_catalog.indexes()

            for field, value in form.items():
                if (field in indexes) and value:
                    if field == 'buscar':
                        query['SearchableText'] = value
                        query['Title'] = value
                        query['Description'] = value
                        continue
                    elif field == 'subject':
                        query['Subject'] = value

        brains = self.portal_catalog(query)
        results = {
            'list': [self._brain_for_dict(brain) for brain in brains if brain],
        }

        return results

    def _brain_for_dict(self, brain):
        """ Converte um obj em dicionario
        """
        try:
            object = brain.getObject()
        except:
            object = None

        if object:
            obj = brain.getObject()
            data_object = obj.__dict__

        return data_object
