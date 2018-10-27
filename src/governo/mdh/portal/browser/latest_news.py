# -*- coding: utf-8 -*-
from collections import OrderedDict
from DateTime import DateTime
from governo.mdh.portal.utils import subjects_under_context
from plone import api
from plone.app.contentlisting.interfaces import IContentListing
from plone.i18n.normalizer.interfaces import IIDNormalizer
from plone.app.search.browser import quote_chars
from Products.CMFPlone.PloneBatch import Batch
from Products.Five.browser import BrowserView
from zope.component import getUtility


MEDIA = [
    'News Item',
    'collective.nitf.content'
]

EVER = DateTime(0).Date()


class LatestNewsView(BrowserView):
    """View for media types with filter."""

    def __call__(self):
        self.setup()
        return self.index()

    def setup(self):
        """Hide portlet columns and disable the green bar for
        anonynmous users.
        """
        self.request.set('disable_plone.leftcolumn', True)
        self.request.set('disable_plone.rightcolumn', True)
        if api.user.is_anonymous():
            self.request.set('disable_border', True)

    @staticmethod
    def filter_types(types):
        """Return a list of portal types listed above."""
        if not types:
            return MEDIA

        # respect `types_not_searched` setting
        plone_utils = api.portal.get_tool('plone_utils')
        types = plone_utils.getUserFriendlyTypes(types)
        return [t for t in types if t in MEDIA]

    def results(self, batch=True, b_size=16, b_start=0):
        """Return results collection context"""
        query = {
            'sort_on': 'created',
            'sort_order': 'reverse',
        }
        if batch:
            b_start = int(b_start)

        text = self.request.form.get('SearchableText', '')
        if text:
            query['SearchableText'] = quote_chars(text)

        portal_type = self.request.form.get('portal_type', '')
        portal_type = self.filter_types(portal_type)
        query['portal_type'] = self.filter_types(portal_type)

        created = self.request.form.get('created', {})
        if self.valid_period(created):
            query['created'] = created

        types = self.request.form.get('document_type',{})
        if types:
            query['document_type'] = types

        tags = self.request.form.get('themes',{})
        if tags:
            query['Subject'] = tags

        # TODO: include results in current context only
        results = api.content.find(**query)
        results = IContentListing(results)
        if batch:
            results = Batch(results, b_size, b_start)
        return results

    @staticmethod
    def valid_period(period):
        """Check if the selected period is valid."""
        period = period.get('query', [])
        try:
            return period[0].Date() > EVER
        except (AttributeError, IndexError, TypeError):
            return False

    def media(self):
        """Return a list of existing types that can be searched."""
        catalog = api.portal.get_tool('portal_catalog')
        types_tool = api.portal.get_tool('portal_types')
        used_types = catalog._catalog.getIndex('portal_type').uniqueValues()
        used_types = self.filter_types(used_types)
        return OrderedDict([
            (t, types_tool.getTypeInfo(t).Title()) for t in used_types])

    def checked(self):
        """Return the selected period."""
        created = self.request.form.get('created', {})
        created = created.get('query', [])

        try:
            return created[0].Date()
        except (AttributeError, IndexError, TypeError):
            # select EVER if value is not what we expect
            return EVER

    def get_all_subjects(self):
        subjects = subjects_under_context()
        L = []
        if subjects:
            for subject in subjects:
                D={}
                D['id'] = self.create_id(subject.lower()) 
                D['name'] = subject
                L.append(D)
        return L

    def create_id(self,name):
        normalizer = getUtility(IIDNormalizer)
        id = normalizer.normalize(name)
        return id

    def documents_select(self):
        types = self.request.form.get('document_type', '')
        if types:
            return ','.join(types)
        else:
            return ''