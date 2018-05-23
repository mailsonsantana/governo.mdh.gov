# -*- coding: utf-8 -*-
from DateTime import DateTime
from plone import api
from plone.app.search.browser import quote_chars
from Products.Five.browser import BrowserView
from plone.i18n.normalizer.interfaces import IIDNormalizer
from governo.mdh.portal.utils import subjects_under_context
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory


EVER = DateTime(0).Date()


class SearchLibraryView(BrowserView):
    """View for media types with filter."""

    def toogle_greenbar(self):
        """Disable the green bar for anonynmous users."""
        if api.user.is_anonymous():
            self.request.set('disable_border', 1)

    def results(self, b_size=5, b_start=0):
        """Apply a custom query over the collection results."""
        custom_query = {}
        b_start = int(b_start)

        text = self.request.form.get('SearchableText', '')
        if text:
            custom_query['SearchableText'] = quote_chars(text)

        created = self.request.form.get('created', {})
        if self.valid_period(created):
            custom_query['created'] = created

        types = self.request.form.get('document_type',{})
        if types:
            custom_query['document_type'] = types

        # TODO:Esta impedindo de ordenar a coleção por ordem de criação 
        # sort_on = self.request.form.get('sort_on', '')
        # if sort_on not in ('', 'Date', 'sortable_title'):
        #     sort_on = ''
        tags = self.request.form.get('themes',{})
        if tags:
            custom_query['Subject'] = tags
        # sort_order = 'reverse' if sort_on == 'Date' else 'ascending'
        # custom_query['sort_order'] = sort_order

        results = self.context.results(
            b_start=b_start,
            b_size=b_size,
            custom_query=custom_query,
            # sort_on=sort_on,
        )
        return results


    def get_document_types(self):
        name = 'governo.mdh.portal.DocumentTypes'
        vocabulary = getUtility(IVocabularyFactory, name)
        return vocabulary(None)

    def documents_select(self):
        types = self.request.form.get('document_type', '')
        if types:
            return ','.join(types)
        else:
            return ''
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
    def valid_period(self, period):
        period = period.get('query', [])
        try:
            return period[0].Date() > EVER
        except (AttributeError, IndexError, TypeError):
            return False

    def checked(self):
        """Return the selected period."""
        created = self.request.form.get('created', {})
        created = created.get('query', [])

        try:
            return created[0].Date()
        except (AttributeError, IndexError, TypeError):
            # select EVER if value is not what we expect
            return EVER
