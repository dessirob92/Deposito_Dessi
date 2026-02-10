# 1. Crea un esercizio che rappresenti tutto quello che hai imparato 
# (variabili, condizioni, cicli, funzioni)
# Crea un programma Python da terminale che permetta all’utente di registrare e 
# controllare le proprie spese mensili.
# Il programma deve usare:
# - Variabili
# - input/output
# - condizioni
# - cicli
# - funzioni

# Inizializzazione
lista_spesa = set()
spesa_totale = 0.0


# Conversione immediata in numero (float) per poter fare calcoli
budget = int(input("Scrivi il tuo budget iniziale: "))

def main(budget_attuale, spesa_totale):
    print("---------- MENU SPESA ----------")
# L'opzione 1 viene mostrata visivamente solo se c'è budget
    if budget_attuale > spesa_totale:
        print("1. Aggiungi spesa --------------")
    else:
        print("------- [Budget Esaurito] -------")
# L'opzione 2 viene mostrata visivamente solo se ci sono articoli nel carrello, o meglio se la sepsa totale è diversa da 0
    if spesa_totale != 0:
        print("2. Rimuovi spesa ---------------")
    else:
        print(" [Carrello vuoto] --------------")
    print("3. Guarda la lista -------------")
    print("4. Calcola il totale della spesa ")
    print("5. Chiudi il programma ---------")
    print("--------------------------------")
    return input("Che operazione vuoi eseguire? ")

#Il sistema torna indietro solo se si scrive b, altrimenti continua a chiedere di scrivere b
def torna_indietro():
    while True:
        go_back = input("Premere 'b' per tornare indietro: ")
        if go_back == "b":
            return
        else:
            print("Errore: Per tornare indietro devi premere 'b'")

    

# Ciclo principale
programma = True
while programma:
    scelta = main(budget, spesa_totale)

    match scelta:
        case "1":
# Controllo attivazione:
            if budget > spesa_totale:
                prodotto_da_aggiungere = input("Cosa vuoi comprare? ")
                if prodotto_da_aggiungere.lower() == "annulla":
                    break
                else:
                    prezzo = int(input(f"Quanto costa {prodotto_da_aggiungere}? "))
                
                if spesa_totale + prezzo <= budget:
                    lista_spesa.add(prodotto_da_aggiungere)
                    spesa_totale += prezzo
                    print(f"Articolo aggiunto al carrello. Budget residuo: {budget - spesa_totale}€")
                else:
                    print("Operazione annullata: supereresti il budget!")
            else:
                print("Azione non disponibile: Budget esaurito!")
#2. Rimuovi spesa - inserire la logica che calcola il budget più la spesa rimossa. Prevedere iterazione (= Vuoi rimuovere altro?)       
        case "2":
# Attivo l'interruttore in_lista per non far entrare l'azione in loop se si sbaglia la stringa in input
            in_lista = True
            while in_lista:
                prodotto_da_rimuovere = input("Cosa vuoi togliere dal carrello? ")
#Verifico che la stringa di input corrisponda a uno degli elementi dentro la lista
                if prodotto_da_rimuovere in (lista_spesa):
                    prezzo = int(input(f"Quanto costa {prodotto_da_rimuovere}? "))
                    lista_spesa.discard(prodotto_da_rimuovere)
                    spesa_totale -= prezzo
                    print(f"Articolo rimosso dal carrello. Budget residuo: {budget - spesa_totale}€")
                    break
                elif prodotto_da_rimuovere.lower() == "annulla":
                    break
                else:
                    in_lista = False
                    print("Errore: Il prodotto non è nel carrello. Riprovare")                
#3. Guarda la lista
        case "3":
            print(lista_spesa)
            indietro = torna_indietro()
#4. Stampa il totale della spesa già calcolato nei case 1 e 2
        case "4":
            print(f"Totale spesa: {spesa_totale}€")
            indietro = torna_indietro()
#5.Chiudi il programma
        case "5":
            print("Chiusura in corso...")
            programma = False
        
#Scelta non valida (da inserire in un ciclo che ripete il programma finchè non si 
#seleziona l'opzione corretta)        
        case _:
            print("Operazione non valida. Riprovare")


# 2. Crea un sistema di funzioni che richiami tutte le singole parti che abbiamo
# creato nel precedente esercizio, devono essere usate SOLO funzioni e almeno da 2
# decoratori ed essere ripetibile

