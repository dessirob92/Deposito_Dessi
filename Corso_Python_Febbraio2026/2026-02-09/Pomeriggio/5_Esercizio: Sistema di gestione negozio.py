# Obiettivo: Implementare un sistema di gestione per un negozio che deve interagire con
# clienti, gestire l'inventario e permettere agli amministratori di supervisionare le
# operazioni. Il sistema sarà strutturato in 3 parti principali:
# 1. Gestione Clienti:
# - I clienti possono visualizzare gli articoli disponibili in inventario
# - I clienti possono selezionare e acquistare articoli dall'inventario
# - Il sistema tiene traccia degli acquisti dei clienti
# 
# 2. Gestione dell'inventario
# - Gli articoli in magazzino sono elencati con il nome, il prezzo e la quantità
# - Si possono aggiungere nuovi articoli all'inventario
# - Gli articoli possono essere rimossi o aggiornati
# 
# 3. Amministrazione
# - Gli amministratori possono visualizzare un rapporto delle vendite
# - Gli amministratori possono visualizzare lo stato corrente dell'inventario
# - Il sistema tiene traccia dei guadagni totali
# - Puoi pre-inserire gli amministratori, non i clienti
# 
# Il sistema dovrebbe permettere di simulare un'interazione base tra il cliente e il
# negozio dopo un login e una registrazione, nonchè fornire gli strumenti necessari
# per la manutenzione e l'analisi del negozio da parte degli amministratori


inventario = {
    "A": {"quantità": 3, "prezzo": 20.0}
}

utenti = {
    "Roberto": {"password": "123", "ruolo": "admin"}
}

totale_guadagni = 0
storico_acquisti = []

#Menu
def mostra_menu(ruolo):
    print("---------- MENU NEGOZIO ----------")
    if ruolo.lower() == "admin":
        print("1. Aggiungi prodotto")
        print("2. Aggiorna prodotto")
        print("3. Visualizza Report Vendite")
    else:
        print("1. [OPERAZIONE NON DISPONIBILE]")
        print("2. [OPERAZIONE NON DISPONIBILE]")
        print("3. [OPERAZIONE NON DISPONIBILE]")
    
    print("4. Mostra inventario")
    print("5. Acquista prodotto")
    print("0. Logout/Esci")
    print("--------------------------------")
    return input("Scegli un'opzione: ")

#Login
def login():
    username = input("Nome utente: ")
    password = input("Password: ")
    
    if username in utenti and str(utenti[username]["password"]) == password:
        return username
    print("ATTENZIONE: Credenziali errate!")
    return None

class Negozio:
#Funzione per registrare un nuovo utente --> Aggiunta item in un dizionario e dizionario dentro il dizionario -- Aggiungere lo scenario di aggiunta di un admin
    def registra_utente(self):
        nuovo = input("Nuovo username: ")
        if nuovo in utenti:
            print("Utente già esistente!")
        else:
            pwd = input("Crea password: ")
            utenti[nuovo] = {"password": pwd, "ruolo": "cliente"}
            print(f"Utente {nuovo} registrato come cliente.")
            
#Funzione per aggiungere un nuovo prodotto al dizionario --> Aggiunta item in un dizionario
    def aggiungi_prodotto(self):
        nome = input("Nome nuovo prodotto: ")
        if nome in inventario:
            print("Errore: Prodotto già presente nell'inventario. Scegliere opzione 2")
        else:
            quantità = int(input("Quantità: "))
            prezzo = float(input("Prezzo: "))
            inventario[nome] = {"quantità": quantità, "prezzo": prezzo}
            print(f"Prodotto {nome} aggiunto!")
            
#Funzione per aggiornare un prodotto del dizionario --> Modifica in un dizionario
    def aggiorna_prodotto(self):
        nome = input("Prodotto da aggiornare: ")
        if nome in inventario:
            quantità = int(input("Nuova quantità: "))
            prezzo = float(input("Nuovo prezzo: "))
            inventario[nome] = {"quantità": quantità, "prezzo": prezzo}
            print("Aggiornamento riuscito.")
        else:
            print("Errore: Prodotto non presente nell'inventario. Scegliere opzione 1")
            
#Funzione per acquistare un prodotto  --> Ricalcolo quantità disponibili e calcolo guadagno
    def acquista_prodotto(self, cliente):
        prodotto = input("Cosa vuoi comprare? ")
        if prodotto in inventario:
            quantità = int(input("Quanti pezzi? "))
            disp = inventario[prodotto]["quantità"]
            
            if disp >= quantità:
                prezzo_un = inventario[prodotto]["prezzo"]
                totale = prezzo_un * quantità
                
#Aggiornamento inventario
                inventario[prodotto]["quantità"] -= quantità
                totale_guadagni += totale
                storico_acquisti.append(f"Il cliente {cliente} ha comprato {quantità}x {prodotto}")
                
                print(f"Acquisto effettuato! Totale: {totale}€")
                if inventario[prodotto]["quantità"] == 0:
                    print("ATTENZIONE: Prodotto esaurito")
                elif inventario[prodotto]["quantità"] == 1:
                    print("ATTENZIONE: Solo una copia disponibile")
                elif inventario[prodotto]["quantità"] <= 3:
                    print("ATTENZIONE: Prodotto in esaurimento")
            else:
                print("Quantità non sufficiente in magazzino!")
        else:
            print("Prodotto non disponibile.")

#Ciclo per il menu di login
negozio_fisico = Negozio()
print("WELCOME!")

while True:
    print("1. Login")
    print("2. Registrati")
    print("0. Esci")
    scelta_iniziale = input("Scegli: ")
#1.Login    
    if scelta_iniziale == "1":
        user_loggato = login()
        if user_loggato:
            ruolo = utenti[user_loggato]["ruolo"]
            
#Sotto-ciclo per il menu del negozio
            mentre_loggato = True
            while mentre_loggato:
                scelta = mostra_menu(ruolo)
                
                match scelta:
#   1.Aggiungi prodotto
                    case "1":
                        if ruolo == "admin": negozio_fisico.aggiungi_prodotto()
                        else: print("Permesso negato.")
#   2.Aggiorna prodotto
                    case "2":
                        if ruolo == "admin": negozio_fisico.aggiorna_prodotto()
                        else: print("Permesso negato.")
#   3.Visualizza report vendite
                    case "3":
                        if ruolo == "admin":
                            print("--- REPORT ---")
                            print(f"Guadagni totali: {totale_guadagni}€")
                            print("Storico:", storico_acquisti)
                        else: print("Permesso negato.")
#   4.Mostra inventario
                    case "4":
                        print("INVENTARIO ATTUALE:", inventario)
#   5.Acquista prodotto
                    case "5":
                        negozio_fisico.acquista_prodotto(user_loggato)
#   0.Logout
                    case "0":
                        mentre_loggato = False
#2.Registrati    
    elif scelta_iniziale == "2":
        negozio_fisico.registra_utente()
#0.Esci
    elif scelta_iniziale == "0":
        print("Uscita in corso...")
        break