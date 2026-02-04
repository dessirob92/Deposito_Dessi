# liste
x = 4
y = "pippo"
z = True

lista = [x, y, z]

# lista di numeri
numeri = [1, 2, 3, 4, 5]

# lista di stringhe
nomi = ["Alice", "Bob", "Charlie"]

# lista mista
misto = [1, "due", True], 4.5

# accesso agli elementi di una lista
print(numeri[0]) #Output: 1
print(numeri[2]) #Output: 3

# lista modificabile
numeri = [1, 2, 3, 4, 5]
numeri[2] = 10
print(numeri) #Ouptut:[1, 2, 10, 4, 5]

print(lista[4]) #restituisce un errore --> list index out of range

# metodi delle liste
numeri2 = [3, 1, 4, 2, 5]
print(len(numeri2)) #restituisce la lunghezza della lista. Output: 5
numeri2.append(6) #inserisce l'elemento 6 alla fine della lista
print(numeri2) #Output: [3, 1, 4, 2, 5, 6]
numeri2.insert(2, 10) #inserisce l'elemento 10 nella posizione 2
print(numeri2) #Output: [3, 1, 10, 4, 2, 5, 6]
numeri2.remove(4) #rimuove l'elemento 4 dalla lista
print(numeri2) #Output: [3, 1, 10, 2, 5, 6]
numeri2.sort() #ordina gli elementi della lista
print(numeri2) #Output: [1, 2, 3, 5, 6, 10]

# tuple
punto = (3, 4)
colore_rgb = (255, 218, 0)
informazioni_persona = ("Alice", 25, "Femmina")

print(punto[0]) #Output: 3
print(punto[1]) #Output: 4
punto.insert(2, 10) #restituisce errore --> la tupla non ammette inserimenti

# tupla packing
punto2 = 3, 4
x, y = punto2
print(x, y)

lista3 = list(punto2) #tupla convertita in lista --> si può modificareì

""" #insiemi
set1 = set([1, 2, 3, 4, 5])
set2 = {4, 5, 6, 7, 8}

set3 = {1, 2, 3, 3, 4, 4, 5}
print(set3) #Output: {1, 2, 3, 4, 5}

print(set1.union(set2)) #Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.intersection(set2)) #Output: {4, 5}
print(set1.difference(set2)) #Output: {1, 2, 3}
print(set1.symmetric_difference(set2)) #Output: {1, 2, 3, 6, 7, 8}

print(set1.add(6))
print(set1.discard(6))
print(set1.len())
print(set1.in(9))
print(set1.copy(set2)) """