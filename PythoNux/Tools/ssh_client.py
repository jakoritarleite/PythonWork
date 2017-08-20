import paramiko

host = raw_input("Host: ")
user = raw_input("Login: ")
passwd = raw_input("Password: ")

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=user, password=passwd)
while True:
	comando = raw_input("shell>>> ")	
	entrada, saida, erros = client.exec_command(comando)
	print (saida.readlines())
	print (erros.readlines())