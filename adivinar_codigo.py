# -*- coding: utf-8 -*-
import random   #módulo aleatorio

print "Bienvenido al juego de MasterMind \n"
print "Consiste en adivinar un código de la cantidad de cifras que quieras \n"
print "El máximo son 10 \n"
print "No te preocupes que tus vidas son ilimitadas \n"

cantidad_de_codigo=input("Escoge de cuántas cifras quieres el código que adivinarás:  ") 
if cantidad_de_codigo==1:
	print "Aaaah que fácil tu código es de una cifra"
else:
	print "\nMuy Bien! Tú código tendrá %s cifras diferentes \n\n"% cantidad_de_codigo
codigo=["0","1","2","3","4","5","6","7","8","9"]
codigo_a_adivinar=""

for num in range(cantidad_de_codigo): #itera en la respuesta del usuario
	codigo_generado= random.choice(codigo) #se genera un numero aleatorio
	while codigo_generado in codigo_a_adivinar: #Evita que se repitan numeros
		codigo_generado=random.choice(codigo)
	codigo_a_adivinar=codigo_a_adivinar + codigo_generado

#print codigo_a_adivinar 



propuesta= raw_input("\nQue código propones?  ")

intentos=1
while propuesta != codigo_a_adivinar and propuesta!="*":
	intentos= intentos+1
	aciertos= 0
	coincidencias=0
	for i in range(cantidad_de_codigo):
		if propuesta[i] == codigo_a_adivinar[i]: #Si en la propuesta del usuario acierta en la posición de algunos números
			aciertos= aciertos+1
		elif propuesta[i] in codigo_a_adivinar: #Si la propuesta del usuario tiene números que coinciden pero no estan en la posición correcta
			coincidencias=coincidencias+1
	print "\nTu código tiene %d aciertos y %d coincidencias"%(aciertos,coincidencias)

	propuesta=raw_input("\nPropón otro código o (* para rendirte)  ")

if propuesta=="*": #Una opción para que el usuario se rinda
	print """\n
       ______  _    _    _      ____   _____ ______ 
\ \   / / __ \| |  | |  | |    / __ \ / ____|  ____|
 \ \_/ / |  | | |  | |  | |   | |  | | (___ | |__   
  \   /| |  | | |  | |  | |   | |  | |\___ \|  __|  
   | | | |__| | |__| |  | |___| |__| |____) | |____ 
   |_|  \____/ \____/   |______\____/|_____/|______|
                                                    """
	print "\nEl código era: %s" % codigo_a_adivinar 
	print "\nSuerte la próxima vez"
else:
	if intentos==1:
		print "\nFelicitaciones ""Adivinaste el código en %d intento"% intentos
		print """\n
__     ______  _    _  __          _______ _   _ 
\ \   / / __ \| |  | | \ \        / /_   _| \ | |
 \ \_/ / |  | | |  | |  \ \  /\  / /  | | |  \| |
  \   /| |  | | |  | |   \ \/  \/ /   | | | . ` |
   | | | |__| | |__| |    \  /\  /   _| |_| |\  |
   |_|  \____/ \____/      \/  \/   |_____|_| \_|
                                                 
                                                 """
	else:
		print """\n
__     ______  _    _  __          _______ _   _ 
\ \   / / __ \| |  | | \ \        / /_   _| \ | |
 \ \_/ / |  | | |  | |  \ \  /\  / /  | | |  \| |
  \   /| |  | | |  | |   \ \/  \/ /   | | | . ` |
   | | | |__| | |__| |    \  /\  /   _| |_| |\  |
   |_|  \____/ \____/      \/  \/   |_____|_| \_|
                                                 
                                                 """

		print "\nAdivinaste el código en %d intentos"% intentos