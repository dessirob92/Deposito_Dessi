# Genera un programma che chiede all'utente di inserire un numero intero positivo.
# Usa un ciclo for per stampare tutti i numeri da 1 fino al numero inserito.
# Per ogni numero:
# 1. Stampa "pari" se il numero è pari
# 2. Stampa "dispari" se il numero è dispari

programma = True
while programma:
    numero = int(input("Inserisci il numero: "))
    if numero > 0:
        programma = False
#Cerco tutti i numeri da 1 al numero inserito
    for c in range(1, numero, 1):
#Se il numero è pari stampo che è pari
            if c % 2 == 0:
                print(c , " - Il numero è pari")
#Se il numero è dispari stampo che è dispari
            else:
                print(c , " - Il numero è dispari")
    else:
        print("ERRORE: Il numero non è positivo") #Da verificare perchè viene ugualmente printato dopo l'output
        programma