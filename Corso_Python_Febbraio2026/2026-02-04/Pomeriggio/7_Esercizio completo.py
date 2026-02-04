#Punto 1: Utilizzo di if
#Scrivi un sistema che prende in input un numero e stampa "Pari" se il numero è pari
#   e "Dispari" se il numero è dispari
numero = int(input("Inserisci un numero: "))
#Verifico se il numero è pari
if numero % 2 == 0:
    print("Il numero è pari")
else:
    print("Il numero è dispari")
#Punto 2: Utilizzo di while e range
#Scrivi un sistema che prende in input un numero intero positivo n e stampa tutti i
#   numeri da n a 0 (compreso), decrementando di 1. Deve potersi ripetere all'infinito
numero2 = int(input("Inserisci un numero: "))
#Partendo dal numero inserito, scendo fino a 0
for numero2 in range(numero2, 0, -1):
    print(numero2)

#Punto 3: Utilizzo di for
#Scrivi un sistema che prende in input una lista di numeri e stampa il quadrato di
#   ciascun numero nella lista
#Dichiaro la lista vuota
lista = []
controllore = True
while controllore:
    numero = int(input("Inserisci un numero: ")) #Viene stampato all'infinito
#Popolo la lista
    lista.append(numero)
    esci = input("Vuoi un altro numero? SI - NO ")
    if esci.lower() == "si":
        controllore
    else:
        controllore = False
#Moltiplico ogni numero della lista per sè stesso
for n in lista:
    print(n*n)

#Punto 4: Utilizzo di if, while e for
#Scrivi un sistema che prende in input una lista di numeri interi che precedentemente è stata
#   valorizzata dall'utente.
#Il sistema deve:
#   1. Utilizzare un ciclo for per trovare il numero massimo nella lista 
#   2. Utilizzare un ciclo while per contare quanti numeri sono presenti nella lista
#   3. Utilizzare una condizione if per stampare "Lista vuota" se la lista è vuota,
#       altrimenti stampare il numero massimo trovato e il numero di elementi nella lista
