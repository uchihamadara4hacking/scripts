'''
Exemple SMS in Python with telesign API
learn more in https://www.telesign.com/

Python 3.7
-
by R4MSOLO
'''

from __future__ import print_function
from telesign.messaging import MessagingClient

#Entre no site acima para cadastrar, e altere 'customer_id' e 'api_key' pelo valor informado no site.
#Enter the site above to register, and change 'customer_id' and 'api_key' by the value reported on the site.

customer_id = None
api_key = None

message_type = "MKT"

head = """
 __   __   ___   ___   __  |__        |__  |_|0|_|
(__| |  ' (__/_ (__/_ |  ) |  ) (__(_ |__) |_|_|0|
 __/			   technology®	   |0|0|0|\n"""
 

def sendListnum():
	count = 0
	message = str(input("Texto para enviar: "))
	arq = open('agenda.txt','r')
	numbers = arq.readlines()
	for i in numbers:
		count+=1
		phone_number = i
		messaging = MessagingClient(customer_id, api_key)
		response = messaging.message(phone_number, message, message_type)
	arq.close()
	print("\n[+]",count,"mensagens enviada com sucesso!\n")

def sendNum():
	print("[!]Digite o DDD da sua area junto ao numero\n")
	phone_number = str(input("Numero: "))
	message = str(input("Texto para enviar: "))
	messaging = MessagingClient(customer_id, api_key)
	response = messaging.message(phone_number, message, message_type)
	print("\n[+]Mensagem enviada com sucesso!\n")
	
def main():
	print(head)
	resp = int(input("1- Enviar SMS para um numero\n2- Enviar SMS para uma lista de numeros\n0- Sair\n==>"))
	if resp == 1:
		sendNum()
	elif resp == 2:
		sendListnum()
	elif resp == 0:
		quit()
	else:
		print("[!]Escolha uma das opcoes acima.\n")
		quit()
try:
	if __name__ == __main__:
		main()

except KeyboardInterrupt:
	print("KeyboardInterrupt, bye!\n")
	quit()
