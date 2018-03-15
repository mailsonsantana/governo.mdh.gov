# -*- coding: utf-8 -*-
from governo.mdh.portal.config import PROJECTNAME
from governo.mdh.portal.interfaces import IBrowserLayer
from governo.mdh.portal.testing import INTEGRATION_TESTING
from plone.browserlayer.utils import registered_layers

import unittest


DEPENDENCIES = (
    'brasil.gov.portal',
)


class InstallTestCase(unittest.TestCase):
    """Ensure product is properly installed."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = self.portal['portal_quickinstaller']

    def test_installed(self):
        self.assertTrue(self.qi.isProductInstalled(PROJECTNAME))

    def test_dependencies_installed(self):
        expected = set(DEPENDENCIES)
        installed = self.qi.listInstalledProducts(showHidden=True)
        installed = set([product['id'] for product in installed])
        result = sorted(expected - installed)
        self.assertEqual(result, [], 'Not installed: ' + ', '.join(result))

    def test_browser_layer_installed(self):
        self.assertIn(IBrowserLayer, registered_layers())

    def test_add_permissions(self):
        permission = 'governo.mdh.portal: Add Ministry'
        expected = ['Contributor', 'Manager', 'Owner', 'Site Administrator']
        roles = self.portal.rolesOfPermission(permission)
        roles = [r['name'] for r in roles if r['selected']]
        self.assertListEqual(roles, expected)

    def test_setup_permission(self):
        permission = 'governo.mdh.portal: Setup'
        roles = self.portal.rolesOfPermission(permission)
        roles = [r['name'] for r in roles if r['selected']]
        expected = ['Manager', 'Site Administrator']
        self.assertListEqual(roles, expected)
