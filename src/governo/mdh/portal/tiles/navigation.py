# -*- coding: utf-8 -*-
from Acquisition import aq_parent
from collective.cover import _
from collective.cover.tiles.base import IPersistentCoverTile
from collective.cover.tiles.base import PersistentCoverTile
from plone import api
from plone.dexterity.interfaces import IDexterityContent
from zope.interface import implementer


class INavigationTile(IPersistentCoverTile):
    """Displays a list of featured mobile apps."""


@implementer(INavigationTile)
class NavigationTile(PersistentCoverTile):
    """Displays a list of featured mobile apps."""

    is_configurable = False
    is_droppable = False
    is_editable = False
    short_name = _(u'msg_short_name_apps', default=u'Navigation')

    def __init__(self, context, request):
        super(NavigationTile, self).__init__(context, request)
        self._setup()

    def _setup(self):
        self.menu_items = []
        self.session = aq_parent(self.context)
        for o in self.context.listFolderContents():
            if self._exclude_from_nav(o):
                continue
            if api.content.get_state(o, '') != 'published':
                continue
            self.menu_items.append(o)

    def _exclude_from_nav(self, obj):
        """Check DX and AT way if is a menu item."""
        if obj is None:
            return True
        if IDexterityContent.providedBy(obj):
            try:
                # Dexterity
                exclude_from_nav = obj.exclude_from_nav
                if callable(exclude_from_nav):
                    return True
                return exclude_from_nav
            except AttributeError:
                pass
        else:
            try:
                # Archetypes
                return obj.getExcludeFromNav()
            except AttributeError:
                pass
        return True  # For some content type that can't be a Menu

    def first_items(self):
        return self.menu_items[:3]

    def more_items(self):
        return self.menu_items[3:]
