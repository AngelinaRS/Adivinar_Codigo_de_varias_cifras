# -*- coding: utf-8 -*-
import random   #módulo aleatorio

print "Bienvenido al juego de MasterMind \n"
print "Consiste en adivinar un código de la cantidad de cifras que quieras \n"
print "El máximo son 7 \n"
print "No te preocupes que tus vidas son ilimitadas"

cantidad_de_codigo=input("Escoge de cuántas cifras quieres el código que adivinarás: \n\n")
print "Muy Bien! Tú código tendrá %s cifras diferentes \n\n"% cantidad_de_codigo
codigo=["0","1","2","3","4","5","6","7","8","9"]
codigo_a_adivinar=""

for num in range(cantidad_de_codigo):
	codigo_generado= random.choice(codigo)
	while codigo_generado in codigo_a_adivinar:
		codigo_generado=random.choice(codigo)
	codigo_a_adivinar=codigo_a_adivinar+ codigo_generado
print codigo_a_adivinar



propuesta= raw_input("Que codigo propones?  ")

intentos=1
while propuesta != codigo_a_adivinar and propuesta!="*":
	intentos= intentos+1
	aciertos= 0
	coincidencias=0
	for i in range(cantidad_de_codigo):
		if propuesta[i] == codigo_a_adivinar[i]:
			aciertos= aciertos+1
		elif propuesta[i] in codigo_a_adivinar:
			coincidencias=coincidencias+1
	print "Tu codigo tiene %d aciertos y %d coincidencias"%(aciertos,coincidencias)

	propuesta=raw_input("Propon otro codigo:  ")

if propuesta=="*":
	print "El codigo era %s" % codigo_a_adivinar 
	print "Suerte la proxima vez"
else:
	if intentos==1:
		print "Felicitaciones adivinaste el codigo en %d intento"% intentos
	else:
		print "Felicitaciones adivinaste el codigo en %d intentos"% intentos
