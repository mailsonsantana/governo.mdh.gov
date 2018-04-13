# -*- coding: utf-8 -*-
from Products.CMFPlone.utils import getToolByName
from Products.Five import BrowserView

class View(BrowserView):
    """Default view for Ministry."""

    def has_agenda(self):
        """Verifica se possui agenda no contexto"""
        catalog = getToolByName(self.context, 'portal_catalog')
        path = '/'.join(self.context.getPhysicalPath())
        agenda = catalog(portal_type=['Agenda'],
                         path={'query': path})
        if agenda:
            return True
        return False

    def get_obj_compromisso(self):
        """ Retorna obj Agenda"""
        catalog = getToolByName(self.context, 'portal_catalog')
        path = '/'.join(self.context.getPhysicalPath())
        compromisso = catalog(portal_type=['Compromisso'],
                         path={'query': path})
        if compromisso:
            obj = compromisso[0].getObject()
            return obj
        return False

    def _format_time(self, value):
        return value.strftime('%Hh%M')

    def _translate(self, msgid, locale='plonelocales', mapping=None):
        tool = self._ts
        # XXX: Por que é retornado 'pt-br' do portal_state ao invés de 'pt_BR'?
        # Quando uso 'pt-br' ao invés de 'pt_BR', não pega a tradução quando
        # feita de forma manual.
        target_language = ('pt_BR' if self.current_language == 'pt-br'
                           else self.current_language)
        return tool.translate(msgid,
                              locale,
                              mapping=mapping,
                              context=self.context,
                              target_language=target_language)

    @property
    def date(self):
        context = self.get_obj_compromisso()
        date = context.start_date
        return date

    def weekday(self):
        date = self.date
        return date.strftime('%w')

    def month(self):
        date = self.date
        date = {}
        date['month'] = date
        return date.strftime('%m')

    def long_date(self):
        date = self.date
        parts = {}
        parts['day'] = date.strftime('%d')
        parts['month'] = self.month()
        parts['year'] = date.strftime('%Y')
        return self.context.translate(Message(_(u'long_date_agenda'),
                                              mapping=parts))

    def orgao(self):
        orgao = self.get_obj_compromisso().orgao
        return orgao

    def autoridade(self):
        autoridade = self.context.autoridade
        if not autoridade:
            autoridade = self.agenda.autoridade
        return autoridade

    def imagem(self):
        imagem = self.agenda.image
        if imagem:
            view = self.agenda.restrictedTraverse('@@images')
            scale = view.scale(fieldname='image', scale='large')
            tag = scale.tag()
            return tag

    def Title(self):
        parts = {}
        parts['weekday'] = self.weekday()
        parts['long_date'] = self.long_date()
        return '%(weekday)s, %(long_date)s' % parts

    def compromisso(self):
        obj = self.context
        comp = {}
        comp['autoridade'] = self.autoridade()
        comp['title'] = obj.Title()
        comp['description'] = obj.Description()
        comp['start_date'] = obj.start_date
        comp['start_time'] = self._format_time(comp['start_date'])
        comp['start_date'] = obj.start_date.strftime('%Y-%m-%d %H:%M')
        comp['end_date'] = obj.end_date
        comp['end_time'] = self._format_time(comp['end_date'])
        comp['end_date'] = obj.end_date.strftime('%Y-%m-%d %H:%M')
        comp['location'] = obj.location
        comp['attendees'] = obj.attendees
        # XXX: Preciso formatar esses dados pela view, uma vez que na
        # template causa erros durante o parse do i18ndude.
        # -FATAL- - ERROR in document:
        # <unknown>:55:44: not well-formed (invalid token)
        # No futuro pode ser interessante colocar essa definição no css.
        attendees = ''
        if comp['attendees']:
            attendees = comp['attendees'].split('\n')
        comp['attendees_formatted'] = '<br/>'.join(attendees)
        comp['url'] = obj.absolute_url()
        return comp
