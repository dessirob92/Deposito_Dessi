# 1.Base / Numero pari e dispari o sequenza
# Scrivi un programma che chiede all'utente di inserire un numero o una stringa
# scegliendo prima quale. Il programma dovrebbe determinare se il numero è pari o
# dispari e stampare il risultato e se deve ripetere o stampare e poi ripetere
programma = True
while programma:
    print("- 1. Numero -")
    print("- 2. Parola -")
    print("-------------")
    operazione = input("Cosa vuoi inserire? ")

    match operazione:
        case "1":
            numero = int(input("Inserisci un numero: "))
#Verifico se il numero è pari
            if numero % 2 == 0:
                print("Il numero è pari")
            else:
                print("Il numero è dispari")
        case "2":
            parola = input("Inserisci la parola: ")
#Verifico se il numero delle lettere è pari
            numero_lettere = 0
            for i in range(len(parola)):
                numero_lettere += 1
            if numero_lettere % 2 == 0:
                print("Il numero di lettere è pari")
            else:
                print("Il numero di lettere è dispari")
        case _:
            print("ERRORE: Operazione non consentita")
            break
#Decido se continuare o uscire        
    ripeti = input("Vuoi ripetere il programma? SI - NO ")
    if ripeti.lower() == "si":
        programma 
    else:
        print("Uscita in corso...")
        break