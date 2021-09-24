import pickle

filename = 'betalinger.pk'

fodboldtur ={}

def afslut():
    outfile = open(filename, 'wb')
    pickle.dump(fodboldtur, outfile)
    outfile.close()
    print("Programmet er afsluttet!")

def printliste():
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
        printliste()
    if (valg == '2'):
        afslut()
    if (valg == '3'):
        personvalg = input("indtast det nummer personen er")
        if personvalg == "1":
            x = int(input("skriv beløb"))
            fodboldtur["Hans Hansen"] = fodboldtur.get("Hans Hansen") + x
            print(fodboldtur.get("Hans Hansen"))
            fodboldtur.update()
            printliste()
        if personvalg == "2":
            x = int(input("skriv beløb"))
            fodboldtur["Klaus Klausen"] = fodboldtur.get("Klaus Klausen") + x
            print(fodboldtur.get("Klaus Klausen"))
            fodboldtur.update()
            printliste()
        if personvalg == "3":
            x = int(input("skriv beløb"))
            fodboldtur["Ole Olsen"] = fodboldtur.get("Ole Olsen") + x
            print(fodboldtur.get("Ole Olsen"))
            fodboldtur.update()
            printliste()
        if personvalg == "4":
            x = int(input("skriv beløb"))
            fodboldtur["Bent Bentsen"] = fodboldtur.get("Bent Bentsen") + x
            print(fodboldtur.get("Bent Bentsen"))
            fodboldtur.update()
            printliste()
        if personvalg == "5":
            x = int(input("skriv beløb"))
            fodboldtur["Peter Petersen"] = fodboldtur.get("Peter Petersen") + x
            print(fodboldtur.get("Peter Petersen"))
            fodboldtur.update()
            printliste()
        if personvalg == "6":
            x = int(input("skriv beløb"))
            fodboldtur["Anders Andersen"] = fodboldtur.get("Anders Andersen") + x
            print(fodboldtur.get("Anders Andersen"))
            fodboldtur.update()
            printliste()
        if personvalg == "7":
            x = int(input("skriv beløb"))
            fodboldtur["Jens Jensen"] = fodboldtur.get("Jens Jensen") + x
            print(fodboldtur.get("Jens Jensen"))
            fodboldtur.update()
            printliste()
        if personvalg == "8":
            x = int(input("skriv beløb"))
            fodboldtur["Ib Ibsen"] = fodboldtur.get("Ib Ibsen") + x
            print(fodboldtur.get("Ib Ibsen"))
            fodboldtur.update()
            printliste()
    if (valg == '4'):
        personvalg = input("indtast det nummer personen er")
        if personvalg == "1":
            x = int(input("skriv beløb"))
            fodboldtur["Hans Hansen"] = fodboldtur.get("Hans Hansen") - x
            print(fodboldtur.get("Hans Hansen"))
            fodboldtur.update()
            printliste()
        if personvalg == "2":
            x = int(input("skriv beløb"))
            fodboldtur["Klaus Klausen"] = fodboldtur.get("Klaus Klausen") - x
            print(fodboldtur.get("Klaus Klausen"))
            fodboldtur.update()
            printliste()
        if personvalg == "3":
            x = int(input("skriv beløb"))
            fodboldtur["Ole Olsen"] = fodboldtur.get("Ole Olsen") - x
            print(fodboldtur.get("Ole Olsen"))
            fodboldtur.update()
            printliste()
        if personvalg == "4":
            x = int(input("skriv beløb"))
            fodboldtur["Bent Bentsen"] = fodboldtur.get("Bent Bentsen") - x
            print(fodboldtur.get("Bent Bentsen"))
            fodboldtur.update()
            printliste()
        if personvalg == "5":
            x = int(input("skriv beløb"))
            fodboldtur["Peter Petersen"] = fodboldtur.get("Peter Petersen") - x
            print(fodboldtur.get("Peter Petersen"))
            fodboldtur.update()
            printliste()
        if personvalg == "6":
            x = int(input("skriv beløb"))
            fodboldtur["Anders Andersen"] = fodboldtur.get("Anders Andersen") - x
            print(fodboldtur.get("Anders Andersen"))
            fodboldtur.update()
            printliste()
        if personvalg == "7":
            x = int(input("skriv beløb"))
            fodboldtur["Jens Jensen"] = fodboldtur.get("Jens Jensen") - x
            print(fodboldtur.get("Jens Jensen"))
            fodboldtur.update()
            printliste()
        if personvalg == "8":
            x = int(input("skriv beløb"))
            fodboldtur["Ib Ibsen"] = fodboldtur.get("Ib Ibsen") - x
            print(fodboldtur.get("Ib Ibsen"))
            fodboldtur.update()
            printliste()



infile = open(filename,'rb')
fodboldtur = pickle.load(infile)
infile.close()
menu()

