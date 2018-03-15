# -*- coding: utf-8 -*-
from collective.cover import _
from collective.cover.interfaces import ITileEditForm
from collective.cover.tiles.list import IListTile
from collective.cover.tiles.list import ListTile
from collective.cover.widgets.textlinessortable import TextLinesSortableFieldWidget
from plone.autoform import directives as form
from zope import schema
from zope.interface import implementer


class ICarouselTile(IListTile):
    """Display a carousel of items."""

    tile_description = schema.Text(title=_(u'Tile Description'), required=False)
    form.omitted('tile_description')
    form.no_omit(ITileEditForm, 'tile_description')

    switch_text = schema.TextLine(title=_(u'Switch Text'), required=False)
    form.omitted('switch_text')
    form.no_omit(ITileEditForm, 'switch_text')

    form.no_omit(ITileEditForm, 'uuids')
    form.widget(uuids=TextLinesSortableFieldWidget)


@implementer(ICarouselTile)
class CarouselTile(ListTile):
    """Display a carousel of items."""

    is_configurable = False
    is_droppable = True
    is_editable = True
    short_name = _(u'msg_short_name_tags', default=u'Carousel')
    limit = 4 * 3

    @property
    def tile_description(self):
        return self.data['tile_description']

    @property
    def switch_text(self):
        return self.data['switch_text']

    def results(self):
        page = []

        for i, item in enumerate(super(CarouselTile, self).results()):
            page.append(item)
            if (i + 1) % 4 == 0:
                yield page
                page = []
        if page:
            yield page
