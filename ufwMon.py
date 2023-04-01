import itertools
import random
from datetime import datetime, timedelta
import sys
import os
from colorama import init
from termcolor import colored
import time

init()

print(colored("Cargando...", 'yellow'))
time.sleep(1)
os.system('clear')

# opciones del primer menu ----------------------------------------------------------

def on_ufw():
	print(colored("Encendiendo ufw", 'yellow'))
	time.sleep(1)
	os.system('clear')
	os.system('ufw enable')
	time.sleep(1)
	os.system('clear')

def off_ufw():
	print(colored("Apagando ufw", 'yellow'))
	time.sleep(1)
	os.system('clear')
	os.system('ufw disable')
	time.sleep(1)
	os.system('clear')
	
def status_ufw():
	print(colored("Verificando estado del servicio...", 'yellow'))
	time.sleep(1)
	os.system('clear')
	print(colored("El sevicio se encuentra:", 'yellow'))	
	print(colored("------------------------------------------", "blue"))
	os.system('systemctl status ufw')
	print(colored("------------------------------------------", "blue"))
	input(colored("Presione enter para continuar", 'green'))
	os.system('clear')
	On_Off()
	
# opciones del segundo menu -----------------------------------------		

def Permite_salida():
	print(colored("Esto permitira el trafico de salida para los servicios y puertos", 'yellow'))
	print(colored('''------------------------------------------''', 'blue'))
	print(colored("Desea habilitar esta opción?: ", 'yellow'), "[yes or no]")
	respuesta = input(colored("Respuesta: ", 'green'))
	os.system('clear')
	
	if respuesta == "yes":
		print(colored("Permitiendo trafico...", 'yellow'))
		time.sleep(1)
		print(colored('''------------------------------------------''', 'blue'))
		os.system('ufw default allow outgoing')
		time.sleep(1)
		os.system('clear')
		trafico()		
	elif respuesta == "no":
		print(colored("Su respuesta fue: ", 'red'), respuesta)
		time.sleep(2)
		os.system('clear')
		trafico()
		
	else:
		print(colored("Su respuesta fue invalida y no se llevo acabo ninguna acción", 'red'))
		time.sleep(2)
		os.system('clear')
		trafico()
		
def Bloquear_salida():
	print(colored("Esto bloqueara el trafico de salida para los servicios y puertos", 'yellow'))
	print(colored('''------------------------------------------''', 'blue'))
	print(colored("Desea habilitar esta opción?: ", 'yellow'), "[yes or no]")
	respuesta = input(colored("Respuesta: ", 'green'))
	os.system('clear')
	
	if respuesta == "yes":
		print(colored("Bloqueando trafico...", 'yellow'))
		time.sleep(1)
		print(colored('''------------------------------------------''', 'blue'))
		os.system('ufw default deny outgoing')
		time.sleep(1)
		os.system('clear')
		trafico()		
	elif respuesta == "no":
		print(colored("Su respuesta fue: ", 'red'), respuesta)
		time.sleep(2)
		os.system('clear')
		trafico()
		
	else:
		print(colored("Su respuesta fue invalida y no se llevo acabo ninguna acción", 'red'))
		time.sleep(2)
		os.system('clear')
		trafico()

def Permite_entrada():
	print(colored("Esto permitira el trafico de entrada a los servicios y puertos", 'yellow'))
	print(colored('''------------------------------------------''', 'blue'))
	print(colored("Desea habilitar esta opción?: ", 'yellow'), "[yes or no]")
	respuesta = input(colored("Respuesta: ", 'green'))
	os.system('clear')
	
	if respuesta == "yes":
		print(colored("Permitiendo trafico...", 'yellow'))
		time.sleep(1)
		print(colored('''------------------------------------------''', 'blue'))
		os.system('ufw default allow incoming')
		time.sleep(1)
		os.system('clear')
		trafico()		
	elif respuesta == "no":
		print(colored("Su respuesta fue: ", 'red'), respuesta)
		time.sleep(2)
		os.system('clear')
		trafico()
		
	else:
		print(colored("Su respuesta fue invalida y no se llevo acabo ninguna acción", 'red'))
		time.sleep(2)
		os.system('clear')
		trafico()

def Bloquear_entrada():
	print(colored("Esto bloqueara el trafico de entrada a los servicios y puertos", 'yellow'))
	print(colored('''------------------------------------------''', 'blue'))
	print(colored("Desea habilitar esta opción?: ", 'yellow'), "[yes or no]")
	respuesta = input(colored("Respuesta: ", 'green'))
	os.system('clear')
	
	if respuesta == "yes":
		print(colored("Bloqueando trafico...", 'yellow'))
		time.sleep(1)
		print(colored('''------------------------------------------''', 'blue'))
		os.system('ufw default allow incoming')
		time.sleep(1)
		os.system('clear')
		trafico()		
	elif respuesta == "no":
		print(colored("Su respuesta fue: ", 'red'), respuesta)
		time.sleep(2)
		os.system('clear')
		trafico()
		
	else:
		print(colored("Su respuesta fue invalida y no se llevo acabo ninguna acción", 'red'))
		time.sleep(2)
		os.system('clear')
		trafico()
		
# opciones del menu de restricciones -----------------------------------------	

def permitir_tra():
	print(colored("Esto permitira el tráfico de un puerto en espesifico", 'yellow'))
	print(colored("Ingrese un puerto.", 'yellow'))
	print(colored("Ejemplo", 'yellow'), "80/tcp or 80/udp")
	print(colored('''------------------------------------------''', 'blue'))
	puerto = input(colored("Su puerto es: ", 'green'))
	os.system('clear')
	print(colored("Su puerto es: ", 'yellow') + puerto)
	print(colored("[yes or no]", 'yellow'))
	print(colored('''------------------------------------------''', 'blue'))
	respuesta = input(colored("Respuesta: ", 'green'))
	os.system('clear')
	
	if respuesta == "yes":
		print(colored("Cargando puerto...", 'yellow'))
		time.sleep(1)
		print(colored('''------------------------------------------''', 'blue'))
		os.system('ufw allow ' + puerto)
		time.sleep(2)
		os.system('clear')
		restricciones()
	elif respuesta == "no":
		print(colored("Su respuesta fue: ", 'red') + respuesta)
		time.sleep(1)
		os.system('clear')
		restricciones()
	else:
		print(colored("Su respuesta es invalida y no se llevo acabo ninguna acción"))
		time.sleep(2)
		os.system('clear')
		restricciones()
		
def bloquear_tra():
	print(colored("Esto bloqueara el tráfico de un puerto en espesifico", 'yellow'))
	print(colored("Ingrese un puerto.", 'yellow'))
	print(colored("Ejemplo", 'yellow'), "80/tcp or 80/udp")
	print(colored('''------------------------------------------''', 'blue'))
	puerto = input(colored("Su puerto es: ", 'green'))
	os.system('clear')
	print(colored("Su puerto es: ", 'yellow') + puerto)
	print(colored("[yes or no]", 'yellow'))
	print(colored('''------------------------------------------''', 'blue'))
	respuesta = input(colored("Respuesta: ", 'green'))
	os.system('clear')
	
	if respuesta == "yes":
		print(colored("Cargando puerto...", 'yellow'))
		time.sleep(1)
		print(colored('''------------------------------------------''', 'blue'))
		os.system('ufw deny ' + puerto)
		time.sleep(2)
		os.system('clear')
		restricciones()
	elif respuesta == "no":
		print(colored("Su respuesta fue: ", 'red') + respuesta)
		time.sleep(1)
		os.system('clear')
		restricciones()
	else:
		print(colored("Su respuesta es invalida y no se llevo acabo ninguna acción", 'red'))
		time.sleep(2)
		os.system('clear')
		restricciones()
		
def denegar_ip():
	print(colored("Esto bloqueara el acceso/tráfico de una IP", 'yellow'))
	print(colored("Ingrese una IP.", 'yellow'))
	print(colored("Ejemplo", 'yellow'), "192.168.1.20")
	print(colored('''------------------------------------------''', 'blue'))
	IP = input(colored("La IP es?: "))
	os.system('clear')
	print(colored("La IP ingresada es: ", 'yellow') + IP)
	print(colored("[yes or no]", 'yellow'))
	print(colored('''------------------------------------------''', 'blue'))
	respuesta = input(colored("Respuesta: ", 'green'))
	os.system('clear')
	
	if respuesta == "yes":
		print(colored("Restringiendo IP...", 'yellow'))
		time.sleep(1)
		print(colored('''------------------------------------------''', 'blue'))
		os.system('ufw deny from ' + IP)
		time.sleep(2)
		os.system('clear')
		restricciones()
	elif respuesta == "no":
		print(colored("Su respuesta fue: ", 'red') + respuesta)
		time.sleep(1)
		os.system('clear')
		restricciones()
	else:
		print(colored("Su respuesta es invalida y no se llevo acabo ninguna acción", 'red'))
		time.sleep(2)
		os.system('clear')
		restricciones()

def permitir_ip():
	print(colored("Esto permitira el acceso/tráfico de una IP", 'yellow'))
	print(colored("Ingrese una IP.", 'yellow'))
	print(colored("Ejemplo", 'yellow'), "192.168.1.20")
	print(colored('''------------------------------------------''', 'blue'))
	IP = input(colored("La IP es?: "))
	os.system('clear')
	print(colored("Ingrese un puerto.", 'yellow'))
	print(colored("Ejemplo:", 'yellow'), "22")
	print(colored('''------------------------------------------''', 'blue'))
	puerto = input(colored("El puerto es?: ", 'green'))
	os.system('clear')
	print(colored("La IP ingresada es: ", 'yellow') + IP)
	print(colored("El puerto ingresado es: ", 'yellow') + puerto)
	print(colored("[yes or no]", 'yellow'))
	print(colored('''------------------------------------------''', 'blue'))
	respuesta = input(colored("Respuesta: ", 'green'))
	os.system('clear')
	
	if respuesta == "yes":
		print(colored("Restringiendo IP...", 'yellow'))
		time.sleep(1)
		print(colored('''------------------------------------------''', 'blue'))
		os.system('ufw allow from ' + IP + ' to any port ' + puerto)
		time.sleep(2)
		os.system('clear')
		restricciones()
	elif respuesta == "no":
		print(colored("Su respuesta fue: ", 'red') + respuesta)
		time.sleep(1)
		os.system('clear')
		restricciones()
	else:
		print(colored("Su respuesta es invalida y no se llevo acabo ninguna acción", 'red'))
		time.sleep(2)
		os.system('clear')
		restricciones()
	
# Menus ------------------------------------------------------------

def restricciones():
	while True:
		print(colored("Menu de restricciones", 'yellow'))
		print("Se recomienda que apagues ufw antes de aplicar cualquier cambio")
		print(colored('''------------------------------------------''', 'blue'))
		print(colored("[1]", 'yellow'), "Permitir tráfico de entrada a un puerto")
		print(colored("[2]", 'yellow'), "Bloquear tráfico de entrada a un puerto")
		print(colored('''------------------------------------------''', 'blue'))
		print(colored("[3]", 'yellow'), "Denegar acceso/tŕafico a una IP")
		print(colored("[4]", 'yellow'), "Permitir acceso/tráfico a una IP")
		print(colored('''--------------------''', 'yellow'))
		print(colored("[c]", 'magenta'), "Limpiar consola")
		print(colored("[r]", 'magenta'), "Regresar")
		print(colored("[0]", 'magenta'), "Salir")
		print(colored('''------------------------------------------''', 'blue'))
		opcion = input(colored("Selecciona una opción: ", 'green'))
		os.system('clear')
		
		if opcion == "1":
			permitir_tra()
		elif opcion == "2":
			bloquear_tra()
		elif opcion == "3":
			denegar_ip()
		elif opcion == "4":
			permitir_ip()
		elif opcion == "c":
			os.system('clear')
		elif opcion == "r":
			menu()
		elif opcion == "0":
			os.system('clear')
			print(colored("Saliendo", 'yellow'))
			time.sleep(1)
			os.system('clear')
			sys.exit()
		else:
			print(colored("Opción invalida", 'red'))
			time.sleep(1)
			os.system('clear')	
		


def trafico():
	while True:
		print(colored("Menu de tráfico", 'yellow'))
		print("Se recomienda que apagues ufw antes de aplicar cualquier cambio")
		print(colored('''------------------------------------------''', 'blue'))
		print(colored("[1]", 'yellow'), "Permitir tráfico de salida")
		print(colored("[2]", 'yellow'), "Bloquear tráfico de salida")
		print(colored('''------------------------------------------''', 'blue'))
		print(colored("[3]", 'yellow'), "Permitir tráfico de entrada")
		print(colored("[4]", 'yellow'), "Bloquear trafico de entrada")		
		print(colored('''--------------------''', 'yellow'))
		print(colored("[c]", 'magenta'), "Limpiar consola")
		print(colored("[r]", 'magenta'), "Regresar")
		print(colored("[0]", 'magenta'), "Salir")
		print(colored('''------------------------------------------''', 'blue'))
		opcion = input(colored("Selecciona una opción: ", 'green'))
		os.system('clear')
		
		if opcion == "1":
			Permite_salida()
		elif opcion == "2":
			Bloquear_salida()
		elif opcion == "3":
			Permite_entrada()
		elif opcion == "4":
			Bloquear_entrada()
		elif opcion == "c":
			os.system('clear')
		elif opcion == "r":
			menu()
		elif opcion == "0":
			print(colored("Saliendo...", 'yellow'))
			time.sleep(1)
			os.system('clear')
			sys.exit()
			
		else:
			print(colored("Opción invalida", 'red'))
			time.sleep(1)
			os.system('clear')



def On_Off():
	while True:
		print(colored("Menu de opciones de encendido", 'yellow'))
		print(colored("------------------------------------------", "blue"))
		print(colored("[1]", 'yellow'), "Encender")
		print(colored("[2]", 'yellow'), "Apagar")
		print(colored("[3]", 'yellow'), "Verificar estado")	
		print(colored('''--------------------''', 'yellow'))
		print(colored("[c]", 'magenta'), "Limpiar consola")
		print(colored("[r]", 'magenta'), "Regresar")
		print(colored("[0]", 'magenta'), "Salir")
		print(colored("------------------------------------------", "blue"))
		opcion = input(colored("Selecciona una opción: ", 'green'))
		os.system('clear')
		
		if opcion == "1":
			on_ufw()
		elif opcion == "2":
			off_ufw()
		elif opcion == "3":
			status_ufw()
		elif opcion == "c":
			os.system('clear')
		elif opcion == "r":
			menu()
		elif opcion == "0":
			os.system('clear')
			print(colored("Saliendo", 'yellow'))
			time.sleep(1)
			os.system('clear')
			sys.exit()
		else:
			print(colored("Opción invalida", 'red'))
			time.sleep(1)
			os.system('clear')			


def menu():
	while True:
		print(colored('''
        __          __  __             
 _   _ / _|_      _|  \/  | ___  _ __  
| | | | |_\ \ /\ / / |\/| |/ _ \| '_ \ 
| |_| |  _|\ V  V /| |  | | (_) | | | |
 \__,_|_|   \_/\_/ |_|  |_|\___/|_| |_|
	''', 'cyan'))
		print(colored("		By Cañas" ,'yellow'))
		print(colored("			Version - 1", 'yellow'))
		print(colored('''------------------------------------------''', 'blue'))
		print(colored("[1]", 'yellow'), "Opciones de encendido")
		print(colored("[2]", 'yellow'), "Configurar tráfico")
		print(colored("[3]", 'yellow'), "Configurar restricciones")
		print(colored("[4]", 'yellow'), "Verificar status de configuraciones")
		print(colored('''--------------------''', 'yellow'))
		print(colored("[c]", 'magenta'), "Limpiar consola")
		print(colored("[0]", 'magenta'), "Salir")
		print(colored('''------------------------------------------''', 'blue'))
		opcion = input(colored("Selecciona una opción: ", 'green'))
		os.system('clear')
		
		if opcion == "1":
			On_Off()
		elif opcion == "2":
			trafico()
		elif opcion == "3":
			restricciones()
		elif opcion == "4":
			os.system('ufw status')
			print(colored('''------------------------------------------''', 'blue'))
			input("Presione enter para regresar: ")
			os.system('clear')
			menu()
		elif opcion == "c":
			os.system('clear')
		elif opcion == "0":
			print(colored("Saliendo...", 'yellow'))
			time.sleep(1)
			os.system('clear')
			sys.exit()
			
		else:
			print(colored("Opción invalida", 'red'))
			time.sleep(1)
			os.system('clear')
		
		
if __name__ == '__main__':
    menu()	
	
