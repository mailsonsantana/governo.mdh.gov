# -*- coding: utf-8 -*-

from BTrees.IIBTree import intersection
from plone import api

from governo.mdh.portal import _
from urlparse import urlparse
from zope.interface import Invalid


MESSAGE = _(u'You must use "Title|http://example.org" format to fill each line.')


def validate_urls(value):
    """Validate URL items."""
    if not value:
        return True
    for item in value:
        # Check string format
        if '|' not in item or item.count('|') > 1:
            raise Invalid(MESSAGE)

        # Check if url is valid
        _, v = item.split('|')
        validate_url(v)
        parsed = urlparse(v.strip())
        if not all([parsed.scheme, parsed.netloc]):
            raise Invalid(MESSAGE)
    return True


def validate_url(value):
    """Validate URL item."""
    if not value:
        return True
    parsed = urlparse(value.strip())
    if not all([parsed.scheme, parsed.netloc]):
        raise Invalid(_(u'You must use "http://example.org" format.'))
    return True


def subjects_under_context(path=None,indexname='Subject'):
        """valid subjects under the given context
        """
        pcat = api.portal.get_tool('portal_catalog')
        cat = pcat._catalog
        path_idx = cat.indexes['path']
        tags_idx = cat.indexes[indexname]
        result = []
        # query all oids of path - low level
        portal = api.portal.getSite()
        if getattr(portal,'mdh',None):
            temas = getattr(portal,'navegue-por-temas',None)
            path = temas
        else:
            path = portal
        pquery = {
            'path': {
                'query': '/'.join(path.getPhysicalPath()),
                'depth': -1,
            }
        }
        path_result, info = path_idx._apply_index(pquery)
        for tag in tags_idx.uniqueValues():
            tquery = {indexname: tag}
            tags_result, info = tags_idx._apply_index(tquery)
            if intersection(path_result, tags_result):
                result.append(tag)
        return result
