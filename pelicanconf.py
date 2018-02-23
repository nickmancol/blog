#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Nicolas Bohorquez'
SITENAME = 'Data cosmonaut'
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
         ('Tiempo Fuera', 'https://tiempofuera.wordpress.com/'),
         ('VidaNP', 'https://vidanp.wordpress.com/'),
         ('Roel Pi', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('CV', 'https://nicolasbohorquez.netlify.com'),
          ('Github', 'https://github.com/nickmancol'),
          ('Linkedin', 'https://github.com/l/nickmancol'),
          ('Twitter', 'https://twitter.com/nickmancol'),
          ('MADAS', 'http://madas.carloalberto.org/'),
          ('Tiempo Fuera', 'https://tiempofuera.wordpress.com/'),
          ('VidaNP', 'https://vidanp.wordpress.com/'),
          ('Roel Pi', 'http://jinja.pocoo.org/'),)

DEFAULT_PAGINATION = 10

THEME = "./themes/gum"
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['assets', 'sitemap', 'gravatar'
           , 'neighbors', 'related_posts', 'series'
           ]
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
DEFAULT_METADATA = {
    'status': 'draft',
}
