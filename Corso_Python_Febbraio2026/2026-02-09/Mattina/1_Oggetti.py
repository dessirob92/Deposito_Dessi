# Classi
#Dichiaro la classe
class Automobile:
#Attributo di classe
    numero_di_ruote = 4
#Metodo costruttore
    def __init__(self, marca, modello): #Il parametro self è obbligatorio
#Attributi di istanza
        self.marca = marca
        self.modello = modello
        
#Metodo di istanza
    def stampa_info(self):
        print("L'automobile è una", self.marca, self.modello)
        
        
#Il costruttore è presente dentro la classe appena viene definita        
class Persona():
    x = 10
    def __init__(self):
        pass
    
class Pippo():
    def __init__(self):
        pass
    
pluto_OBJ = Pippo()    
    
    
roberto_OBJ = Persona()
print(roberto_OBJ.x)

davide_OBJ = Persona()

davide_OBJ.x = 17
print("----------------------")
print(roberto_OBJ.x)
print(davide_OBJ.x)

Persona.x = 20 #x viene ridefinita. Da qui in poi, tutti gli elementi della classe hanno valore 20
veronica_OBJ = Persona()
print(veronica_OBJ.x)


# Tipi base
(print(type(10)))
(print(type(3.14)))
(print(type("test")))
(print(type([1, 2])))

# Tipi personalizzati
class MioOggetto:
    def __init__(self, quantità = 0):
        self.quantità = quantità
#Decide cosa viene stampato quando richiamiamo l'oggetto (TO_STRING)
    def __str__(self):
#Viene richiamato quando facciamo print(istanza_di_Persona)
        return "Ciao Roberto, sono un metodo speciale"
obj = MioOggetto(20)
print(type(obj)) #Il nome della classe definisce il tipo dell'oggetto

print(obj)

class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
    
    def saluta(self):
        print(f"Ciao, mi chiamo {self.nome}")
        
#Creazione di un oggetto Persona
p = Persona("Luca", 25)

p.saluta() #Output: Ciao, mi chiamo Luca


class Calcolatrice:
    @staticmethod
    def somma(a, b):
        return a + b
    
#Uso del metodo statico senza creare un'istanza
risultato = Calcolatrice.somma(5, 3)

print(risultato) #Output: 8

class Contatore:
    numero_istanze = 0 #Attributo di classe
    
    def __init__(self):
        Contatore.numero_istanze += 1
        
    @classmethod
    def mostra_numero_istanze(cls):
        print(f"Sono state create {cls.numero_istanze} istanze")
            
#Creazione di alcune istanze
c1 = Contatore()
c2 = Contatore()

Contatore.mostra_numero_istanze() #Output: Sono state create 2 istanze