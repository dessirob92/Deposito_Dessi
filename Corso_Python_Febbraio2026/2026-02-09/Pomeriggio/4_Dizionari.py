# Dizionari
studente = {
#"chiave": valore
    "nome": "Alice",
    "età": 20,
    "sesso": "Femmina"
}

print(studente["nome"])
print(studente["età"])

#Cambio un valore di una chiave già esistente
studente["età"] = 21
print(studente) #Output: {'nome': 'Alice', 'età': 21, 'sesso': 'Femmina'}

#Creo una nuova chiave nel dizionario
studente["città"] = "Roma"
print(studente) #Output: {'nome': 'Alice', 'età': 21, 'sesso': 'Femmina', 'città': 'Roma'}

print(studente.keys()) #Output: dict_keys(['nome', 'età', 'sesso', 'città'])
print(studente.values()) #Output: dict_values(['Alice', 21, 'Femmina', 'Roma'])