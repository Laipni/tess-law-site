#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import datetime

AUTHOR = 'ТЕСС'
SITENAME = 'Юридическая фирма "ТЕСС"'
SITEURL = ''

PATH = 'content'
THEME = 'theme/tess-bootstrap'
TIMEZONE = 'Europe/Moscow'
DEFAULT_LANG = 'ru'

# ИСПРАВЛЕННЫЕ НАСТРОЙКИ
OUTPUT_PATH = 'output/'
BIND = '127.0.0.1'
PORT = 8000

# Feed generation
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Static paths
STATIC_PATHS = ['downloads', 'images']

# URLs
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

RELATIVE_URLS = True

# Jinja2 globals
JINJA_GLOBALS = {
    'now': datetime.datetime.utcnow,
}

# SEO
SITE_KEYWORDS = 'налоговый юрист, юридические услуги, налоговые консультации'

# Pagination
DEFAULT_PAGINATION = 10

# ИСПРАВЛЕННЫЕ НАСТРОЙКИ ДЛЯ РАБОТЫ СЕРВЕРА
CACHE_CONTENT = False
CACHE_PATH = 'cache'
CHECK_MODIFIED_METHOD = 'mtime'
LOAD_CONTENT_CACHE = False