# Esercizio 1: Creare una serie di condizioni una dentro l'altra che a fronte di un input per ogni if decidano se fart passare o no (3 livelli, fate un paragone con ==)
# Verifica la media voto a fine anno scolastico
media_voto_finale = int(input("Inserisci il voto finale: "))
if (media_voto_finale >= 6):
    punteggio_provescritte = int(input("Inserisci il punteggio totalizzato nelle prove scritte: "))
    punteggio_provaorale = int(input("Inserisci il punteggio totalizzato nella prova orale: "))
# Verifica il punteggio totale delle prove di esame
    if (punteggio_provescritte + punteggio_provaorale >= 60):
        print("Prova superata")
    elif (punteggio_provescritte + punteggio_provaorale == 100):
        print("Prova superata con il punteggio massimo")
# Se la somma dei punteggi non raggiunge 60, considera i crediti scolastici conseguiti
    else:
        tot_crediti = int(input("Inserisci il totale dei crediti conseguiti: "))
        if (punteggio_provescritte + punteggio_provaorale + tot_crediti >= 60):
            print("Prova superata")
        else: 
            print("Prova non superata")
else:
    print("Non ammesso")


# Esercizio 2: Andare a creare un if con vari elif e un else finale che gestisca un menu per la selezione di un crud basilare (aggiungi, rimuovi, elimina)
lettere = ["a", "b", "c"]
print("--- 1. Aggiungi")
print("--- 2. Rimuovi")
print("--- 3. Elimina")
print("--- 4. Guarda la lista")

scelta = int(input("Cosa vuoi fare?"))
# Aggiunge un elemento
if scelta == 1:
    valore = input("Inserisci valore: ")
    lettere.append(valore)
    print(lettere)
# Rimuove un elemento
elif scelta == 2:
    valore = input("Cosa vuoi rimuovere?")
    if (valore in lettere):
        lettere.remove(valore)
        print(lettere)
    else:
        print("ERRORE: Lettera non presente")
# Cancella la lista
elif scelta == 3:
    lettere.clear()
    print("Cancellato tutto")
# Guarda la lista
elif scelta == 4:
    print(lettere)
# L'input iniziale non è nè 1, nè 2, nè 3
else:
    print("Comando non valido")
print("----------------------")
print("-------- Fine --------")  
print("----------------------")
    
# Esercizio 3: Creare un if con else semplice, dentro l'if inserire una struttura di creazione di dati (nome, password, id dato dal sistema a crescere) e nell'else il controllo automatico laddove è presente l'account nel sistema e solo se si passa dall'else concludere lo script
