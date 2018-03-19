# -*- coding: utf-8 -*-
from governo.mdh.portal.browser.controlpanel import IMdhSettings
from plone.i18n.normalizer.interfaces import IIDNormalizer
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from zope.schema.vocabulary import SimpleVocabulary


def DocumentTypesVocabulary(context):
    """Document types vocabulary."""
    normalizer = getUtility(IIDNormalizer)
    registry = getUtility(IRegistry)
    settings = registry.forInterface(IMdhSettings)  # noqa: P001
    items = []
    for document_type in settings.available_document_types:
        token = normalizer.normalize(document_type)
        items.append(SimpleVocabulary.createTerm(token, token, document_type))
    return SimpleVocabulary(items)
