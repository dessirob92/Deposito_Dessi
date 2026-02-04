#Esercizio 1: Chiedi all'utente di inserire un numero. Il programma dovrebbe quindi fare un conto alla rovescia a partire da quel numero fino a zero, stampando ogni numero e chiederti se vuoi ripetere o no
continua = True
while continua:
    numero = int(input("Inserisci un numero: "))
    #conto alla rovescia fino allo 0
    for i in range (numero, -1, -1):
        print(i)
    #ciclo booleano per uscire o ripetere il programma
        esci = input("Vuoi ripetere il programma? SI - NO ")
        if esci.lower() == "si":
            continua 
        elif esci.lower() == "no":
            continua = False
            print("Stai uscendo...")
            print("FINE")

#Esercizio 2: Chiedi all'utente di inserire un numero. Il programma dovrebbe controllare se il numero è primo / pari o no. Se è primo, lo salva e stampa "Il numero è primo". Altrimenti, stampa "Il numero non è primo." Si ferma il tutto quando ha 5 numeri primi
primi = []

while len(primi) < 5:
    numero = int(input("Inserisci un numero: "))

    if numero < 2:
        print("Il numero non è primo.")
        continue

    primo = True

    # controllo divisori con FOR
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break

    if primo:
        print("Il numero è primo")
        primi.append(numero)
    else:
        print("Il numero non è primo.")

print("Numeri primi trovati:", primi)