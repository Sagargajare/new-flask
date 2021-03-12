import os.path

from flask import Flask
from flask import request
from flask import jsonify
import cv2

from time import gmtime, strftime
import logging
import sys
import uuid


# from . import api_ver
# import mrz_parser

""" The flask app for serving predictions """
app = Flask(__name__, static_folder='')

#setting_err = app_utils.load_settings(app)




from app import app
from app import app_utils
from app import app_utils
setting_err = app_utils.load_settings(app, 'localhost')
if setting_err:
    logging.error(setting_err)
    sys.exit()
from app import constants
from app import mrz_parser