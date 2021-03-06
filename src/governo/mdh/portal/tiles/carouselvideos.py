# -*- coding: utf-8 -*-
from collective.cover import _
from collective.cover.interfaces import ITileEditForm
from collective.cover.tiles.list import IListTile
from collective.cover.tiles.list import ListTile
from collective.cover.utils import get_types_use_view_action_in_listings
from collective.cover.widgets.textlinessortable import TextLinesSortableFieldWidget
from plone.autoform import directives as form
from plone.tiles.interfaces import ITileDataManager
from zope import schema
from zope.interface import implementer


class ICarouselVideosTile(IListTile):
    """Display a carousel of items."""

    tile_description = schema.Text(title=_(u'Tile Description'), required=False)
    form.omitted('tile_description')
    form.no_omit(ITileEditForm, 'tile_description')

    switch_text = schema.TextLine(title=_(u'Switch Text'), required=False)
    form.omitted('switch_text')
    form.no_omit(ITileEditForm, 'switch_text')

    form.no_omit(ITileEditForm, 'uuids')
    form.widget(uuids=TextLinesSortableFieldWidget)


@implementer(ICarouselVideosTile)
class CarouselVideosTile(ListTile):
    """Display a carousel of videos."""

    is_configurable = True
    is_droppable = True
    is_editable = True
    short_name = _(u'msg_short_name_carousel_videos', default=u'Carousel Videos')

    def accepted_ct(self):
        return ['sc.embedder']

    @property
    def tile_description(self):
        return self.data['tile_description']

    @property
    def switch_text(self):
        return self.data['switch_text']

    def results(self):
        page = []

        for i, item in enumerate(super(CarouselVideosTile, self).results()):
            page.append(item)
            if (i + 1) % 3 == 0:
                yield page
                page = []
        if page:
            yield page

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

    def get_description(self, item):
        """Get the description of the item, or the custom description
        if set.

        :param item: [required] The item for which we want the description
        :type item: Content object
        :returns: the item description
        :rtype: unicode
        """
        # First we get the url for the item itself
        description = ''
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
        url = getattr(item, 'url', item.absolute_url())
        # uuid = self.get_uuid(item)
        # data_mgr = ITileDataManager(self)
        # data = data_mgr.get()
        # uuids = data['uuids']
        # if uuid in uuids:
        #     if uuids[uuid].get('custom_url', u''):
        #         # If we had a custom url set, then get that
        #         url = uuids[uuid].get('custom_url')
        return url

    def get_custom_url(self, item):
        """Get the URL of the item, or the custom URL if set.

        :param item: [required] The item for which we want the URL
        :type item: Content object
        :returns: the item URL
        :rtype: str
        """
        # First we get the url for the item itself
        #import pdb;pdb.set_trace()
        url = getattr(item, 'url', item.absolute_url())
        uuid = self.get_uuid(item)
        data_mgr = ITileDataManager(self)
        data = data_mgr.get()
        uuids = data['uuids']
        if uuid in uuids:
            if uuids[uuid].get('custom_url', u''):
                # If we had a custom url set, then get that
                url = uuids[uuid].get('custom_url')
        return url