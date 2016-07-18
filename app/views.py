__author__ = "Ziften <michael.ritsema@ziften.com>"

from app import app
from flask import request, render_template, redirect, jsonify, Response


base_url = 'https://sales.cloud.ziften.com'

@app.route('/ziftensearch', methods=['GET'])
def zsearch():
    ip = request.args.get('context')
    url = base_url + 'ipaddresses/overview/' + ip 
    #return ""
    return jsonify({'url': url})