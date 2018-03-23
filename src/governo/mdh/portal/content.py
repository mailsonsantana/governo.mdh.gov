# -*- coding: utf-8 -*-
from governo.mdh.portal.interfaces import IConselho, ITimeline, ITheme
from plone.dexterity.content import Container
from zope.interface import implementer


@implementer(IConselho)
class Conselho(Container):
    """A ministry."""

@implementer(ITimeline)
class Timeline(Container):
    """A Timeline."""

@implementer(ITheme)
class Theme(Container):
    """A Theme."""