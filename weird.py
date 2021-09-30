import pickle

filename = 'betalinger.pk'

fodboldtur ={}




def afslut():
    outfile = open(filename, 'wb')
    pickle.dump(fodboldtur, outfile)
    outfile.close()
    print("Programmet er afsluttet!")

def printliste():
    #for item in fodboldtur.items():
    #    print(item)
    count = 0
    for dude in fodboldtur.keys():
        print(count, dude)
        count += 1
    menu()

def menu():
    print("MENU")
    print("1: Print liste")
    print("2: Afslut program")
    print("3: indbetaling vælg person og indskriv beløb")
    #print("4 udbetaling vælg person og indtast beløb")
    valg = input("Indtast dit valg:")
    if (valg == '1'):
        printliste()
    if (valg == '2'):
        afslut()
    if (valg == '3'):
        print()
        personvalg = int(input("indtast det nummer personen er"))
        personvalg.key = fodboldtur.keys()[personvalg]
        beløb = int(input("beløb"))
        fodboldtur[personvalg] += beløb



infile = open(filename,'rb')
fodboldtur = pickle.load(infile)
infile.close()
menu()

