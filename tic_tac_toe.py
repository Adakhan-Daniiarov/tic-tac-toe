brett = [["","",""],
         ["","",""],
         ["","",""]]


def zug_machen(zeile: int, spalte: int, zeichen: str):
    if zeichen == "x":
        brett[zeile][spalte] = "x"
    if zeichen == "o":
        brett[zeile][spalte] = "o"


def brett_anzeigen():
    for i in brett:
        print(i)

def brett_pruefen():
        if (   (brett[0][0] == "x" and brett[1][0] == "x" and brett[2][0] == "x")
            or (brett[0][1] == "x" and brett[1][1] == "x" and brett[2][1] == "x")
            or (brett[0][2] == "x" and brett[1][2] == "x" and brett[2][2] == "x")
            or (brett[0][0] == "x" and brett[0][1] == "x" and brett[0][2] == "x")
            or (brett[1][0] == "x" and brett[1][1] == "x" and brett[1][2] == "x")
            or (brett[2][0] == "x" and brett[2][1] == "x" and brett[2][2] == "x")
            or (brett[0][0] == "x" and brett[1][1] == "x" and brett[2][2] == "x")
            or (brett[0][2] == "x" and brett[1][1] == "x" and brett[2][0] == "x")):
            return 1
        if (   (brett[0][0] == "o" and brett[1][0] == "o" and brett[2][0] == "o")
            or (brett[0][1] == "o" and brett[1][1] == "o" and brett[2][1] == "o")
            or (brett[0][2] == "o" and brett[1][2] == "o" and brett[2][2] == "o")
            or (brett[0][0] == "o" and brett[0][1] == "o" and brett[0][2] == "o")
            or (brett[1][0] == "o" and brett[1][1] == "o" and brett[1][2] == "o")
            or (brett[2][0] == "o" and brett[2][1] == "o" and brett[2][2] == "o")
            or (brett[0][0] == "o" and brett[1][1] == "o" and brett[2][2] == "o")
            or (brett[0][2] == "o" and brett[1][1] == "o" and brett[2][0] == "o")):
            return 1

def IstFrei(zeile: int, spalte: int):
    if brett[zeile][spalte] == "":
        return True
    else:
        return False




while True:

    print("Spieler X ist dran")
    zeile = int(input("Zeile "))
    spalte = int(input("Spalte "))

    if IstFrei(zeile, spalte):
        zug_machen(zeile, spalte, "x")
        if brett_pruefen() == 1:
            brett_anzeigen()
            print("Spieler X hat gewonnen")
            break
        brett_anzeigen()
    else:
        while IstFrei(zeile, spalte) != True:
            print("Das Feld ist schon belegt!")
            zeile = int(input("Zeile "))
            spalte = int(input("Spalte "))
        zug_machen(zeile, spalte, "x")
        if brett_pruefen() == 1:
            brett_anzeigen()
            print("Spieler X hat gewonnen")
            break
        brett_anzeigen()

    print("Spieler O ist dran")
    zeile = int(input("Zeile "))
    spalte = int(input("Spalte "))

    if IstFrei(zeile, spalte):
        zug_machen(zeile, spalte, "o")
        if brett_pruefen() == 1:
            brett_anzeigen()
            print("Spieler O hat gewonnen")
            break
        brett_anzeigen()
    else:
        while IstFrei(zeile, spalte) != True:
            print("Das Feld ist schon belegt!")
            zeile = int(input("Zeile "))
            spalte = int(input("Spalte "))
        zug_machen(zeile, spalte, "o")
        if brett_pruefen() == 1:
            brett_anzeigen()
            print("Spieler O hat gewonnen")
            break
        brett_anzeigen()
