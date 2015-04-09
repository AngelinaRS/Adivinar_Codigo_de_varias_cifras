import random

tablero = []

for x in range(0,10):
    tablero.append(["O"] * 10)

def print_tablero(tablero):
    for fila in tablero:
        print " ".join(fila)

print "Juguemos batalla naval!"
#print_tablero(tablero)

def fila_aleatoria(tablero):
    return random.randint(0,len(tablero)-1)

def columna_aleatoria(tablero):
    return random.randint(0,len(tablero[0])-1)

barco_fila = fila_aleatoria(tablero)
barco_col = columna_aleatoria(tablero)
print barco_fila
print barco_col

#De aqui en adelante todo deberia ir en tu bucle for!
#Asegurate de indentar!
for turno in range(5):
    print turno+1, "turno"
    
    adivina_fila = input("Adivina fila:")
    adivina_columna = input("Adivina columna:")

    if adivina_fila == barco_fila and adivina_columna == barco_col:
        print "Felicitaciones! Hundiste mi barco!"
        break
    else:

        if (adivina_fila < 0 or adivina_fila > 10) or (adivina_columna < 0 or adivina_columna > 10):
            print "Vaya, esto ni siquiera esta en el oceano."
        elif (tablero[adivina_fila-1][adivina_columna-1] == "X"):
            print "Ya dijiste esa."
        else:
            tablero[adivina_fila-1][adivina_columna-1] = "X"
            print "No impactaste mi barco!"
    if turno == 4:
        print "Termino el juego"
        
  # Muestra (turno + 1) aqui!
    print "te quedan:",  4-turno, "oportunidades"
    print_tablero(tablero)  