# -*- coding: utf-8 -*-
from Acquisition import aq_parent

from brasil.gov.agenda.browser.mixin import AgendaMixin

from datetime import datetime
from datetime import timedelta
from plone.app.uuid.utils import uuidToObject

from zope.component import getMultiAdapter

from Products.CMFPlone.utils import getToolByName
from Products.Five import BrowserView

import time

class View(BrowserView, AgendaMixin):
    """Default view for Ministry."""

    def __init__(self, context, request):
          self.context = context
          self.request = request



    def has_agenda(self):
        """Verifica se possui agenda no contexto"""
        catalog = getToolByName(self.context, 'portal_catalog')
        path = '/'.join(self.context.getPhysicalPath())
        agenda = catalog(portal_type=['Agenda'],
                         path={'query': path})
        if agenda:
            return True
        return False

    def get_uuid_agenda(self):
        if self.has_agenda():
            catalog = getToolByName(self.context, 'portal_catalog')
            path = '/'.join(self.context.getPhysicalPath())
            agenda = catalog(portal_type=['Agenda'],
                             path={'query': path})
            uuid = agenda[0].getObject().UID()
            return uuid

    def _last_modified(self):
        agenda = uuidToObject(self.get_uuid_agenda())
        last_modified = int(agenda.modified().strftime('%s'))
        agenda_diaria = agenda.get(time.strftime('%Y-%m-%d'), None)
        if agenda_diaria:
            modified = int(agenda_diaria.modified().strftime('%s'))
            if modified > last_modified:
                last_modified = modified
            for compromisso in agenda_diaria.objectValues():
                modified = int(compromisso.modified().strftime('%s'))
                if modified > last_modified:
                    last_modified = modified
        return last_modified

    @property
    def agenda(self):
        return uuidToObject(self.get_uuid_agenda())

    def agenda_diaria(self):
        agenda = uuidToObject(self.get_uuid_agenda())
        agenda_diaria = agenda.get(time.strftime('%Y-%m-%d'), None)
        return agenda_diaria

    @property
    def agenda_url(self):
        return self.agenda.absolute_url()

    @property
    def agenda_title(self):
        return self.agenda.Title()

    def _collection_events(self, last_modified=None):
        agenda_diaria = self.agenda_diaria()
        page = []
        if agenda_diaria:
            now = datetime.now()
            catalog = getToolByName(self.context, 'portal_catalog')
            query = {}
            query['portal_type'] = 'Compromisso'
            query['sort_on'] = 'start'
            query['path'] = '/'.join(agenda_diaria.getPhysicalPath())
            results = catalog.searchResults(**query)
            for i, brain in enumerate(results):
                compr = brain.getObject()
                timestamp_class = ['timestamp-cell']
                if compr.start_date < now < compr.end_date:
                    timestamp_class.append('is-now')
                compromisso = {
                    'location': compr.location,
                    'description': compr.Title(),
                    'time': compr.start_date.strftime('%Hh%M'),
                    'timestamp_class': ' '.join(timestamp_class),
                }
                page.append(compromisso)
                is_third_item = (i + 1) % 3 == 0
                if is_third_item:
                    yield page
                    page = []
            if page:
                yield page

    def collection_events(self):
        return self._collection_events(self._last_modified())

    def _url_agenda(self, last_modified=None):
        agenda = uuidToObject(self.get_uuid_agenda())
        agenda_diaria = agenda.get(time.strftime('%Y-%m-%d'), None)
        if agenda_diaria:
            return agenda_diaria.absolute_url()

    def url_agenda(self):
        return self._url_agenda(self._last_modified())

    def _translate(self, msgid, locale='plonelocales', mapping=None):
            tool = getToolByName(self.context, 'translation_service')
            portal_state = getMultiAdapter((self.context, self.request),
                                           name=u'plone_portal_state')
            current_language = portal_state.language()
            # XXX: Por que é retornado 'pt-br' do portal_state ao invés de 'pt_BR'?
            # Quando uso 'pt-br' ao invés de 'pt_BR', não pega a tradução quando
            # feita de forma manual.
            target_language = ('pt_BR' if current_language == 'pt-br'
                               else self.current_language)
            return tool.translate(msgid,
                                  locale,
                                  mapping=mapping,
                                  context=self.context,
                                  target_language=target_language)

    def days(self):
        tool = getToolByName(self.context, 'translation_service')
        today = datetime.now()
        # get a list with 3 days before and 3 days after today
        days = [(today + timedelta(i)) for i in xrange(-3, 4)]
        weekdays = []
        for day in days:
            cssclass = ['day']
            if day == today:
                cssclass.append('is-selected')
            if self.agenda.get(day.strftime('%Y-%m-%d'), False):
                cssclass.append('has-appointment')
            strweek = self._translate(tool.day_msgid(day.weekday()))
            weekdays.append({
                'day': day.day,
                'weekday': strweek[:3],
                'iso': day.isoformat(),
                'cssclass': ' '.join(cssclass),
            })
        return weekdays

    def id(self):
        return self.agenda.UID()
