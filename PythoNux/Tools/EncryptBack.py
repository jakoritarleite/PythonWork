#! /usr/bin/env python
#! coding : utf-8
""" usage :
sudo ./nxcrypt.py --file=file_to_encrypt 
sudo ./nxcrypt.py --file=file_to_encrypt --output=output_file
sudo ./nxcrypt.py --help 
"""

# modules
import sys
import py_compile
import optparse
import os
import commands
import time

_output_ = "backdoor.py" # edit this line is you want edit default output .
_byte_ = (_output_) + "c"

# if platform is linux and NXcrypt isn't launched  as root
if (sys.platform.startswith("linux")) :
	if (commands.getoutput("whoami")) != "root" :
		print ("run it as root")
		sys.exit() #exit
	else:
		pass
else:
    pass
    

#menu     
menu = """
__  ______  _   _ _  _    ___  _
\ \/ /  _ \| \ | | || |  / _ \/ |
 \  /| |_) |  \| | || |_| | | | |
 /  \|  _ <| |\  |__   _| |_| | |
/_/\_\_| \_\_| \_|  |_|  \___/|_|
                                 
Powered by Adriel Freud. - (python backdoor encryption tool)                                      
       """
menu_linux = "\033[32m" + (menu) + "\033[37m"
      
name = """
 -XRN401 e uma ferramenta para bypass in AntVirus
 -Ele encrypta backdoor, payloads em bytecode
 -author: XRN401 (DebutySec)
 -only for penetration testing 
 
	   """
name_linux = "\033[31m" +  (name) + "\033[37m"

#options 
parser = optparse.OptionParser()
print("")
parser.add_option("--arquivo", "-f", help="Arquivo python para encryptar", action="store", dest="file")
parser.add_option("--output", "-o", help="Saida do arquivo crypted python", dest="out", action="store")
print("")
option , arg = parser.parse_args()
if not option.file :
	parser.error("Arquivo para encryptar - Digite -help para pedir ajuda")
	sys.exit()
elif  option.file :
	payload = (option.file)
	
	if not option.out :
		if (sys.platform.startswith("linux")) :
			print (menu_linux)
			print ("")
			print (name_linux)
		else:
			print (menu)
			print ("")
			print (name)
			
		try:
			py_compile.compile(payload, cfile=_byte_, dfile=None, doraise=False, ) #compilation
		except (py_compile.PyCompileError,IOError,TypeError) :
			sys.exit("Error de encryptacao :  file  {} don't exist or it's already crypted ".format(option.file)) #error
		print ("[*] Arquivo : {}".format(option.file))
		print ("[*] default output : {}".format(_output_))
		if (sys.platform.startswith("linux"))  :
			os.system(" mv  {} {} ".format(_byte_,_output_))

		elif (sys.platform.startswith("windows")) :
			os.system(" rename {} {} ".format(_byte_,_output_))
			
		elif (sys.platform.startswith("darwin")):
			os.system(" mv {}  {} ".format(_byte_,_output_))
		print ("[+] encryption finished  100% ")
		print time.strftime('[*] time : %H:%M ',time.localtime()) 
		print time.strftime('[*] date :%d/%m/%y ',time.localtime())
		print ("[+] file : {} ".format(_output_))
	elif option.out  :
		output = option.out
		bytecode = (option.out) + "c"
		if (sys.platform.startswith("linux")) :
			print (menu_linux)
			print ("")
			print (name_linux)
		else:
			print (menu)
			print ("")
			print (name)
		print ("[*] file : {}".format(option.file))
		print ("[*] output : {}".format(output))
		try :
			py_compile.compile(payload, cfile=bytecode, dfile=None, doraise=False, ) #compilation
		except (py_compile.PyCompileError,IOError,TypeError) :
			sys.exit("encryption error : file don't exist or it's already crypted ")
		if (sys.platform.startswith("linux")):
			os.system("mv {}  {} ".format(bytecode,output))
		elif (sys.platform.startswith("windows")):
			os.system("rename {}  {} ".format(bytecode,output))
		elif (sys.platform.startswith("darwin")):
			os.system("mv {}  {} ".format(bytecode,output))	
		print ("[+] encryption finished 100% ")
		print time.strftime('[*] time : %H:%M ',time.localtime()) 
		print time.strftime('[*] date :%d/%m/%y ',time.localtime())
		print ("[*] file : {} ".format(output))	