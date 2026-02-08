# Esercizio 4: Scrivi un programma che chieda all'utente la sua età. Se l'età è inferiore a 18 annni, il programma dovrebbe stampare "Mi dispiace, non puoi vedere questo film". Altrimenti, dovrebbe stampare "Puoi vedere questo film"
età = int(input("Quanti anni hai?"))

match età:
    case età if età >= 18:
        print("Puoi vedere questo film")
    case _:
        print("Mi dispiace, non puoi vedere questo film")

# Esercizio 5: Scrivi un programma che chieda all'utente di inserire due numeri e un'operazione da eseguire tra addizione, sottrazione, moltiplicazione e divisione. Il programma dovrebbe poi eseguire l'operazione e stampare il risultato. Tuttavia, se l'utente tenta di dividere per zero, il programma dovrebbe stampare "Errore: Divisione per zero". Se l'operazione inserita non viene riconosciuta, il programma dovrebbe stampare "Operazione non valida"
print("--- 1. Addizione")
print("--- 2. Sottrazione")
print("--- 3. Moltiplicazione")
print("--- 4. Divisione")
print("----------------------")
x = float(input("Inserisci il primo numero: "))
y = float(input("Inserisci il secondo numero: "))
operazione = input("Che operazione vuoi eseguire? ")

match operazione:
    case "1":
        print (x + y)
    case "2":
        print (x - y)
    case "3":
        print (x * y)
    case "4":
        if y != 0:
            print (x / y)
        else:
            print("ERRORE: non posso dividere un numero per 0")
    case _:
        print("Operazione non valida")