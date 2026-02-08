# Ex. Sulla base del codice del file "5_Esercizio completo.py" del 05/02/2026
# Andare a far creare inizialmente le collezioni come tuple e poi trasformarle
# in liste solo all'esigenza

import random

programma = True
somma_pari = 0
lista_numeri = set()
lista_dispari = []
numeri_primi = []
totale = 0
totale_primo = True

while programma:
    numero = int(input("Inserisci il numero: "))

    if numero > 0:
        programma = False
        totale += numero
#Stampo i numeri casuali
        while len(lista_numeri) < numero:
            lista_numeri.add(random.randint(1, numero))
#Cerco i numeri dispari
        for c in range(1, numero, 1):
            if c % 2 != 0:
                lista_dispari.append(c)
#Sommo i numeri pari
        if numero % 2 == 0:
            somma_pari += numero
        for c in range(1, numero, 1):
            if c % 2 == 0:
                somma_pari +=c
#Cerco i numeri primi
        for i in range (2, numero):
            if numero % i == 0:
                numeri_primi.append(i)
#Sommo tutti i numeri per capire se il totale è un numero primo
        for c in range(1, numero, 1):
                totale +=c
                for i in range (2, totale):
#Se totale è divisibile per un qualsiasi numero i tra 2 e il totale
                    if totale % i == 0:
#Non è divisibile
                        totale_primo = False
#è divisibile
                    else:
                        totale_primo
        print("Lista numeri: ", lista_numeri)
        print("Lista numeri dispari: ", lista_dispari)
        print("Somma di numeri pari: ", somma_pari)
        print("Numeri primi: ", numeri_primi)
        print("Somma di tutti i numeri: ", totale)
        print(totale_primo)

    else:
        print("ERRORE: Il numero non è positivo")