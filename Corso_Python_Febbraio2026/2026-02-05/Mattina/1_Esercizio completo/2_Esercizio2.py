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
        for c in range(numero1, numero2, 1):
            primo = True
            for n in range(2, int(c**0.5) + 1):
                if n % primo == 0:
                    lista_primi.append(n)
                    
                else:
                    primo = False
                    lista_nonprimi.append(c)
        print(lista_primi)
        print(lista_nonprimi)
    elif (numero1 > numero2):
       pass              

    
    esci = input("Vuoi ripetere il programma? SI - NO ")
    if esci.lower() == "si":
        programma 
    else:
        print("Uscita in corso...")
        break
    
# pari = [n for n in lista if n % 2 == 0]
# dispari = [n for n in lista if n % 2 != 0]