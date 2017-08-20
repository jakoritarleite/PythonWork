#/usr/bin/python

# Desenvolvido por Koritar
# FB: https://www.facebook.com/joao.koritar
#   =>DebutySecTeamSecurity<=

import base64

#Cores
ciann = '\033[36m\033[1m'


#Tem a function de decodificar e escrever no arquivo
def base64decodeArquivo():	
	print('\n [+]-----------------------[+]')
	string = raw_input("Digite a Form: ") #O cod. em b64 vai aqui
	print("")
	decode = base64.b64decode(string) #Aqui decodifica o cod.
	arq = open("hash.txt", "w") #Abre o arquivo q vai ficar o cod.
	arq.write(str(decode)) #Escreve o cod. no arquivo
	arq.close() #Fecha o arquivo
	print("\n[!] Criado arquivo com a Hash!")
	print('\n [+]-----------------------[+]')

#Decodifica e printa na tela
def base64decodePrint():	
	print('\n [+]-----------------------[+]')
	string = raw_input("\n [+] Digite a Form: ") #O cod. em b64 vai aqui
	print("")
	decode = base64.b64decode(string) #Aqui decodifica o cod.
	print("[+] Encoded: "+decode) #Printa o cod.
	print('\n [+]-----------------------[+]')

def exitall():
	num = 1
	exit()

#Deixar o script em loop
def menuloop():
	print('\n'+ciann+'[!] Decodificador de base64 [!]'+ciann+'\n')
	chose = raw_input(' [1] Printar cod. na tela [+] \n [2] Escrever no arquivo  [+] \n [3] Exit [+] \n \n [+] Shell >> ') #Mostra as options


	if chose == '1':
		base64decodePrint()

	if chose == '2':
		base64decodeArquivo()
	
	if chose == '3':
		exitall()	

num = 0
while num == 0:
	menuloop()
