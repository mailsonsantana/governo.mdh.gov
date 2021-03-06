# -*- coding: utf-8 -*-
from collective.cover import _
from collective.cover.interfaces import ITileEditForm
from collective.cover.tiles.list import IListTile
from collective.cover.tiles.list import ListTile
from collective.cover.utils import get_types_use_view_action_in_listings
from governo.mdh.portal.widgets.textlinessortable import TextLinesSortableFieldWidget
from plone.autoform import directives as form
from plone.tiles.interfaces import ITileDataManager
from zope import schema
from zope.interface import implementer


class IGalleryTile(IListTile):
    """Displays a list of tags."""

    tile_description = schema.Text(title=_(u'Tile Description'), required=False)
    form.omitted('tile_description')
    form.no_omit(ITileEditForm, 'tile_description')

    form.no_omit(ITileEditForm, 'uuids')
    form.widget(uuids=TextLinesSortableFieldWidget)


@implementer(IGalleryTile)
class GalleryTile(ListTile):
    """Displays a list of tags."""

    is_configurable = False
    is_droppable = True
    is_editable = True
    short_name = _(u'msg_short_name_gallery', default=u'Gallery')
    limit = 5 * 3

    @property
    def tile_description(self):
        return self.data['tile_description']

    def get_title(self, item):
        """Get the title of the item, or the custom title if set.

        :param item: [required] The item for which we want the title
        :type item: Content object
        :returns: the item title
        :rtype: unicode
        """
        # First we get the title for the item itself
        title = item.Title()
        uuid = self.get_uuid(item)
        data_mgr = ITileDataManager(self)
        data = data_mgr.get()
        uuids = data['uuids']
        if uuid in uuids:
            if uuids[uuid].get('custom_title', u''):
                # If we had a custom title set, then get that
                title = uuids[uuid].get('custom_title')
        return title

    def get_subtitle(self, item):
        """Get the subtitle of the item, or the custom subtitle if set.

        :param item: [required] The item for which we want the subtitle
        :type item: Content object
        :returns: the item subtitle
        :rtype: unicode
        """
        # First we get the subtitle for the item itself
        subtitle = getattr(item, 'subtitle', None)
        uuid = self.get_uuid(item)
        data_mgr = ITileDataManager(self)
        data = data_mgr.get()
        uuids = data['uuids']
        if uuid in uuids:
            if uuids[uuid].get('custom_subtitle', u''):
                # If we had a custom subtitle set, then get that
                subtitle = uuids[uuid].get('custom_subtitle')
        return subtitle

    def get_description(self, item):
        """Get the description of the item, or the custom description
        if set.

        :param item: [required] The item for which we want the description
        :type item: Content object
        :returns: the item description
        :rtype: unicode
        """
        # First we get the url for the item itself
        description = item.Description()
        uuid = self.get_uuid(item)
        data_mgr = ITileDataManager(self)
        data = data_mgr.get()
        uuids = data['uuids']
        if uuid in uuids:
            if uuids[uuid].get('custom_description', u''):
                # If we had a custom description set, then get that
                description = uuids[uuid].get('custom_description')
        return description

    def get_url(self, item):
        """Get the URL of the item, or the custom URL if set.

        :param item: [required] The item for which we want the URL
        :type item: Content object
        :returns: the item URL
        :rtype: str
        """
        # First we get the url for the item itself
        url = getattr(item, 'remoteUrl', item.absolute_url())
        if item.portal_type in get_types_use_view_action_in_listings():
            url += '/view'
        uuid = self.get_uuid(item)
        data_mgr = ITileDataManager(self)
        data = data_mgr.get()
        uuids = data['uuids']
        if uuid in uuids:
            if uuids[uuid].get('custom_url', u''):
                # If we had a custom url set, then get that
                url = uuids[uuid].get('custom_url')
        return url
