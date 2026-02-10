# 1. Base: Indovina il numero
#Scrivi un programma che genera un numero casuale tra 1 e 100 (inclusi). L'utente deve
# indovinare quale numero è stato generato. Dopo ogni tentativo, il programma dovrebbe
# dire all'utente se il numero da indovinare è più alto o più basso rispetto al numero
# inserito. Il gioco termina quando l'utente indovina il numero o decide di uscire

import random
#Funzione che genera il numero
def genera_numero(min_val=1, max_val=100):
    return random.randint(min_val, max_val)
#Funzione che chiede se voglio continuare
def vuoi_continuare():
    risposta = input("Vuoi continuare? (si/no) ")
    return risposta.lower() != "no"
#Funzione che fa scrivere il numero in input
def scrivi_numero():
    while True:
            return int(input("Inserisci il numero: "))
#Funzione che confronta il numero inserito con quello generato
def confronta(numero, numero_casuale):
    if numero == numero_casuale:
        print("Hai indovinato!")
        return False
    elif numero > numero_casuale:
        print("Il numero è più basso.")
    else:
        print("Il numero è più alto.")

    return vuoi_continuare()

def main():
    numero_casuale = genera_numero()
    programma = True
    while programma:
        numero = scrivi_numero()
        programma = confronta(numero, numero_casuale)

main()

# 2. Avanzato: Sequenza di Fibonaci fino a N
# Chiedi all'utente di inserire un numero N. Il programma dovrebbe stampare la sequenza
# di Fibonacci fino a N. Ad esempio, se l'utente inserisce 100, il programma dovrebbe
# stampare tutti i numeri della sequenza di Fibonacci minori o uguali a 100

