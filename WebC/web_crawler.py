import argparse
import requests
import re

menu = """\033[1;36m
  ____                    _               
 / ___|_ __ __ ___      _| | ___ _ __    
| |   | '__/ _` \ \ /\ / / |/ _ \ '__| 
| |___| | | (_| |\ V  V /| |  __/ |    
 \____|_|  \__,_| \_/\_/ |_|\___|_|    
                                                            
Powered by Adriel Freud\n\033[1;m""" 

parse = argparse.ArgumentParser(description="Url for Get Informations of WebSite")
parse.add_argument("-u", "--url", help="Url for get Informations! ")
args = parse.parse_args()

url = args.url
to_crawl = [url]
crawled = set()
emails_found = set()

header = {'user-agent': 'Mozilla/5.0 (X11; Linux i686; rv:43.0) Gecko/10100101 Firefox/43.0 Iceweasel/43.0.4'}

def crawling(url):
	while True:
		url = to_crawl[0]
		try:
			req = requests.get(url, headers=header)
		except:
			to_crawl.remove(url)
			crawled.add(url)
			continue

		html = req.text
		links = re.findall(r'<a href="?\'?(https?:\/\/[^"\'>]*)', html)
		print ("\n\033[1;36m[==>]Crawling: %s\033[1;m"%url)
		emails = re.findall(r'[\w\._-]+@[\w\_-]+\.[\w\._-]+\w', html)
		to_crawl.remove(url)
		crawled.add(url)

		for link in links:
			if link not in crawled and link not in to_crawl:
				to_crawl.append(link)
		for email in emails:
			emails_found.add(email)
			print('\n\033[31m[==>] Email: %s\033[1;m'%emails_found)
		
if args.url:
	print(menu)
	crawling(args.url)
else:
	print(menu)
	parse.print_help()
