# while
conteggio = 0
while conteggio < 5:
    print(conteggio) #Output: 0, 1, 2, 3, 4
    conteggio += 1
    
conteggio2 = 0
while conteggio2 < 5:
    conteggio2 += 1
    print(conteggio2) #Output: 1, 2, 3, 4, 5
    
# ciclo booleano controllato
controllore = True
while controllore:
    print("oh no") #Viene stampato all'infinito
    
    esci = input("Vuoi uscire? SI - NO ")
    if esci.lower() == "si":
        controllore = False
        print("Stai uscendo...")
        print("FINE")
    else:
        controllore
else:
    print("While 1 - Il controllore era false")
        
# for
numeri = [1, 2, 3, 4, 5]
for numero in numeri:
    print(numero)
    
stringa = "roberto"
for lettera in stringa:
    print(lettera)
    
# range()
for c in range(1, 21, 2):
    print(c) #Stampa delle sequenze di valori
    
# break
numeri = [1, 2, 3, 4, 5]
for numero in numeri:
    if numero == 3:
        break
    print(numero)
    
# continue
numeri = [1, 2, 3, 4, 5]
for numero in numeri:
    if numero == 3:
        continue
    print(numero)
    
# pass
for i in range(5):
    if i == 3:
        pass
    print(i)
    
# splat
numeri = [*range(1, 11)]
print(numeri) #Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]