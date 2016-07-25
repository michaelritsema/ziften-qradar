__author__ = "Ziften <michael.ritsema@ziften.com>"

from app import app
from flask import request, render_template, redirect, jsonify, Response
import settings

ip_search_url = '/ipaddresses/ipaddresses?ipaddress__cidr='

def ipreportmanager(report_id, ip):
    url = '/ipreportmanager/%s/%s'
    return settings.get_base_url() + (url % (ip,report_id))

@app.route('/portsearch', methods=['GET'])
def portSearch():
    c = request.args.get('context')
    url = ipreportmanager(705,c)
    return jsonify({'url': url})

@app.route('/hostnamesearch', methods=['GET'])
def hostnameSearch():
    c = request.args.get('context')
    url = ipreportmanager(707,c)
    return jsonify({'url': url})

@app.route('/systemsearch', methods=['GET'])
def systemSearch():
    c = request.args.get('context')
    url = ipreportmanager(701,c)
    return jsonify({'url': url})

@app.route('/ipsearch', methods=['GET'])
def ipSearch():
    c = request.args.get('context')
    url = settings.get_base_url() + ip_search_url + c 
    return jsonify({'url': url})

@app.route('/md5search', methods=['GET'])
def md5Search():
    c = request.args.get('context')
    url = ipreportmanager(702,c)
    return jsonify({'url': url})

# Need to verify admin priv
@app.route('/ziftensettings', methods=['GET', 'POST'])
def ziftensettings():
    base_url = ""
    try:
        base_url = settings.get_base_url()
        if request.method == 'POST':
            base_url = request.form["base_url"]
            settings.set_base_url(request.form["base_url"])
            render_template("closewindow.html")

    except Exception as ex:
        print ex
      
    base_url = settings.get_base_url()
    return render_template("settings.html", base_url=base_url)

@app.route('/index', methods=['GET','POST'])
def index():
    return render_template("consoleframe.html", base_url=settings.get_base_url())
