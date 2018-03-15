# -*- coding: utf-8 -*-
from governo.mdh.portal import _
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope import schema
from zope.interface import provider


@provider(IFormFieldProvider)
class IDocumentClassification(model.Schema):
    """Document classification."""

    document_type = schema.Choice(
        title=_(u'Document Type'),
        vocabulary='governo.mdh.portal.DocumentTypes',
        required=True,
    )
