# 1. Crea una classe chiamata Punto. Questa classe dovrebbe avere:
# Due attributi: x e y, per rappresentare le coordinate del punto nel piano
# Un metodo muovi che prenda in input un valore per dx e un valore per dy e modifichi le
# coordinate del punto di questi valori
# Un metodo distanza_da_origine che restituisca la distanza del punto dall'origine del
# piano.
# DEVE ESSERE RIPETIBILE
""" class Punto:
    def __init__(self):
#Definiamo le coordinate iniziali (stato dell'oggetto)
        self.x = 0
        self.y = 0
    
    def muovi(self):
#Salvo i nuovi valori dentro l'oggetto usando self
        self.x = int(input("Scrivi x: "))
        self.y = int(input("Scrivi y: "))
        
    def mostra_posizione(self):
#Recupero i valori salvati in precedenza - Aggiungere il calcolo della distanza dall'origine
        print(f"Il punto si è mosso a: {self.x}, {self.y}")
            
# Ripeto l'esecuzione
programma = True
while programma:
    punto = Punto()       #Crea l'oggetto punto di classe Punto()
    punto.muovi()         #Richiamo la funzione muovi() per l'oggetto punto
    punto.mostra_posizione() #Richiamo l'oggetto mostra_posizione per l'oggetto punto
#Riprova    
    retry = input("Vuoi riprovare? ")
    if retry != "y":
        programma = False
        print("Uscita in corso...") """

# Crea una classe chiamata Libro. Questa classe dovrebbe avere:
# Tre attributi: titolo, autore e pagine.
# Un metodo descrizione che restituisca una stringa del tipo "Il libro 'titolo è 
# stato scritto da 'autore' e ha 'pagine' pagine"
# DEVE ESSERE RIPETIBILE

class Libro:
    def __init__(self):
        #Inizializzo le variabili
        self.titolo = ""
        self.autore = ""
        self.pagine = 0
    
    def libro(self):
        # Salvo i nuovi valori dentro l'oggetto
        self.titolo = input("Scrivi il titolo: ")
        self.autore = input("Scrivi l'autore: ")
        self.pagine = int(input("Scrivi il numero di pagine: "))
        
    def mostra_informazioni(self):
        #Recupero i valori salvati in precedenza
        print(f"Il titolo del libro è: {self.titolo}")
        print(f"L'autore del libro è: {self.autore}")
        print(f"Il libro ha {self.pagine} pagine")
            
     
# 3. Crea una classe biblioteca che permeta di creare un libro e stamparlo

class Biblioteca:
    def __init__(self):
        self.libri = []
        
    def aggiungi_libro(self, libro_da_aggiungere):
        nuovo_libro = f"{libro_da_aggiungere.titolo} | {libro_da_aggiungere.autore} | {libro_da_aggiungere.pagine}"
        self.libri.append(nuovo_libro)
        
    def mostra_biblioteca(self):
        print(f"Libro | Autore | Pagine")
        for libro in self.libri:
            print(libro)

miaBiblioteca = Biblioteca()
# --- Esecuzione ---
programma = True
while programma:
    nuovo_libro = Libro() #Creo l'oggetto libro di classe Libro()
    nuovo_libro.libro() #Richiamo la funzione libro() per l'oggetto libro
    nuovo_libro.mostra_informazioni() #Richiamo la funzione mostra_informazioni per l'oggetto libro

    miaBiblioteca.aggiungi_libro(nuovo_libro)
    miaBiblioteca.mostra_biblioteca()
#Riprova    
    retry = input("Vuoi riprovare? ")
    if retry != "y":
        programma = False
        print("Uscita in corso...")

#Ex. Andare a gestire nel primo esercizio X punti che sono X oggetti che deve definire tutti e stampare tutti assieme