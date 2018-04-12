# -*- coding: utf-8 -*-
from governo.mdh.portal import _
from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from zope import schema
from zope.interface import Interface
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

colors = SimpleVocabulary([
    SimpleTerm(value="inverter-white", token=1, title=u'Cores Brancas'),
    SimpleTerm(value="default", token=2, title=u'Cores Pretas'),
])


class IBrowserLayer(Interface):
    """Add-on specific layer."""


class IMinistry(model.Schema):
    """A ministry."""

    title = schema.TextLine(
        title=_(u'label_title', default=u'Name'),
        description=_(
            u'help_title', default=u'The name of the ministry.'),
        default=u'',
        required=True,
    )

    description = schema.Text(
        title=_(u'label_description', default=u'Description'),
        description=_(
            u'help_description',
            default=u'A brief text describing the mission of the ministry.'),
        default=u'',
        required=True,
    )

    minister = schema.TextLine(
        title=_(u'label_minister', default=u'Minister'),
        description=_(
            u'help_minister', default=u'The name of the minister.'),
        default=u'',
        required=True,
    )

    image = NamedBlobImage(
        title=_(u'label_image', default=u'Photo (close-up)'),
        description=_(
            u'help_image',
            default=u'A photo of the minister in close-up.'),
        required=True,
    )

    lead_image = NamedBlobImage(
        title=_(u'label_lead_image', default=u'Photo (lead image)'),
        description=_(
            u'help_lead_image',
            default=u'A photo of the minister to be used as lead image.'),
        required=True,
    )

    text = RichText(
        title=_(u'Body text'),
        required=False,
    )

class ITimeline(model.Schema):
    """A timeline."""

    title = schema.TextLine(
        title=_(u'label_title', default=u'Title'),
        description=_(
            u'help_title', default=u'The title of timeline.'),
        default=u'',
        required=True,
    )

    description = schema.Text(
        title=_(u'label_description', default=u'Description'),
        description=_(
            u'help_description',
            default=u'A brief text describing of timeline.'),
        default=u'',
        required=False,
    )

    more_information = schema.TextLine(
        title=_(u'label_more_information', default=u'More Informartion'),
        description=_(
            u'help_more_information', default=u'The field for more information.'),
        default=u'',
        required=False,
    )

    image_timeline = NamedBlobImage(
        title=_(u'label_image_timeline', default=u'Image Timeline'),
        description=_(
            u'help_image_timeline',
            default=u'A photo of Timeline.'),
        required=True,
    )

    year = schema.TextLine(
        title=_(u'label_year', default=u'Year'),
        description=_(
            u'help_year', default=u'The year of timeline.'),
        default=u'',
        required=False,
    )

    month = schema.TextLine(
        title=_(u'label_month', default=u'Month'),
        description=_(
            u'help_month', default=u'The month of timeline.'),
        default=u'',
        required=False,
    )

class ITheme(model.Schema):
    """A Theme."""

    title = schema.TextLine(
        title=_(u'label_title', default=u'Theme'),
        description=_(
            u'help_title', default=u'The theme.'),
        default=u'',
        required=True,
    )

    theme_top_image = NamedBlobImage(
        title=_(u'label_theme_top_image', default=u'Photo (top theme)'),
        description=_(
            u'help_theme_top_image',
            default=u'A photo for top theme.'),
        required=True,
    )

    color_top = schema.Choice(
        vocabulary=colors,
        title=_(u'label_color_top', default=u'Color Top'),
        description=_(
            u'help_color_top',
            default=u'A color contrast top.'),
        required=True,
        default='default',
    )