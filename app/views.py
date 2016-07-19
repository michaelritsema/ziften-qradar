__author__ = "Ziften <michael.ritsema@ziften.com>"

bootstrap_server = False 

if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)
    bootstrap_server = True
else:
    from app import app

from flask import request, render_template, redirect, jsonify, Response
import settings




md5_search_url = '/binaries/binaries?imagefilemd5__contains='
filename_search_url = '/applications/applications?most_prevalent_filename__contains='
system_search_url = '/systems/systems?system__contains='
ip_search_url = '/ipaddresses/ipaddresses?ipaddress__cidr='
hostname_search_url ='/hostnames/hostnames?hostname__contains='
user_search_url = '/osusers/osusers?user_account__contains='


@app.route('/usersearch', methods=['GET'])
def userSearch():
    c = request.args.get('context')
    url = settings.get_base_url() + user_search_url + c 
    return jsonify({'url': url})

@app.route('/hostnamesearch', methods=['GET'])
def hostnameSearch():
    c = request.args.get('context')
    url = settings.get_base_url() + hostname_search_url + c 
    return jsonify({'url': url})

@app.route('/systemsearch', methods=['GET'])
def systemSearch():
    c = request.args.get('context')
    url = settings.get_base_url() + system_search_url + c 
    return jsonify({'url': url})

@app.route('/filenamesearch', methods=['GET'])
def filenameSearch():
    c = request.args.get('context')
    url = settings.get_base_url() + filename_search_url + c 
    return jsonify({'url': url})

@app.route('/ipsearch', methods=['GET'])
def ipSearch():
    c = request.args.get('context')
    url = settings.get_base_url() + ip_search_url + c 
    return jsonify({'url': url})

@app.route('/md5search', methods=['GET'])
def md5Search():
    c = request.args.get('context')
    url = settings.get_base_url() + md5_search_url + c 
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

    except Exception as ex:
        print ex
      
    base_url = settings.get_base_url()
    return render_template("settings.html", base_url=base_url , test="x")

if bootstrap_server:
    app.run('0.0.0.0')