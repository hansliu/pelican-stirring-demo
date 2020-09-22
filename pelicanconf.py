#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Hans Liu'
SITENAME = 'Stirring: A Pelican theme'
SITEURL = 'https://hansliu.com/pelican-stirring-demo'

PATH = 'content'

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Pelican', 'https://getpelican.com/'),
    ('Python.org', 'https://www.python.org/'),
    ('Jinja2', 'https://palletsprojects.com/p/jinja/')
)

DEFAULT_PAGINATION = 9

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'stirring'

# Stirring theme variables
SITEFAVICON = 'https://hansliu.com/pelican-stirring-demo/images/favicon.ico'
SITEAUTHORS = {
    'Hans Liu': {
        'image': 'https://www.gravatar.com/avatar/9f7a4464129bd81ca5ac89e8067a5178?s=110',
        'description': 'Is a programmer, photographer, and traveler.'
    }
}
SITECATEGORIES = {
    'demo': {
        'image': 'images/demo.png'
    }
}

THEME_MENUITEMS = (
    ('Home', '#', 'fas fa-home'),
    ('About', '#', 'fas fa-address-card')
)
THEME_SOCIAL = (
    ('LinkedIn', 'https://linkedin.com/in/liuhans', 'fab fa-linkedin fa-2x'),
    ('Github', 'https://github.com/hansliu', 'fab fa-github-square fa-2x')
)
INTERNAL_LINKS = (
    ('Terms', 'pages/tos.html'),
    ('Privacy', 'pages/privacy.html')
)

GOOGLE_CUSTOM_SEARCH = "011860739956157042125:fttd__0pkbu"
DISQUS_SITENAME = 'hansliu'
GOOGLE_ANALYTICS = 'UA-49957360-1'
