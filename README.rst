**********************************
Portal Ministério dos Direitos Humanos
**********************************

.. contents:: Conteúdos
   :depth: 2

Introdução
==========

Este pacote contém o código fonte do Ministério dos Direitos Humanos
A documentação inclusa descreve o procedimento de instalação e atualização baseado na Identidade Digital do Governo (IDG).

Esta documentação não pretende substituir a `documentação do IDG <http://identidade-digital-de-governo-plone.readthedocs.io/>`_,
mas complementar ela adicionando só os passos necessários para instalar os componentes do portal.

Componentes do portal
=====================

Este pacote inclui as seguintes customizações e componentes:

* Tipo de conteúdo ``Ministério``,``Tema``,``Timeline``
* Tiles de collective.cover (``carousel``, ``gallery``, ``highlights``, ``navigation``, ``photoday``,``composicao``,``carouseldevideos``,``documentfinder``,``photogallery``,``search``,``theme``,``timeline``)
* Código CSS e JavaScript para o tema gerado pelo webpack

Pré-requisitos
==============

A instalação do portal requere de uma série de pré-requisitos de software e hardware que devem ser satisfeitos.
Os pré-requisitos estão descritos a fundo na documentação do IDG:

Software
--------

* Sistema operacional homologado (Debian/Ubuntu ou CentOS) atualizado na versão suportada mais recente
* Dependências de compilação do Zope instaladas e atualizsadas
* Ambiente virtual de Python 2.7 atualizado
* Usuário ``plone`` criado

Consulte a documentação do IDG para maior informação sobre como instalar cada um desses componentes.

Hardware
--------

Os requerimentos de hardware dependem do número de acessos de usuários anónimos e número de editores simultáneos.
Tomando em conta o histórico do portal sugerimos a instalação em máquinas virtuais com pelo menos um processador e 4GB de memória por instância de Zope ativa.

O número total de máquinas virtuais necessárias não pode ser calculado com antecedencia,
pois o valor dependerá de parámetros de configuração de caching e do uso do portal.

Vários problemas de software conhecidos no IDG que causavam consumo alto de recursos tem sido resolvidos nos últimos anos,
pelo que consideramos que o portal deveria ter um funcionamento estável con recursos bem inferiores aos atuais.

Porém, recomendamos iniciar com uma arquitetura similar e se ajustar para em baixo toda vez que tenha sido confirmado que os recursos são suficientes.

Instalação
==========

Descarregue e instale o IDG do branch ``master`` utilizando uma configuraçao ZEO de acordo a documentação do projeto.
Inicie todos os componentes do stack começando pelo servidor ZEO e continuando pelas instâncias.

Confira se é possivel criar normalmente um portal IDG padrão.
Caso de falhas revise os logs do buildout e/ou o log de eventos do Zope,
corrigindo qualquer problema detetado.

Realice as seguintes modificações no seu buildout de produção:

Adicione o código do Portal nos eggs e a referência da fonte para descarga do pacote:

.. code-block:: ini

    [buildout]
    ...
    eggs +=
        governo.mdh.portal

    extensions = mr.developer
    always-checkout = force
    auto-checkout =
        brasil.gov.agenda
        brasil.gov.portal
        brasil.gov.temas
        governo.mdh.portal

    [sources]
    governo.mdh.portal = git clone https://jeffersonramal@bitbucket.org/jeffersonramal/governo.mdh.portal.git

Adicione também as seguintes partes:

.. code-block:: ini

    [buildout]
    ...
    parts +=
        ...
        node
        staticresources-brasilgovtemas
        staticresources-brasilgovagenda
        staticresources-portalmdh

    [node]
    recipe = gp.recipe.node
    version = 6.6.0
    npms = npm yarn webpack@3
    scripts = npm yarn webpack

    [staticresources-brasilgovtemas]
    recipe = sc.recipe.staticresources
    name = brasil.gov.temas
    short_name = brasilgovtemas
    directory = src/brasil.gov.temas/webpack

    [staticresources-brasilgovagenda]
    recipe = sc.recipe.staticresources
    name = brasil.gov.agenda
    short_name = brasilgovagenda
    directory = src/brasil.gov.agenda/webpack

    [staticresources-portalmdh]
    recipe = sc.recipe.staticresources
    name = portalplanalto
    short_name = portalmdh
    directory = src/governo.mdh.portal/webpack

Rode novamente o buildout;
Vários componentes novos serão descarregados e o tema do portal será gerado usando o webpack.
Reinicie todas as instâncias e confira que é possivel criar normalmente um portal vazío.
Caso de falhas revise os logs do buildout e/ou o log de eventos do Zope,
corrigindo qualquer problema detetado.

Acesse a ZMI através da url http://IP_DO_SERVIDOR:8080/manage_main
Acesse o portal_quickinstaller e selecione o produto Portal do Ministério dos Direitos Humanos
Clique em Install.