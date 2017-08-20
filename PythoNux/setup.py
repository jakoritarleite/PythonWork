# coding=utf-8

import os
import socket
import sys
import time

if os.name == 'nt':
	os.system('color a')

Menu = raw_input('''
 ____        _   _           _   _            
|  _ \ _   _| |_| |__   ___ | \ | |_   ___  __
| |_) | |_| | __| '_ \ / _ \|  \| | | | \ \/ /
|  __/|___  | |_| | | | (_) | |\  | |_| |>  < 
|_|       |_|\__|_| |_|\___/|_| \_|\__,_/_/\_\
\n		
Powered by Adriel Freud, Giu DBS.

		[1] Menu
		[2] Creditos

	[+] Escolha algumas da Opcoes acima.
				  
Interact>>> ''')

if Menu	== '1':
	fer = raw_input('''\n
######################
##                  ##
##   Ferramentas!   ##
##                  ##
######################

	[1] Scan De Portas Simples!
	[2] Sniffer!
	[3] Clonning Interface Web!
	[4] Encrypt Virus in ByteCode
	[5] SqlMap!
	[6] Connect in SSH!
	[7]

Interact>>> ''')
###############################################
	if fer == '1':
		try:	
			os.system('python Tools\portscan.py')
			print("")
		except:
			os.system('python Tools/portscan.py')


	if fer == '2':
		try:
			os.system('python Tools\sniffer.py')
			print("")
		except:
			os.system('python Tools/sniffer.py')



	if fer == '3':
		try:
			os.system('python Tools\clonning.py')
			print("")	
		except:
			os.system('python Tools/clonning.py')


	if fer == '4':
		try:
			print("")
			encrypt = raw_input('EncryptBack.py ')
			os.system('python Tools\EncryptBack.py' +' '+ encrypt)
			print("")
		except:
			print("")
			encrypted = raw_input('EncryptBack.py ')
			os.system('python Tools/EncryptBack.py' +' '+ encrypted)



	if fer == '5':
		try:
			print("")
			print("Insire os parametros apartir de...")
			print("")
			sqlmap = raw_input('sqlmap.py ')
			os.system('python Tools\sqlmap.py' +' '+ sqlmap)
			print("")
		except:
			print("")
			print("Insire os parametros apartir de...")
			sqlmap = raw_input("sqlmap.py ")
			os.system('python Tools/sqlmap.py' +' '+ sqlmap)

	if fer == '6':
		try:
			print("")
			os.system("python Tools\ssh_client.py")
		except:
			print("")
			os.system("python Tools/ssh_client.py")

################################################

elif Menu ==  '2':
		print('''\n
##############################################
##                                          ##
##  Uma Ferramenta desenvolvida em Python!  ##
##    Para Fins Lucrativos e Didaticos      ##
##                                          ##
##          [-] PythonNux  V2.0 [-]         ##
##                                          ##
##############################################''')
		os.system('setup.py') # Se alterar o nome do arquivo mude-o aqui tb !







