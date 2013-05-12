import urllib
import json

page=1

while page<=10:
	response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft&page=%(page)i"%{"page":page})
	result=json.load(response)
	for tweet in result[u'results']:
		print tweet[u'text']
	page=page+1
