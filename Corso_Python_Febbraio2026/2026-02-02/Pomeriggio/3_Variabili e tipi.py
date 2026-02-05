# print con variabili statiche
nome = "Roberto"
numero = 10
print("Nome:", nome)
print("Numero:", numero)

# input e print
nome = input("Inserisci il nome: ")
età = int(input("Inserisci l'età: "))
print("Mi chiamo", nome, "e ho", età, "anni")

# input con variabili definite
sesso = ""
età = 0

# esso = input("Che sesso sei? ")
età = int(input("Quanti anni hai? "))

print(sesso, età)

# operazioni matematiche
x = 10
y = 2
print(x, "+", y, "=", x + y)
print(x, "-", y, "=", x - y)
print(x, "*", y, "=", x * y)
print(x, "/", y, "=", int(x / y))
print(x, "^", y, "=", x ** y)

x = 1
y = 0.2
print(x, "-", y, "=", x - y)

# stampa valore singolo di una stringa
s = "Roberto"
print(s[0])
print(s[5])
print(s[10])

# concatenazione di stringhe
saluto = "Ciao"
nome = "Roberto"
print(saluto + " " + nome)

# funzioni delle stringhe
s = "Ciao, Roberto"
print(len(s))
print(s.upper())
print(s.lower())
print(s.split(','))
print(s.replace('Roberto', 'Mondo'))

# char
carattere = 'A'

# boolean
booleanT = True
booleanF = False

print(booleanT, booleanF)

x = 5
y = 10
print(x == y)
print(x != y)
print(x < y)
print(x <= y)
print(x >= y)

# operatori logici
x = 5
y = 10
z = 7
print(x < y and y > z) #Output: True
print(x < y or z > y) #Output: True
print(not(x < y)) #Output: False