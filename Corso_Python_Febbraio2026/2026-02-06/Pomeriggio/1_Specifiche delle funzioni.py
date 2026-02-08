# Funzioni generatori
def fibonacci(n):
#Definisce la logica centrale della funzione
    a, b = 0, 1
   
    while a < n:
        yield a
        a, b = b, a + b

#Inizio il programma
while True:
    numero = int(input("Scrivi un numero: "))

    print("Sequenza di Fibonacci:")
#Richiamo la funzione "fibonacci" per il numero inserito
    print(*fibonacci(numero), sep = "\n")

    risposta = input("Vuoi inserire un altro numero? (s/n): ").lower()

    if risposta == "n":
        print("Ciao! 👋")
        break

#Provare a implementare una funzione che genera 3 numeri casuali. 
#Per ognuno di essi, richiamare la funzione "fibonacci"


def contatore_fino_a(n):
    i = 1
    while i <= n:
        yield i
        i +=1
        
print(int(contatore_fino_a(10)))

# Catena di generatori
def catena_generatori():
#Prima produce 1..3, poi 10..12
    yield from range(1, 4)
    yield from range (10, 13)
    
print(list(catena_generatori()))

# Decoratori
def decoratore(funzione):
    def wrapper():
        print("Prima dell'esecuzione dellla funzione")
        funzione()
        print("Dopo l'esecuzione della funzione")
    return wrapper
#Richiamo il decoratore e lo modifica temporaneamente
@decoratore
#Ridefinisco il decoratore
def saluta():
    print("Ciao!")
    
saluta()


def decoratore_con_argomenti(funzione):
#Definisco gli argomenti
    def wrapper(*args, **kwargs):
        print("Prima")
        risultato = funzione(*args, **kwargs)
        print("Dopo")
        return risultato
    return wrapper

@decoratore_con_argomenti
def somma(a, b):
    print(a + b)
    return a + b

print("Il risultato è: ", somma(3, 4))

# Esempio 1
#Decoratore che prende una funzione come input
def logger(funzione):
#Wrapper che esegue del codice prima e dopo la chiamata alla funzione originale. In questo caso, il wrapper stampa gli argomenti e il risultato della funzione decorata
    def wrapper(*args, **kwargs):
        print(f"Chiamata a {funzione.__name__} con argomenti: {args} e {kwargs}")
        risultato = funzione(*args, **kwargs)
        print(f"Risultato di {funzione.__name__}: {risultato}")
        return risultato
        return wrapper
#@logger Applica il decoratore logger alla funzione "moltiplica" --> Ogni volta che chiamiamo "moltiplica", verrà prima eseguito il codice del wrapper
@logger
def moltiplica(a, b):
    return a * b

# Chiamata alla funzione decorata
print(moltiplica(3, 4))


# Esempio 2
import time

def calcola_tempo(funzione):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        risultato = funzione(*args, **kwargs)
        end_time = time.time()
        print(f"Tempo di esecuzione: {end_time - start_time} secondi")
        return risultato
    return wrapper

@calcola_tempo
def calcolo_lento():
    time.sleep(2)
    print("Calcolo completato")
    
#Chiamata alla funzione decorata
calcolo_lento()