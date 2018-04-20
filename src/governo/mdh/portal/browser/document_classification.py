# -*- coding: utf-8 -*-
from plone import api
from Products.CMFPlone.utils import safe_unicode
from zope.publisher.browser import BrowserView

import json


class DocumentClassificationJsonView(BrowserView):

    """Json view to return all files respecting document finder tile options."""

    def _setup(self):
        self.uuid = self.request.get('uuid', '')
        self.searchable_text = safe_unicode(self.request.get('SearchableText', ''))
        self.current_documents = safe_unicode(self.request.get('currentDocuments[]', []))
        if type(self.current_documents) is unicode:
            self.current_documents = [self.current_documents]

        self.collection = api.content.get(UID=self.uuid)
        self.limit = 8

    def extract_data(self):
        """Extracts data from the current content"""

        custom_query = {
            'SearchableText': self.searchable_text,
            'sort_order': 'reverse',
        }
        results = self.collection.results(
            batch=False,
            brains=True,
            custom_query=custom_query,
            sort_on='Date',
        )

        files = []
        for brain in results:
            if self.current_documents and brain.document_type not in self.current_documents:
                continue
            if not self.current_documents and brain.document_type:
                continue
            files.append({
                'content': brain.Title,
                'title': brain.Description,
                'href': brain.getURL(),
            })
        return files[:self.limit]

    def __call__(self):
        self._setup()
        response = self.request.response
        response.setHeader('content-type', 'application/json')
        return response.setBody(json.dumps(self.extract_data()))
