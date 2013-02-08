from bs4 import BeautifulSoup
from pprint import pprint
import requests
import urllib2
import urllib
import datetime

def scrape_for_vine(query1,query2=""):
	
	url = "https://twitter.com/search/realtime?q=vine.co%2Fv%2F+%2B+"+query1+query2+"&src=typd"
	html = urllib2.urlopen(url).read()
	soup = BeautifulSoup(html)
	vine_url_array=[]
	vine_dict={}

	for instance in soup.find_all('span',{'class' : 'js-display-url'}):
		vine_url = instance.get_text()
		vine_url_array.append(vine_url)
		#print vine_url_array	
	
	for i in vine_url_array:
		i='http://'+i
		soupe = BeautifulSoup( urllib2.urlopen(i).read() )
		link = soupe.source['src']
		title = soupe.p.get_text()
		vine_dict[title]=link
		print soupe.div('class':'user').img['src']


	'''
	soupe = BeautifulSoup( urllib2.urlopen('http://vine.co/v/b1gqDWpwT1z').read() )
	print soupe.source['src']
	print soupe.p.get_text()
	'''


if __name__ == '__main__':
	print '-------------------> Lets scrape them vines <-------------------'
	scrape_for_vine("london")