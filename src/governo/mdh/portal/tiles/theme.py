# -*- coding: utf-8 -*-
from Acquisition import aq_base
from collective.cover.browser.scaling import ImageScale
from collective.cover.tiles.base import IPersistentCoverTile
from collective.cover.tiles.base import PersistentCoverTile
from governo.mdh.portal import _
from plone.namedfile import field
from plone.namedfile import NamedBlobImage
from plone.tiles.interfaces import ITileDataManager
from plone.app.imaging.utils import getAllowedSizes
from zope.interface import implementer
from zope.schema import Choice, TextLine
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

colors = SimpleVocabulary([
    SimpleTerm(value="inverter-white", token=1, title=u'Cores Brancas'),
    SimpleTerm(value="default", token=2, title=u'Cores Pretas'),
])

class IThemeTile(IPersistentCoverTile):
    """Displays a list of featured mobile apps."""

    title = TextLine(
        title=_(u'Title'),
        required=True,
        default=u'',
    )

    image = field.NamedBlobImage(
        title=_(u'label_theme_top_image'),
        required=True,
    )

    color_top = Choice(
        title=_(u'label_color_top', default=u'Color Top'),
        vocabulary=colors,
        required=False,
        default='default',
    )
    

@implementer(IThemeTile)
class ThemeTile(PersistentCoverTile):
    """Displays a Theme section."""

    is_configurable = False
    is_droppable = True
    is_editable = True
    short_name = _(u'msg_short_name_theme', default=u'Theme')

    def accepted_ct(self):
        return ['Theme']

    def populate_with_object(self, obj):
        super(ThemeTile, self).populate_with_object(obj)
        obj = aq_base(obj)
        img = obj.theme_top_image.data
        color_top = obj.color_top
        title = obj.Title()
        if img:
            data = obj.theme_top_image.data
            image = NamedBlobImage(data)
        else:
            image = None

        data_mgr = ITileDataManager(self)
        data_mgr.set({
            'image': image,
            'color_top':color_top,
            'title':title,
        })

    @property
    def get_color_top(self):
        return self.data['color_top']
    
    @property
    def is_empty(self):
        return not self.has_image