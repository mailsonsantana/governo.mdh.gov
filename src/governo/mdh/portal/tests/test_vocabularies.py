# -*- coding: utf-8 -*-
from governo.mdh.portal.browser.controlpanel import IMdhSettings
from governo.mdh.portal.testing import INTEGRATION_TESTING
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from zope.component import queryUtility
from zope.schema.interfaces import IVocabularyFactory

import unittest


class VocabulariesTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        registry = getUtility(IRegistry)
        self.settings = registry.forInterface(IMdhSettings)  # noqa: P001

    def test_document_types_vocabulary(self):
        name = 'governo.mdh.portal.DocumentTypes'
        util = queryUtility(IVocabularyFactory, name)
        self.assertIsNotNone(util, None)
        document_types = util(self.portal)
        self.assertEqual(len(document_types), 3)
