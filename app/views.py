__author__ = "Ziften <michael.ritsema@ziften.com>"

import json
from app import app
from qpylib import qpylib
from flask import request, render_template, redirect, jsonify, Response
from collections import defaultdict
import urlparse
import dateutil.parser
from functools import wraps

base_url = 'https://sales.cloud.ziften.com'

@app.route('/ziftensearch', methods=['GET'])
def zsearch():
    ip = request.args.get('context')
    url = base_url + 'ipaddresses/overview/' + ip 
    #return ""
    return jsonify({'url': 'https://google.com'})