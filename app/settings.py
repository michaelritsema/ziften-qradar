import os
import qpylib

def get_base_url():
	settings_filename = qpylib.qpylib.get_store_path(relative_path="") + 'settings.txt'

	url = ""
	try:
		f = open(settings_filename,'r')
		url = f.read()
		f.close()
	except Exception as e:
		print e
		try:
			f = open(settings_filename,'w')
			url = "https://ZIFTEN_CONSOLE_URL_NOT_CONFIGURED.cloud.ziften.com" 
			f.write(url)
			f.close()
		except Exception as e:
			print e
 	return url

def set_base_url(url):
	try:
		f = open(settings_filename,'w')
		f.write(url)
		f.close()
	except Exception as e:
		print e