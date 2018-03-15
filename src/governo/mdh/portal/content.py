# -*- coding: utf-8 -*-
from governo.mdh.portal.interfaces import IMinistry
from plone.dexterity.content import Container
from zope.interface import implementer


@implementer(IMinistry)
class Ministry(Container):
    """A ministry."""
