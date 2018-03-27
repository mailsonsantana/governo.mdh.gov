# -*- coding: utf-8 -*-
from collective.cover.browser.scaling import ImageScale
from collective.cover.interfaces import ITileEditForm
from collective.cover.tiles.base import IPersistentCoverTile
from collective.cover.tiles.base import PersistentCoverTile
from governo.mdh.portal import _
from plone import api
from plone.app.imaging.utils import getAllowedSizes
from plone.app.textfield import RichText
from plone.autoform import directives as form
from plone.namedfile import field
from urlparse import urlparse
from zope import schema
from zope.interface import implementer
from zope.interface import Invalid
from zope.schema import Choice
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


def validate_link(value):
    parsed = urlparse(value.strip())
    if not all([parsed.scheme, parsed.netloc]):
        raise Invalid(_(u'Invalid link.'))
    return True


class IHighlightsTile(IPersistentCoverTile):
    """Displays a list of featured mobile apps."""

    image = field.NamedBlobImage(
        title=_(u'Image'),
        required=False,
    )

    image_description = schema.TextLine(
        title=_(u'Image description'),
        required=False,
        default=u'',
    )

    text = RichText(title=u'Text')

    tile_size = Choice(
        title=_(u'Tile size'),
        vocabulary=SimpleVocabulary([
            SimpleTerm(value=u'full', title=_(u'Full')),
            SimpleTerm(value=u'big', title=_(u'Big')),
            SimpleTerm(value=u'medium', title=_(u'Medium')),
            SimpleTerm(value=u'small', title=_(u'Small')),
        ]),
        required=True,
        default=u'big',
    )

    video_link = schema.ASCIILine(
        title=_(u'Video URL'),
        required=False,
        constraint=validate_link,
    )
    form.omitted('video_link')
    form.no_omit(ITileEditForm, 'video_link')

    more_link = schema.TextLine(title=_('Show more... link'), required=False)
    form.omitted('more_link')
    form.no_omit(ITileEditForm, 'more_link')
    form.widget(more_link='collective.cover.tiles.edit_widgets.more_link.MoreLinkFieldWidget')

    more_link_text = schema.TextLine(title=_('Show more... link text'), required=False)
    form.omitted('more_link_text')
    form.no_omit(ITileEditForm, 'more_link_text')


@implementer(IHighlightsTile)
class HighlightsTile(PersistentCoverTile):
    """Displays a Highlights section."""

    is_configurable = True
    is_droppable = False
    is_editable = True
    short_name = _(u'msg_short_name_highlights', default=u'Highlights')

    def get_srcset(self):
        data = self.data.get('image')
        scale_view = ImageScale(self, self.request, data=data, fieldname='')
        base_url, ext = scale_view.url.rsplit('.', 1)
        sizes = [(s, w, h) for s, (w, h) in getAllowedSizes().iteritems()]
        srcset = ''
        for i, (scale, width, height) in enumerate(sorted(sizes, key=lambda x: x[1])):
            srcset += '{0}image/{1} {2}w'.format(base_url, scale, width)
            if i + 1 < len(sizes):
                srcset += ', '
        return srcset

    @property
    def more_link(self):
        if not (self.data['more_link'] and self.data['more_link_text']):
            return None

        pc = api.portal.get_tool('portal_catalog')
        brainz = pc(UID=self.data['more_link'])
        if not len(brainz):
            return None

        return {
            'href': brainz[0].getURL(),
            'text': self.data['more_link_text'],
        }
