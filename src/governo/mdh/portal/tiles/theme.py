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
from zope.schema import Choice
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

colors = SimpleVocabulary([
    SimpleTerm(value="inverter-white", token=1, title=u'Cores Brancas'),
    SimpleTerm(value="default", token=2, title=u'Cores Pretas'),
])

class IThemeTile(IPersistentCoverTile):
    """Displays a list of featured mobile apps."""

    theme_top_image = field.NamedBlobImage(
        title=_(u'label_theme_top_image'),
        required=True,
    )

    color_top = Choice(
        title=_(u'label_color_top', default=u'Color Top'),
        vocabulary=colors,
        required=True,
        default='default',
    )
    

@implementer(IThemeTile)
class ThemeTile(PersistentCoverTile):
    """Displays a Theme section."""

    is_configurable = True
    is_droppable = True
    is_editable = True
    short_name = _(u'msg_short_name_apps', default=u'Theme')

    def accepted_ct(self):
        return ['Image']

    def populate_with_object(self, obj):
        super(ThemeTile, self).populate_with_object(obj)
        obj = aq_base(obj)
        img = obj.image.data

        if img:
            data = obj.image.data
            image = NamedBlobImage(data)
        else:
            image = None

        data_mgr = ITileDataManager(self)
        data_mgr.set({
            'image': image,
        })

    @property
    def get_color_top(self):
        return self.data['color_top']

    @property
    def get_theme_top_image(self):
        data = self.data['theme_top_image']
        data = '<img src="http://localhost:8080/mdh/temas/crianca-e-adolescente/@@images/4d751db7-d2a0-4cd3-bf77-d575493c26fc.png" alt="Criança e Adolescente" title="Criança e Adolescente" height="474" width="3840" />'
        return data
    
    @property
    def is_empty(self):
        return not self.has_image