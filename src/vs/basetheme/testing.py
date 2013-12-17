from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class VsBasetheme(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import vs.basetheme
        xmlconfig.file('configure.zcml',
                       vs.basetheme,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'vs.basetheme:default')

VS_BASETHEME_FIXTURE = VsBasetheme()
VS_BASETHEME_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(VS_BASETHEME_FIXTURE, ),
                       name="VsBasetheme:Integration")