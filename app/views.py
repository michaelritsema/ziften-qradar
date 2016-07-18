__author__ = "Carbon Black <support@carbonblack.com>"

import json
from app import app
from qpylib import qpylib
from flask import request, render_template, redirect, jsonify, Response
import urllib
import config
from cbapi import CbApi
from collections import defaultdict
import urlparse
import dateutil.parser
from functools import wraps
import requests
import traceback
import os
import sqlite3
import pprint

base_url = 'https://sales.cloud.ziften.com'

@app.route('/search', methods=['GET'])
def search():
    ip = request.args.get('context')
    query = 'ipaddr:%s' % ipaddr
    url = base_url + 'ipaddresses/overview/' + ip 
    return jsonify({'url': url})