# Obiettivo: Creare una classe Ristorante che permetta di gestire alcune funzionalità di base

# 1. Definizione della Classe:
# - Creare una classe chiamata Ristorante
# - La classe dovrebbe avere un costruttore __init__ che accetta 2 parametri: nome (nome
# del ristorante) e tipo_cucina (tipo di cucina offerta)
# - Definire un attributo aperto che indica se il ristorante è aperto o chiuso. Questo
# attributo deve essere impostato su False di default (cioè, il ristorante è chiuso)
# - Una Lista o + menu dove dentro ci sono i piatti e prezzi che ha il ristorante
# 
# 2. Metodi della Classe:
# - descrivi_ristorante(): Un metodo che stampa una frase descrivendo il ristorante,
# includendo il nome e il tipo di cucina
# - stato_apertura(): Un metodo che stampa se il ristorante è aperto o chiuso
# - apri_ristorante(): Un metodo che imposta l'attributo aperto su True e stampa un
# messaggio che indica che il ristorante è ora aperto
# - chiudi_ristorante(): Un metodo che imposta l'attributo aperto su False e stampa un
# messaggio che indica che il ristorante è ora chiuso
# - aggiungi_al_menu(): Un metodo per aggiungere piatti al menu
# - togli_dal_menu(): Un metodo per togliere piatti al menu
# - stampa_menu(): Un metodo per stampare il menu
# 
# 3. Testare la Classe:
# - Creare un'istanza della classe Ristorante, passando i valori appropriati al
# costruttore
# - Testare tutti i metodi creati per assicurarsi che funzionino come previsto

class Ristorante():
    aperto = False
    
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.menu = []
        self.prezzo = []

    def descrivi_ristorante(self):
        print(f"Nome ristorante: {self.nome}")
        print(f"Tipo cucina: {self.tipo_cucina}")
        
    def ristorante_aperto(self):
        if self.aperto == True:
            print("Siamo aperti")
        else:
            print("Siamo chiusi")
            
    def apri_ristorante(self):
        self.aperto = True
        print("Il ristorante ora è aperto")
        
    def chiudi_ristorante(self):
        self.aperto = False
        print("Il ristorante ora è chiuso")
        
    def aggiungi_al_menu(self): #Aggiungere la condizione che l'opzione si attiva solo se il ristorante è aperto           
        nome = input("Inserisci il nome: ")
        self.menu.append(nome)
        prezzo = input("Inserisci il prezzo: ")
        self.prezzo.append(prezzo)
        print("Articolo aggiunto al menu")
        
    def togli_dal_menu(self): #Aggiungere la condizione che l'opzione si attiva solo se il ristorante è aperto
        nome = input("Inserisci il nome: ")
        if nome in self.menu:
            indice = self.menu.index(nome)
            self.prezzo.pop(indice)
            self.menu.remove(nome)
        else:
            print(f"Errore: {nome} non è nel menu")
            
    def mostra_menu(self):
        indice_lista = len(self.menu)
        for i in range(0, indice_lista, 1):
            print(self.menu[i], "-", self.prezzo[i], "€")
            
            
#Aggiungere l'istanza del ristorante, il menu e il match sulla scelta 
#(vd. file 2_Esercizio settimana 1 del 2026-02-06 Pomeriggio)