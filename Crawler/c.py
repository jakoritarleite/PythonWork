#/usr/bin/python

# Desenvolvido por Adriel Freud!
# Contato: usuariocargo2016@gmail.com 
# FB: http://www.facebook.com/xrn401
#   =>DebutySecTeamSecurity<=

# MODO DE USO: crawler.py http://site.com/
# OBS: Nao esqueca do 'HTTP' or 'HTTPS'

import sys, urllib, re
from bs4 import BeautifulSoup
from time import sleep


site = sys.argv[1]
abrir = urllib.urlopen(site)
resp = abrir.code

if resp == 200:
	print("\n[*]Request Succefully!\n")
	bt = BeautifulSoup(abrir.read(), "lxml")
	allinks = bt.find_all('a')
	try:

		allinks0 = bt.find_all('meta')
		print("\033[1;36m<================== Information ==================>\n\n \033[1;m ")
		for link in allinks0:
			print("\033[31m[!]Information: \033[1;m"+ str(link['content']))
			print("")
	except:
		pass
	link1 = bt.link['href']
	link2 = bt.img['src']



	print("\033[1;36m<==================== Links ====================>\n\n \033[1;m ")
	print("\033[31m[+]Link: \033[1;m"+ str(link1))
	print("")
	print("\033[31m[+]Link: \033[1;m"+ str(link2))
	print("")
	print("")
	for link in allinks:
		print("\033[31m[+]Link: \033[1;m"+ str(link['href']))
		print("")
	print("\n\n\033[1;36m<==================== Emails! ====================> \033[1;m")
	abrir = urllib.urlopen(site)
	code = (abrir.read())
	mail = re.findall(r"[\w.]+[\w-]+[\w_]+[\w.]+[\w-]+[\w_]@[\w.]+[\w-]+[\w_]+[\w.]+[\w-]+[\w_]",code)
	for i in mail:
		print ('\n\033[31m[*]Email> \033[1;m' + str(i))

else:
	print("\n\033[31m[!]Request Failed, Exiting Program...\n \033[1;m")
	sleep(5)
exit()
