# -*- coding: utf-8 -*-
#from collective.z3cform.datagridfield import DataGridFieldFactory, DictRow
from governo.mdh.portal import _
from plone.app.textfield import RichText
from plone.directives import form
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from zope import schema
from zope.interface import Interface
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

colors = SimpleVocabulary([
    SimpleTerm(value="inverter-white", token=1, title=u'Cores Brancas'),
    SimpleTerm(value="default", token=2, title=u'Cores Pretas'),
])


# class ITableRowSchema(form.Schema):

#     title = schema.TextLine(title=u"Título", required=False)
#     url = schema.TextLine(title=u"Link", required=False)

class IBrowserLayer(Interface):
    """Add-on specific layer."""


class IConselho(model.Schema):
    """A ministry."""

    title = schema.TextLine(
        title=_(u'label_title', default=u'Title'),
        description=_(
            u'help_title', default=u'The title page.'),
        default=u'',
        required=True,
    )

    description = schema.Text(
        title=_(u'label_description', default=u'Description'),
        description=_(
            u'help_description',
            default=u'A brief text describing page.'),
        default=u'',
        required=True,
    )


    lead_image = NamedBlobImage(
        title=_(u'label_lead_image', default=u'Photo (lead image)'),
        description=_(
            u'help_lead_image',
            default=u'A photo of background top to be used as lead image.'),
        required=True,
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

    subtitle = schema.TextLine(
        title=_(u'label_subtitle', default=u'Subtitle'),
        description=_(
            u'help_subtitle', default=u'The subtitle of timeline.'),
        default=u'',
        required=False,
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


    # Verificar erro ao utilizar o collective.z3cform.datagridfield
    # form.widget(features=DataGridFieldFactory)
    features = schema.Text(
        title=_(u'label_features', default=u'Features'),
        description=_(
            u'help_features', default=u'The list features.'),
        required=False,
        # value_type=DictRow(title=u"List features top",
        #     schema=ITableRowSchema),
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
