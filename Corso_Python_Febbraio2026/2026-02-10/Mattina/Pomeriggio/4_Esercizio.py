# Lo scopo di questo esercizio è creare un sistema di gestione per una fabbrica che
# produce e vende vari tipi di prodotti. Gli studenti dovranno creare una classe base
# chiamata Prodotto e diverse classi parallele che rappresentano diversi tipi di
# prodotti. Inoltre, dovranno creare una classe Fabbrica che gestisce l'inventario
# e le vendite dei prodotti.
# 
# 1.Classe Prodotto:
# - Attributi:
#   - nome (stringa che descrive il nome del prodotto) 
#   - costo_produzione (costo per produrre il prodotto)
#   - prezzo_vendita (prezzo a cui il prodotto viene venduto al pubblico)
# - Metodi:
#   - calcola_profitto --> Restituisce la differenza tra il prezzo di vendita e il
#   costo di produzione
# 
# 2.Classi parallele:
# - Creare almeno due classi parallele a Prodotto, per esempio Elettronica e
# Abbigliamento
# - Aggiungere attributi specifici per ciascun tipo di prodotto, come materiale per
# Abbigliamento e garanzia per Elettronica
# 
# 3.Classe Fabbrica:
# - Attributi:
#   - inventario --> un dizionario che tiene traccia del numero di ogni tipo di 
#   prodotto in magazzino
# -Metodi:
#   - aggiungi_prodotto --> aggiunge prodotti all'inventario
#   - vendi_prodotto --> diminuisce la quantità di un prodotto in inventario e stampa
#   il profitto realizzato dalla vendita
#   - resi_prodotto --> aumenta la quantità di un prodotto restituito in inventario

# 1. CLASSE BASE
class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
    
    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione

# 2. CLASSI PARALLELE (Sottoclassi)

class Elettronica(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia):
# Recupero i parametri della classe padre Prodotto
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.garanzia = garanzia

class Abbigliamento(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.materiale = materiale

# 3. CLASSE FABBRICA
class Fabbrica:
    def __init__(self):
# Definisco il dizionario inventario (specifico per la classe Fabbrica)
        self.inventario = {}

#Aggiungo un prodotto
    def aggiungi_prodotto(self, prodotto, quantita):
        nome = prodotto.nome
        if nome in self.inventario:
            self.inventario[nome]['quantita'] += quantita
        else:
            # Salviamo l'oggetto e la sua quantità
            self.inventario[nome] = {'oggetto': prodotto, 'quantita': quantita}
        print(f"Aggiunti {quantita} pezzi di {nome}.")

#Vendo un prodotto
    def vendi_prodotto(self, nome_prodotto, quantita):
        if nome_prodotto in self.inventario:
            info = self.inventario[nome_prodotto]
            if info['quantita'] >= quantita:
                # Calcolo profitto usando il metodo della classe Prodotto
                profitto_unitario = info['oggetto'].calcola_profitto()
                profitto_totale = profitto_unitario * quantita
                
                # Aggiornamento magazzino
                info['quantita'] -= quantita
                print(f"Venduto {nome_prodotto}! Profitto realizzato: {profitto_totale}€")
                
                # Avvisi scorte (come avevi fatto tu, molto utile!)
                if info['quantita'] == 0:
                    print("ATTENZIONE: Esaurito!")
            else:
                print("Errore: Quantità insufficiente!")
        else:
            print("Errore: Prodotto non trovato.")

#Calcolo la resa di un prodotto
    def resi_prodotto(self, nome_prodotto, quantita):
        if nome_prodotto in self.inventario:
            self.inventario[nome_prodotto]['quantita'] += quantita
            print(f"Reso effettuato: {quantita} pezzi di {nome_prodotto} tornati in magazzino.")
        else:
            print("Errore: Il prodotto reso non appartiene al catalogo.")

#Creo un'istanza della classe Fabbrica
mia_fabbrica = Fabbrica()

#Creo un'istanza della sottoclasse Elettronica
telefono = Elettronica("Smartphone", 200, 500, "24 mesi")
#Creo un'istanza della sottoclasse Abbigliamento
maglia = Abbigliamento("T-Shirt", 5, 20, "Cotone")

#Richiamo la funzione della classe Fabbrica per aggiungere prodotti nell'inventario
mia_fabbrica.aggiungi_prodotto(telefono, 10)
mia_fabbrica.aggiungi_prodotto(maglia, 50)

#Richiamo la funzione della classe Fabbrica per vendere i prodotti e calcolare il profitto
mia_fabbrica.vendi_prodotto("Smartphone", 2) # Profitto: (500-200) * 2 = 600

#Richiamo la funzione della classe Fabbrica per calcolare la resa di un prodotto
mia_fabbrica.resi_prodotto("Smartphone", 1)