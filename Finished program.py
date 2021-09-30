import pickle

filename = 'betalinger.pk'

fodboldtur ={}




def afslut():
    outfile = open(filename, 'wb')
    pickle.dump(fodboldtur, outfile)
    outfile.close()
    print("Programmet er afsluttet!")

def printliste():
    count = 0
    for dude in fodboldtur.keys():
        print(count, dude)
        count += 1


def printliste2():
    for item in fodboldtur.items():
        print(item)
    menu()

def menu():
    print("MENU")
    print("1: Print liste")
    print("2: Afslut program")
    print("3: indbetaling vælg person og indskriv beløb")
    print("4 udbetaling vælg person og indtast beløb")
    valg = input("Indtast dit valg:")
    if (valg == '1'):
        printliste2()
    if (valg == '2'):
        afslut()
    if (valg == '3'):
        print(printliste())
        personvalg = int(input("indtast det nummer personen er"))

        #personvalgkey = fodboldtur.keys()[personvalg]

        personvalgkey = list(fodboldtur)[personvalg]

        beløb = int(input("beløb"))
        fodboldtur[personvalgkey] += beløb
        menu()
    if (valg == '4'):
        print(printliste())
        personvalg = int(input("indtast det nummer personen er"))
        personvalgkey = list(fodboldtur)[personvalg]
        beløb = int(input("beløb"))
        fodboldtur[personvalgkey] -= beløb
        menu()

infile = open(filename,'rb')
fodboldtur = pickle.load(infile)
infile.close()
menu()

#https://stackoverflow.com/questions/45221640/dict-keys-not-subscriptable?noredirect=1&lq=1