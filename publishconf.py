#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# Production settings для GitHub Pages
SITEURL = 'https://laipni.github.io/tess-law-site'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Google Analytics (если нужно)
GOOGLE_ANALYTICS = None
