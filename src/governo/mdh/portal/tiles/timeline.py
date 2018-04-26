# -*- coding: utf-8 -*-
from Acquisition import aq_base
from collective.cover.browser.scaling import ImageScale
from collective.cover.interfaces import ITileEditForm
from collective.cover.tiles.list import IListTile
from collective.cover.tiles.list import ListTile
from collective.cover.utils import get_types_use_view_action_in_listings
from collective.cover.widgets.textlinessortable import TextLinesSortableFieldWidget
from governo.mdh.portal import _
from plone.autoform import directives as form
from plone.namedfile import field
from plone.namedfile import NamedBlobImage
from plone.tiles.interfaces import ITileDataManager
from zope.interface import implementer
from zope.schema import Text, TextLine


class ITimelineTile(IListTile):
    """Displays a timeline items."""

    form.no_omit(ITileEditForm, 'uuids')
    form.widget(uuids=TextLinesSortableFieldWidget)

@implementer(ITimelineTile)
class TimelineTile(ListTile):
    """Displays a Timeline section."""

    is_configurable = False
    is_droppable = True
    is_editable = True
    short_name = _(u'msg_short_name_timeline', default=u'Timeline')

    def accepted_ct(self):
        return ['Timeline']

    @property
    def tile_description(self):
        return self.data['description']

    def results(self):
        page = []

        for i, item in enumerate(super(TimelineTile, self).results()):
            page.append(item)
            if (i + 1) % 1 == 0:
                yield page
                page = []

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

    def get_more_link_text(self, item):
        more_link_text = item.more_information
        uuid = self.get_uuid(item)
        data_mgr = ITileDataManager(self)
        data = data_mgr.get()
        uuids = data['uuids']
        if uuid in uuids:
            if uuids[uuid].get('custom_more_link_text', u''):
                # If we had a custom more_link_text set, then get that
                more_link_text = uuids[uuid].get('custom_more_link_text')
        return more_link_text

    def get_year(self, item):
        year = item.year
        uuid = self.get_uuid(item)
        data_mgr = ITileDataManager(self)
        data = data_mgr.get()
        uuids = data['uuids']
        if uuid in uuids:
            if uuids[uuid].get('custom_year', u''):
                # If we had a custom year set, then get that
                year = uuids[uuid].get('custom_year')
        return year

    def get_month(self, item):
        month = item.month
        uuid = self.get_uuid(item)
        data_mgr = ITileDataManager(self)
        data = data_mgr.get()
        uuids = data['uuids']
        if uuid in uuids:
            if uuids[uuid].get('custom_month', u''):
                # If we had a custom month set, then get that
                month = uuids[uuid].get('custom_month')
        return month

    def get_image(self,item):
        if item:
            image = item.image_timeline
            scales = item.restrictedTraverse('@@images')
            scale = scales.scale('image_timeline', scale='timeline_view')
            return scale
            


    def get_between_years(self,itens):
        if itens:
            years = [year[0].year for year in itens]
            year_left = years[0]
            year_right = years[-1]
            D={}
            D['year_left'] = year_left
            D['year_right'] = year_right
        else:
            D={}
            D['year_left'] = ''
            D['year_right'] = ''
        return D