#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Nicolas Bohorquez'
SITENAME = 'Cosmonaut Coder Blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Bogota'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('CV', 'https://nicolasbohorquez.netlify.com/'),
         ('MADAS', 'http://madas.carloalberto.org/'),
         ('Roel Pi', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

THEME = "./themes/pelican-striped-html5up"

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['sitemap', 'gravatar'
           , 'neighbors'
           ]
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
