# Definizione della funzione
def saluta():
    print("Ciao! Questa è una funzione semplice.")

# Chiamata della funzione
saluta()


def saluta_persona(nome: str, messaggio = "Ciao"):
    print(f"{messaggio} {nome}!")

saluta_persona("Mario")
saluta_persona("Anna")


def stampaSingola_lista(listaX: list):
    print("Benvenuto nella funzione")
    for i in listaX:
        print(i)
    print("Fine")


lista = list(range(0, 20, 2))
stampaSingola_lista(lista)

lista2 = list(range(1, 20, 2))
stampaSingola_lista(lista2)


# Return
def ricalcoloValore(x: int):
    return x * 7

numero_finale = ricalcoloValore(10)

print(numero_finale)
print(ricalcoloValore(5))
print(ricalcoloValore(3))   # <-- chiamata corretta (prima mancavano le parentesi)


def quadrato(numero: int):
    return numero * numero

risultato = quadrato(4)
print(risultato)


def divisione(a: int, b: int):
    if b == 0:
        print("Errore: divisione per zero!")
        return None
    return a / b

x = divisione(27, 3)
print(x)
