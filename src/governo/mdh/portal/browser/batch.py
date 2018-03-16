# -*- coding: utf-8 -*-
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.batching.browser import BatchView
from ZTUtils import make_query


class TemasBatchView(BatchView):
    """
    """

    index = ViewPageTemplateFile("templates/navigation.pt")

    def __call__(self, batch, batchformkeys=None,
                 minimal_navigation=False,
                 show_page_range=False,
                 ajaxcontentid='content-batch'):
        super(BatchView, self).__call__(
            batch, batchformkeys, minimal_navigation)
        self.ajaxcontentid = ajaxcontentid
        self.show_page_range = show_page_range
        return self.index()

    def make_link(self,
                  pagenumber=0,
                  pagesize=None):
        form = self.request.form

        if self.batchformkeys:
            batchlinkparams = dict([(key, form[key])
                                    for key in self.batchformkeys
                                    if key in form])
        else:
            batchlinkparams = form.copy()

        if not pagesize:
            pagesize = self.batch.pagesize

        start = max(pagenumber - 1, 0) * pagesize
        return '%s?%s' % (self.request.ACTUAL_URL, make_query(batchlinkparams,
                                                              {self.batch.b_start_str: start,
                                                               'b_size': pagesize}))


