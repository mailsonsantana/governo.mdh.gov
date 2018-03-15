# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2


class Fixture(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # XXX: https://github.com/plone/plone.app.event/issues/81
        # Install products that use an old-style initialize() function
        z2.installProduct(app, 'Products.DateRecurringIndex')
        z2.installProduct(app, 'Products.Doormat')

        import governo.mdh.portal
        self.loadZCML(package=governo.mdh.portal)

    def setUpPloneSite(self, portal):
        self.applyProfile(portal, 'governo.mdh.portal:default')
        portal.portal_workflow.setDefaultChain('simple_publication_workflow')

    def tearDownZope(self, app):
        # Uninstall products installed above
        z2.uninstallProduct(app, 'Products.Doormat')
        z2.uninstallProduct(app, 'Products.DateRecurringIndex')


FIXTURE = Fixture()

INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name='governo.mdh.portal:Integration')

FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,), name='governo.mdh.portal:Functional')

ROBOT_TESTING = FunctionalTesting(
    bases=(FIXTURE, AUTOLOGIN_LIBRARY_FIXTURE, z2.ZSERVER_FIXTURE),
    name='governo.mdh.portal:Robot',
)
