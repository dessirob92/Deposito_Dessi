# Scrivi un programma che chieda all'utente di inserire un numero
# intero positivo n. Il programma deve poi eseguire le seguenti operazioni:
# 1. Utilizzare un ciclo while per garantire che l'utente inserisca un numero
# positivo. Se l'utente inserisce un numero negativo o zero, il programma deve
# continuare a chiedere un numero fino a quando non viene inserito un numero
# positivo.
# 2. Utilizzare un ciclo for con range per calcolare e stampare la somma dei
# numeri pari da 1 a n
# 3. Utilizzare un ciclo for per stampare tutti i numeri dispari da 1 a n
# 4. Utilizzare una struttura if per determinare se n è un numero primo. Un numero
# primo è divisibile solo per 1 e per se stesso. Il programma deve stampare se
# n è primo o no
programma = True
somma = 0
lista_dispari = []
primo = True
while programma:
    numero = int(input("Inserisci il numero: "))
#Controllo se il numero è positivo
    if numero > 0:
        programma = False
        somma += numero
#Sommo i numeri
        for c in range(1, numero, 1):
            somma += c
        print(somma)
#Cerco i numeri dispari
        for c in range(1, numero, 1):
            if c % 2 != 0:
                lista_dispari.append(c)
        print(lista_dispari)
#Controllo se il numero è primo
        for i in range (2, numero):
            if numero % i == 0: #letteralmente indica se numero diviso per i dà resto
                primo
            else:
                primo = False
        print(primo)
    else:
        print("ERRORE: Il numero non è positivo")
        programma