#! -*- coding: UTF-8 -*-
"""
    Instance script for correction of dates in the news

    Execution::
    bin/instance run corrige_datas.py

"""
from datetime import datetime
from DateTime import DateTime
import transaction
from Testing.makerequest import makerequest
from zope.component.hooks import setSite
from AccessControl.SecurityManagement import newSecurityManager

import pdb;pdb.set_trace()
# Configuracoes
portal_id = 'mdh'
user_id = 'admin'

# Use Zope application server user database (not plone site)
admin=app.acl_users.getUserById("admin")
newSecurityManager(None, admin)

# Usamos o makerequest para criar um request fake para este ambiente
app = makerequest(app)

# Pegamos o portal Plone
portal = portal_id 
site = app[portal] 

# Definimos qual e o site, algumas ferramentas precisam disso, como o FSS
setSite(site)

# Ate este momento estamos como usuario anonimo.
# usando o newSecurityManager nos damos as credenciais do usuario admin
newSecurityManager(None, app.acl_users.getUserById(user_id))

ct = site.portal_catalog

# Fazer uma busca no catalog por todas as noticias que deseja modificar a data
news = ct(portal_type='collective.nitf.content',path='/mdh/sdh/noticias/')
for new in news:
    # Pegar a data de criacao
    date_created = new.created

    # Pegar o objeto
    obj = new.getObject()

    # Setar a data de criacao na data de publicacao
    obj.setEffectiveDate(date_created)

    # Reindexar o objeto
    obj.reindexObject()

    print 'Alterando conteúdo ' + new.portal_type +'\n' \
          '\nTítulo:'+ new.Title +\
          '\n Nova Data: ' + str(new.created.strftime('%d/%m/%Y'))
    print '------------------------------------------------------------------'
    print '******************************************************************'

transaction.commit()
print '-------------- Commit da transacao --------------'
print '-------------------------------------------------'
print 'Foram alteradas ' + str(len(news)) + ' datas'


