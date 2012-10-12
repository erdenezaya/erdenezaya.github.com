#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Erdenezaya.B"
SITENAME = u"Erdenezaya's note"
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Blogroll
LINKS =  (('blog', 'http://erdenezaya.com'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/erdenezayanma'),
          ('facebook', 'http://facebook.com/erdenezayanma'),)

DEFAULT_PAGINATION = 3

DISPLAY_PAGES_ON_MENU = "True"
DEFAULT_CATEGORY = ('Articles')
MD_EXTENSIONS = ['codehilite','extra']
MARKUP = ('rst', 'md')
ARTICLE_EXCLUDES = ('pages',)
#from pelican.plugins import related_posts
PLUGINS = ['pelican.plugins.related_posts',]
DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives')
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 50
STATIC_PATHS = ['imgs', 'js', 'css', 'less']
OUTPUT_PATH = '/home/macdrifter/webapps/pelican/'
ARTICLE_PERMALINK_STRUCTURE = '/%Y/%m/'
#CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
CATEGORY_FEED = 'feeds/%s.atom.xml'
FEED = 'feeds/all.atom.xml'
TAG_FEED = 'feeds/%s.atom.xml'
FILES_TO_COPY = [('CNAME', 'CNAME')]
COPYRIGHT = 'Copyright 2012 Erdenezaya.B, by Pelican'
#Plugins
PLUGINS = ['pelican.plugins.gravatar',]
THEME = 'bootstrap2'
