#/usr/bin/python

# Desenvolvido por Koritar
# Koritar + Adriel
# FB Koritar: https://www.facebook.com/joao.koritar
# FB Adriel: http://www.facebook.com/xrn401
#   =>DebutySecTeamSecurity<=
# !Script totalmente LGBT!


#Original
original = '\033[0;0m'
#Vermelho
red = '\033[31m'
#Amarelo
yellow = '\033[33m'
#Roxo com negrito
greyN = '\033[0;37m\033[1m'
#Roxo com negrito
purpleN = '\033[0;35m\033[1m'
#Azul com negrito
blueN = '\033[0;34m\033[1m'


def tools():
	print(yellow+'''
                                   
mmmmmmm               ""#          
   #     mmm    mmm     #     mmm  
   #    #" "#  #" "#    #    #   " 
   #    #   #  #   #    #     """m 
   #    "#m#"  "#m#"    "mm  "mmm" 
                                   
                   
'''+original)

	print('\n'+blueN+' [+] Options [+]')
	print(greyN+'\n  [1] Crawler        [+]')
	print(greyN+'  [2] Decoder Base64 [+]')
	print(greyN+'  [3] Encoder Base64 [+]')
	print(greyN+'  [4] PythoNux       [+]')
#	print(greyN+'  [5] Web Crawler    [+]') #Have bug
	print(greyN+'  [5] Menu           [+]')
	print(greyN+'  [6] Exit    [+]')
	
	
	choices = raw_input(purpleN+'\n [+] Shell >>')
	
	if choices == '1':
		if __name__ == "__main__":
			from Crawler import cra
	

	if choices == '2':
		if __name__ == "__main__":
			from decoder import decoder
	

	if choices == '3':
		if __name__ == "__main__":
			from encoder import encoder
		

	if choices == '4':
		if __name__ == "__main__":
			from PythoNux import setup

#	if choices == '5':
#		if __name__ == "__main__":
#			from WebC import web_crawler

	if choices == '5':
		if __name__ == "__main__":
			import menu

	if choices == '6':
		exit()


print(yellow+'''
                                                                                                                                      
 mmmmm           m    #                   m     m               #     
 #   "# m   m  mm#mm  # mm    mmm   m mm  #  #  #  mmm    m mm  #   m 
 #mmm#" "m m"    #    #"  #  #" "#  #"  # " #"# # #" "#   #"  " # m"  
 #       #m#     #    #   #  #   #  #   #  ## ##" #   #   #     #"#   
 #       "#      "mm  #   #  "#m#"  #   #  #   #  "#m#"   #     #  "m 
         m"                                                           
        ""                                                            
'''+original)


print('\n'+greyN+'[+] Script with some tools [+] ')

print('\n'+blueN+' [+] Options [+]')
print('\n'+purpleN+'  [1] Creditos    [+] ')
print('  [2] Tools       [+]')
print('  [3] Exit        [+]'+original)

chose = raw_input('\n'+blueN+' [+] Shell >> '+red)

#Mostra os creditos
if chose == '1':
	if __name__ == "__main__":
		from credit import credits

if chose == '2':
	tools()
	
if chose == '3':
	exit()
