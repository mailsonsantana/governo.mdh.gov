# -*- coding: utf-8 -*-
from governo.mdh.portal import _
from governo.mdh.portal.config import DEFAULT_DOCUMENT_TYPES
from plone.app.registry.browser import controlpanel
from plone.autoform import directives as form
from plone.supermodel import model
from zope import schema


class IMdhSettings(model.Schema):
    """Interface for the control panel form."""

    form.widget('available_document_types', rows=7)
    available_document_types = schema.List(
        title=_(u'Available Document Types'),
        description=_(u'List of available document types in the site.'),
        required=True,
        default=DEFAULT_DOCUMENT_TYPES,
        value_type=schema.TextLine(title=_(u'Document Type')),
    )


class MdhSettingsEditForm(controlpanel.RegistryEditForm):
    schema = IMdhSettings
    label = _(u'Portal MDH settings')
    description = _(u'Here you can modify settings for the site.')


class MdhSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = MdhSettingsEditForm
