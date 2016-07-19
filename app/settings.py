import os

def get_base_url():
	f = open('settings.txt','r')
	url = f.read()
	f.close()
 	return url

def set_base_url(url):
	f = open('settings.txt','w')
	f.write(url)
	f.close()