import os.path

from flask import Flask
from flask import request
from flask import jsonify
import cv2

from time import gmtime, strftime
import logging
import sys
import uuid

from app import app_utils
from app import app_utils

# import api_bridge
# import app_utils
from app import constants
from app import mrz_parser
# from . import api_ver
# import mrz_parser

""" The flask app for serving predictions """
app = Flask(__name__, static_folder='')

#setting_err = app_utils.load_settings(app)
setting_err = app_utils.load_settings(app, 'localhost')

if setting_err:
    logging.error(setting_err)
    sys.exit()

from app import app
