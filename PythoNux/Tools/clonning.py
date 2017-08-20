from time import *
import os
import sys
import urllib
import socket

###################################
# FEITO PELO GRUPO T34M D38UT1SEC #
###################################

if (os.name == 'nt'):
	os.system('cls')
else:
	os.system('clear')

try:
	host = str(raw_input('Digite um site para clonar com http:// no comeco: '))

	rep = host.replace('http://','')

	ip = socket.gethostbyname(rep)

	print ("[+] Clonando site",host)
	print("\n")
	sleep(1)
	print ("[+] IP: ",ip)

	try:
		url = urllib.urlopen(host)
		result = (url.read())
		arq = file('site.html','w')
		arq.write(result)
		arq.close()
		print ("\n[+] Clonado com sucesso!")
	except Exception as a:
		print (a)
		print ("[-] Erro ao Guardar arquivo..")

except KeyboardInterrupt:
	print ("[+] Control-C Pressionado..")
	raise SystemExit