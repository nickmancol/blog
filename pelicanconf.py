#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Nicolas Bohorquez'
SITENAME = 'Data cosmonaut'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images', 'pdfs']
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
         ('Tiempo Fuera', 'https://tiempofuera.wordpress.com/'),
         ('VidaNP', 'https://vidanp.wordpress.com/'),
         ('Roel Pi', 'http://roelpeters.be/'),)

# Social widget
SOCIAL = (('CV', 'https://nicolasbohorquez.com'),
          ('Tiempo Fuera', 'https://tiempofuera.wordpress.com/'),
          ('VidaNP', 'https://vidanp.wordpress.com/'),
          ('Roel Pi', 'http://roelpeters.be/'),)

DEFAULT_PAGINATION = 10

THEME = "./themes/gum"
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
GOOGLE_ANALYTICS_ID = 'UA-116705941-3'
GOOGLE_ANALYTICS_SITENAME = 'Data Cosmonaut'

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['assets', 'sitemap', 'gravatar'
           , 'neighbors', 'related_posts', 'series'
           ]
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
DEFAULT_METADATA = {
    'status': 'draft',
}
