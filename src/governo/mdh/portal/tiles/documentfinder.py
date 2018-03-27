# -*- coding: utf-8 -*-
from collective.cover.tiles.base import IPersistentCoverTile
from collective.cover.tiles.base import PersistentCoverTile
from governo.mdh.portal import _
from plone import api
from plone.tiles.interfaces import ITileDataManager
from zope import schema
from zope.component import getUtility
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory


class IDocumentFinderTile(IPersistentCoverTile):
    """A tile that allows filtering the results of a collection."""

    title = schema.TextLine(
        title=_(u'Title'),
        required=False,
    )

    uuid = schema.TextLine(
        title=u'UUID',
        required=False,
        readonly=True,
    )


@implementer(IDocumentFinderTile)
class DocumentFinderTile(PersistentCoverTile):
    """A tile that allows filtering the results of a collection."""

    is_configurable = False
    is_droppable = True
    is_editable = True
    short_name = _(
        u'msg_short_name_document_finder', default=u'Document Finder')

    def accepted_ct(self):
        return ('Collection',)

    def populate_with_object(self, obj):
        super(DocumentFinderTile, self).populate_with_object(obj)  # check permission

        if obj.portal_type not in self.accepted_ct():
            return

        data_mgr = ITileDataManager(self)
        data_mgr.set({
            'title': 'Documentos de Imprensa',
            'uuid': api.content.get_uuid(obj),
        })

    def results(self, limit):
        uuid = self.data.get('uuid', '')
        obj = api.content.get(UID=uuid)
        if obj is None:
            self._cleanup()  # remove reference
            return []

        results = obj.results(
            batch=False,
            brains=True,
            custom_query={'sort_order': 'reverse'},
            sort_on='Date',
        )
        return [brain for brain in results if brain.document_type][:limit]

    def is_empty(self):
        return self.data.get('uuid', None) is None

    def _cleanup(self):
        data_mgr = ITileDataManager(self)
        data_mgr.set({'uuid': None})

    def get_document_types(self):
        name = 'governo.mdh.portal.DocumentTypes'
        vocabulary = getUtility(IVocabularyFactory, name)
        return vocabulary(None)

    @property
    def more_link(self):
        uuid = self.data.get('uuid', '')
        obj = api.content.get(UID=uuid)
        if obj is None:
            self._cleanup()  # remove reference
            return ''
        return obj.absolute_url()
