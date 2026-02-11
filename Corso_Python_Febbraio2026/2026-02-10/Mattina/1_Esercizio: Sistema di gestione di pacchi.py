# Scrivi un programa in Python che simuli un gestore di pacchi utilizzando più classi;
# sono ammessi solo classi, oggetti, funzioni, metodi e al massimo liste o dizionari
# 
# Il sistema deve includere una classe Pacco con: codice (stringa), peso (numero) e
# stato (es. "in magazzino", "in consegna", "consegnato"), con un metodo per mostrare
# le info e un metodo per cambiare stato.
# 
# Deve esserci una classe Magazzino che contiene una lista (o dizionario) di pacchi
# e permette di aggiungere un pacco, cercarlo per codice e mostrare tutti i pacchi
# in un certo stato.
# 
# Deve esserci, infine, una classe GestorePacchi che usa il magazzino per mettere un
# pacco "in consegna", segnare un pacco come "consegnato" e calcolare il peso totale
# dei pacchi ancora non consegnati.
# 
# Nel programma principale crea almeno 5 pacchi, inseriscili nel magazzino, cambia lo
# stato di alcuni pacchi (almeno una consegna avviata e una consegna completata) e 
# stampa: elenco pacchi "in magazzino", elenco pacchi "in consegna" e il peso totale
# dei pacchi non ancora consegnati.

class Pacco:
    def __init__(self, codice_univoco, peso, stato="in magazzino"):
        self.codice_univoco = codice_univoco
        self.peso = peso
        self.stato = stato

    def aggiorna_stato(self, nuovo_stato):
        self.stato = nuovo_stato
    
    def mostra_info(self):
        print(f"ID: {self.codice_univoco} | Peso: {self.peso}kg | Stato: {self.stato}")

class Magazzino:
    def __init__(self):
        self.lista_pacchi = []

    def aggiungi_pacco(self, pacco):
        self.lista_pacchi.append(pacco)
        print(f"Pacco {pacco.codice_univoco} aggiunto con successo.")

    def cerca_pacco(self, codice):
        for p in self.lista_pacchi:
            if p.codice_univoco == codice:
                return p
        return None

    def mostra_per_stato(self, stato_cercato):
        print(f"Pacchi in stato: {stato_cercato} ---")
        trovati = [p for p in self.lista_pacchi if p.stato == stato_cercato]
        if trovati:
            for p in trovati: p.mostra_info()
        else:
            print(f"Nessun pacco in stato '{stato_cercato}' trovato.")

class GestorePacchi:
    def __init__(self, magazzino):
        self.magazzino = magazzino

    def modifica_stato(self, codice, nuovo_stato):
        pacco = self.magazzino.cerca_pacco(codice)
        if pacco:
            pacco.aggiorna_stato(nuovo_stato)
            print(f"OK: Stato del pacco {codice} aggiornato.")
        else:
            print(f"ERRORE: Pacco {codice} non trovato.")

    def calcola_peso_totale(self):
        # Somma il peso di tutti i pacchi il cui stato NON è "consegnato"
        return sum(p.peso for p in self.magazzino.lista_pacchi if p.stato != "consegnato")

# --- INTERFACCIA UTENTE (MAIN) ---
magazzino = Magazzino()
gestore = GestorePacchi(magazzino)

print("=== GESTORE PACCHI ===")

while True:
    print("1. Registra nuovo pacco")
    print("2. Mostra pacchi per stato")
    print("3. Aggiorna stato (Consegna/Consegnato)")
    print("4. Visualizza peso totale da consegnare")
    print("0. Esci")
    
    scelta = input("Seleziona operazione: ")

    match scelta:
        case "1":
            # LOGICA: Creazione manuale
            cod = input("Inserisci codice univoco: ")
            try:
                p_peso = float(input("Inserisci peso (kg): "))
                nuovo_pacco = Pacco(cod, p_peso)
                magazzino.aggiungi_pacco(nuovo_pacco)
            except ValueError:
                print("ERRORE: Inserisci un numero valido per il peso!")

        case "2":
            stato = input("Stato da filtrare (in magazzino / in consegna / consegnato): ")
            magazzino.mostra_per_stato(stato)

        case "3":
            cod = input("Codice pacco da aggiornare: ")
            nuovo = input("Nuovo stato: ")
            gestore.modifica_stato(cod, nuovo)

        case "4":
            peso_res = gestore.calcola_peso_totale()
            print(f"PESO TOTALE NON ANCORA CONSEGNATO: {peso_res} kg")

        case "0":
            print("Chiusura in corso...")
            break
        case _:
            print("Scelta non valida.")