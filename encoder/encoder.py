#/usr/bin/python

# Desenvolvido por Koritar
# FB: https://www.facebook.com/joao.koritar
#   =>DebutySecTeamSecurity<=

ciann = '\033[36m\033[1m'

import base64

def base64encodeArquivo():
	print('\n [+]-----------------------[+]')
	string = raw_input("\n [+] Digite a Form: ")
	print("")
	encode = base64.standard_b64encode(string)
	arq = open("hash.txt", "w")
	arq.write(encode)
	arq.close()
	print("\n [!] Criado arquivo com a Hash!")
	print('\n [+]-----------------------[+]')

def base64encodePrint():
	print('\n[+]-----------------------[+]')
	string = raw_input("\n [+] Digite a Form: ")
	print("")
	encode = base64.standard_b64encode(string)
	print("[+] Encoded: "+encode)
	print('\n[+]-----------------------[+]')




def menuloop():
	print('\n'+ciann+'[!] Codificador de base64 [!]'+ciann+'\n')
	chose = raw_input(' [1] Printar cod. na tela [+] \n [2] Escrever no arquivo  [+] \n [3] Exit [+] \n \n [+] Shell >> ') #Mostra as options


	if chose == '1':
		base64encodePrint()

	if chose == '2':
		base64encodeArquivo()
	
	if chose == '3':
		exit()	

num = 0
while num == 0:
	menuloop()
