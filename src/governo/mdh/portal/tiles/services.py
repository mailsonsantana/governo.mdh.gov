# -*- coding: utf-8 -*-
from collective.cover import _
from collective.cover.interfaces import ITileEditForm
from collective.cover.tiles.list import IListTile
from collective.cover.tiles.list import ListTile
from collective.cover.widgets.textlinessortable import TextLinesSortableFieldWidget
from plone.autoform import directives as form
from zope.interface import implementer


class IServicesTile(IListTile):
    """Displays a search box and a list of service highlights."""

    form.no_omit(ITileEditForm, 'uuids')
    form.widget(uuids=TextLinesSortableFieldWidget)


@implementer(IServicesTile)
class ServicesTile(ListTile):
    """Displays a search box and a list of service highlights."""

    is_configurable = False
    is_droppable = True
    is_editable = True
    short_name = _(u'msg_short_name_services', default=u'Services')
