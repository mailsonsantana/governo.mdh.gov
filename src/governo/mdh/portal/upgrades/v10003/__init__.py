# -*- coding: utf-8 -*-
from governo.mdh.portal.logger import logger
from plone import api
JS = [
    '++resource++brasil.gov.agenda/brasilgovagenda.js',
    '++resource++portalmdh/swiper.min.js',
    '++resource++portalmdh/portalmdh.js',
    '++resource++contraste.js',
    '++resource++brasil.gov.portal/js/main.js',
    '++resource++brasil.gov.tiles/brasilgovtiles.js',
    '++resource++brasil.gov.timeline/swiper.min.js'
]
CSS = [
    '++resource++calendar_styles/calendar.css',
    '++resource++brasil.gov.agenda/brasilgovagenda.css',
    '++resource++brasil.gov.tiles/brasilgovtiles.css',
]

def deprecate_resource_registries(setup_tool):
    """Deprecate resource registries."""
    js_tool = api.portal.get_tool('portal_javascripts')
    for js in JS:
        if js in js_tool.getResourceIds():
            js_tool.unregisterResource(id=js)
        assert js not in js_tool.getResourceIds()  # nosec

    css_tool = api.portal.get_tool('portal_css')
    for css in CSS:
        if css in css_tool.getResourceIds():
            css_tool.unregisterResource(id=css)
        assert css not in css_tool.getResourceIds()  # nosec

    logger.info('Static resources successfully removed from registries')