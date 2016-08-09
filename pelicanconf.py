#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'pierreorz'
SITEURL = 'http://dengdezhao.cn'
#SITEURL='http://localhost:8000'
SITENAME='Dengdezhao'
PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh_CN'
DEFAULT_DATE_FORMAT=('%Y-%m-%d(%A) %H:%M')
USE_FOLDER_AS_CATEGORY=True
DEFAULT_CATEGORY='hide'
FEED_ATOM='feeds/atom.xml'
FEED_RSS='feeds/rss.xml'
FEED_ALL_ATOM=None
FEED_ALL_RSS=None
CATEGORY_FEED_ATOM=None
TRANSLATION_FEED_ATOM=None

MENUITEMS=[('Home',SITEURL),('About','about.html'),]

MD_EXTENSIONS = [
  "extra",
  "toc",
  "headerid",
  "meta",
  "sane_lists",
  "smarty",
  "wikilinks",
  "admonition",
  "codehilite(guess_lang=False,pygments_style=emacs,noclasses=True)"]
CNZZ_ANALYTICS = True
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'

DISPLAY_CATEGORIES_ON_MENU = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME='new-bootstrap2'

PLUGIN_PATHS=[u"../pelican-plugins"]
PLUGINS=["sitemap"]
SITEMAP={
	"format":"xml",
	"priorities":{
		"articles":0.7,
		"indexes":0.5,
		"pages":0.3,
	},
	"changefreqs":{
		"articles":"monthly",
		"indexes":"daily",
		"pages":"monthly",
	}
}

STATIC_PATHS=[u"static"]

