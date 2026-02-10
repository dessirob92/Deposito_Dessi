# 2.Intermedio / Numeri primi in un intervallo:
# Chiedi all'utente di inserire due numeri che definiscono un intervallo (es 10 e
# 50). Il programma dovrebbe stampare tutti i numeri primi compresi in
# quell'intervallo o i numeri non primi o entrambi divisi a tua scelta, salvandoli in
# due aggregazioni differenti e chiedere se deve ripetere
programma = True
while programma:
    numero1 = int(input("Inserisci il primo numero: "))
    numero2 = int(input("Inserisci il secondo numero: "))
#Inizializza le lista
    lista_primi = []
    lista_nonprimi = []
    if (numero1 < numero2):
        for n in range(numero1, numero2):
#Per ogni numero dell'intervallo controllo se il numero è primo
            if n < 2:
                lista_nonprimi.append(n)
            isprimo = True
#Per ogni numero partendo da 2 fino alla radice quadrata del numero in analisi controllo se è primo
            for i in range(2, int(n**0.5) +1):
                if n % i == 0:
                    isprimo = False
            if isprimo:
                lista_primi.append(n)
            else:
                lista_nonprimi.append(n)
        print("I numeri primi nell'intervallo sono: ", set(lista_primi))
        print("I numeri non primi nell'intervallo sono: ", set(lista_nonprimi))
#    elif (numero 1 > numero2):
#        pass
    else:
        print("Errore: I numeri sono uguali")              
    esci = input("Vuoi ripetere il programma? SI - NO ")
    if esci.lower() == "si": #Modificare inserendo un while per scegliere correttamente tra "si" e "no"
        programma 
    else:
        print("Uscita in corso...")
        break
    
# pari = [n for n in lista if n % 2 == 0]
# dispari = [n for n in lista if n % 2 != 0]