import os

def get_base_url():
	url = ""
	try:
		f = open('settings.txt','r')
		url = f.read()
		f.close()
	except Exception as e:
		print e
		try:
			f = open('settings.txt','w')
			f.write("https://ZIFTEN_CONSOLE_URL_NOT_CONFIGURED.cloud.ziften.com")
			f.close()
		except Exception as e:
			print e
 	return url

def set_base_url(url):
	try:
		f = open('settings.txt','w')
		f.write(url)
		f.close()
	except Exception as e:
		print e