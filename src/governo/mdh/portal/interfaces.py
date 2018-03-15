# -*- coding: utf-8 -*-
from governo.mdh.portal import _
from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from zope import schema
from zope.interface import Interface


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
