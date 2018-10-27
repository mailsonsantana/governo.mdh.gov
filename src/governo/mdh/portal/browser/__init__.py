# -*- coding: utf-8 -*-
from governo.mdh.portal.browser.filterresults import FilterResultsView  # noqa: E501,F401
from governo.mdh.portal.browser.searchlibrary import SearchLibraryView  # noqa: E501,F401
from governo.mdh.portal.browser.news import NewsView  # noqa: E501,F401

from plone.app.layout.viewlets import ViewletBase


class ResourcesViewlet(ViewletBase):
    """This viewlet inserts static resources on page header."""