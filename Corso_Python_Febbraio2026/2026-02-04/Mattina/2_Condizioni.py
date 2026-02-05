# if
x = 10
y = 20
if(x < y):
    print("OK")
    print("ok")
# else
else:
    print("Else")

# elif
if x < y:
    print("Minore")
elif x==y:
    print("Uguali")
elif x > y:
    print("Maggiore")
else:
    print("Else")
    
# if, else e elif con input
numero = int(input("Inserisci il numero: "))
if numero > y:
    print("OK")
elif numero == y:
    print("Uguale")
else:
    print("NO")
    
parola = "roberto"

if parola.lower == "roberto":
    print("OK")
else:
    print("NO")

# match
comando = input("Inserisci un comando: ")
match comando:
    case "start":
        print("Avvio del programma")
    case "stop":
        print("Chiusura del programma")
    case "pausa":
        print("Programma in pausa")
    case _:
        print("Comando non riconosciuto")