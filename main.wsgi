#! /srv/www/spotiboty/venv/bin/python

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/srv/www/spotiboty/public_html')
# This script will look for file called main.py because of the "from main..." below
from main import app as application
application.secret_key = 'anything you wish'
