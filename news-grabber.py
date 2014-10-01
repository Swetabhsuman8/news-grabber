"""
File: news-grabber.py
Author: kaushik
Email: kkaushik24@gmail.com
Description:script to get all the news from yahoo 
"""



import requests
import BeautifulSoup
import time
import codecs

streamWriter = codecs.lookup('utf-8')[-1]
url='http://in.news.yahoo.com/'
classify=['politics','world','internet','cricket','football','tennis']


def createLinks(content):
	"""docstring for createLinks"""
	
	soup=BeautifulSoup.BeautifulSoup(content)
	s=soup.findAll(attrs={'class' :'yom-mod yom-blist'},limit=3)
	m=[]
	for link in s:
		t=link.fetch('a')
		for l in t:
			m.append(l.get('href'))
	m=list(set(m))
	
	return m

def generateLinkContent(link,fprefix):
	"""docstring for generateLinkContent"""
	resp=requests.get(url+link)
	content=resp.text
	soup=BeautifulSoup.BeautifulSoup(content)
	s=soup.find(attrs={'itemprop' :'articleBody'})
	output  = open('./dataCollect/'+fprefix+'/' + fprefix + '.' 
                            + time.strftime('%Y%m%d-%H%M%S') + '.txt', 'w')
	output = streamWriter(output)

	para=s.fetch('p')
	for ln in para:
		output.write(ln.getText())
		
		

	

	

#bootstrapping starts here
for i in range(0,6):
	
	resp=requests.get(url+classify[i])
	content=resp.text
	links=createLinks(content)
	print (classify[i]+'\n\n')
	for ln in links:
		generateLinkContent(ln,classify[i])


