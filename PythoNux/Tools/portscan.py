#!Developed by AdrielFreud
#!Email : usuariocargo2016@gmail.com

from socket import * 
import os

if os.name == 'nt':
	os.system('cls')
else:
	os.system('clear')


print ('''
*******************************************
********** Simples PortScanning ***********
*******************************************
''')

if __name__ == '__main__':
    targetserver = raw_input('Digite o IP para o  scan: ')
    targetIP = gethostbyname(targetserver)
    print ("\nPronto para o scan :3 ")
    print("")
    # Range para contagem de portas!
    for i in range(1, 1025):
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(0.05)

        result = s.connect_ex((targetIP, i))

        if(result == 0) :
            print ('Port %d: OPEN' % (i,))
        s.close()

print ("\n[+] Scanning finished!")
