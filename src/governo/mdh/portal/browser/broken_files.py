# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from plone import api

class BrokenFilesView(BrowserView):
    """View for list broken files."""

    def get_files(self):
        L = []
        files = api.content.find(portal_type='File')
        for file in files:
            D = {}
            obj = file.getObject()
            if obj.file is None:
                D['url'] = obj.absolute_url() + '/edit'
                D['title'] = obj.id
                L.append(D)
        return L
