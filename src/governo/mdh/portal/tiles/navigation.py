# -*- coding: utf-8 -*-
from Acquisition import aq_parent
from collective.cover import _
from collective.cover.tiles.base import IPersistentCoverTile
from collective.cover.tiles.base import PersistentCoverTile
from plone import api
from plone.dexterity.interfaces import IDexterityContent
from zope.interface import implementer
from zope import schema


class INavigationTile(IPersistentCoverTile):
    """Displays a list of featured mobile apps."""
    facebook_url = schema.TextLine(
        title=_(u'URL Facebook'),
        required=False,
        description=_(u'Insira a url da página do facebook'),
        default=u'http://',
    )

    twitter_url = schema.TextLine(
        title=_(u'URL Twitter'),
        required=False,
        description=_(u'Insira a url da página do Twitter'),
        default=u'http://',
    )

@implementer(INavigationTile)
class NavigationTile(PersistentCoverTile):
    """Displays a list of featured mobile apps."""

    is_configurable = False
    is_droppable = False
    is_editable = True
    short_name = _(u'msg_short_name_navigation', default=u'Navigation')

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

    def get_redes_sociais(self):
        facebook = self.data['facebook_url']
        twitter = self.data['twitter_url']
        return dict(facebook_url=facebook,
                    twitter_url=twitter)

    def more_items(self):
        return self.menu_items[3:]
