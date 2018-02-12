#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Nicolas Bohorquez'
SITENAME = 'Cosmonaut Coder'
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
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

THEME = "./pelican-themes/pelican-striped-html5up"

PLUGINS = ['assets', 'sitemap', 'gravatar'
           , 'neighbors'
           ]
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
