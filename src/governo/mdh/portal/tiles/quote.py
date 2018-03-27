# -*- coding: utf-8 -*-
from collective.cover.interfaces import ITileEditForm
from collective.nitf.tiles.nitf import INITFTile
from collective.nitf.tiles.nitf import NITFTile
from governo.mdh.portal import _
from plone.autoform import directives as form
from zope import schema
from zope.browserpage import ViewPageTemplateFile
from zope.interface import implementer
from zope.schema import Choice
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


class IQuoteTile(INITFTile):

    """A tile that shows an article quote."""

    form.omitted('quote_color')
    form.no_omit(ITileEditForm, 'quote_color')
    quote_color = Choice(
        title=_(u'Quote color'),
        vocabulary=SimpleVocabulary([
            SimpleTerm(value=u'blue', title=_(u'Blue')),
            SimpleTerm(value=u'green', title=_(u'Green')),
        ]),
        required=True,
        default=u'blue',
    )

    form.omitted('quote')
    form.no_omit(ITileEditForm, 'quote')
    quote = schema.Text(
        title=_(u'Quote'),
        required=False,
    )

    form.omitted('quote_rights')
    form.no_omit(ITileEditForm, 'quote_rights')
    quote_rights = schema.TextLine(
        title=_(u'Quote Rights'),
        required=False,
    )


@implementer(IQuoteTile)
class QuoteTile(NITFTile):

    """A tile that shows an article quote."""

    index = ViewPageTemplateFile('quote.pt')
    short_name = _(u'msg_short_name_quote', u'Quote')

    def color_class(self):
        return 'quote-' + self.data['quote_color']

    def quote(self):
        return self.data.get('quote', '')

    def quote_rights(self):
        return self.data.get('quote_rights', '')
