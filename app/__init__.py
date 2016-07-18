__author__ = "michael.ritsema@ziften.com"

from flask import Flask, send_from_directory, send_file, make_response
from qpylib import qpylib

app = Flask(__name__)