# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

version = '1.0'
description = 'Portal Ministério dos Direitos Humanos'
long_description = (
    open('README.rst').read() + '\n' +
    open('CONTRIBUTORS.rst').read() + '\n' +
    open('CHANGES.rst').read()
)

setup(
    name='governo.mdh.portal',
    version=version,
    description=description,
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Plone',
        'Framework :: Plone :: 4.3',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='brasil plone gov',
    author='Jefferson Almeida',
    author_email='jralmeida88@gmail.com',
    url='https://bitbucket.org/jefferson.ramal/governo.mdh.portal.git',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['governo', 'governo.mdh'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'brasil.gov.portal',
        'collective.texttospeech',
        'ftw.upgrade',
        'plone.app.imagecropping',
        'plone.app.theming',
        'plone.autoform',
        'plone.resource',
        'Products.GenericSetup',
        'setuptools',
        'z3c.jbot',
        'zope.interface',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'plone.browserlayer',
            'plone.testing',
            'plone.app.robotframework',
        ],
    },
    entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
