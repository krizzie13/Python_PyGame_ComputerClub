def startSpel():
    speelveld = []
    speelveld = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    huidigeSpeler = "O"
    spelerIndex = 0
    while isSpelNietKlaar(speelveld, huidigeSpeler):
        printSpelbord(speelveld)
        plaatsSymbool(huidigeSpeler, spelerIndex, speelveld)
        isSpelNietKlaar(speelveld, huidigeSpeler)
        huidigeSpeler = bepaalVolgendeSymbool(huidigeSpeler)
        spelerIndex = veranderSpeler(spelerIndex)
    printSpelbord(speelveld)
    print(f"Speler {spelerIndex + 1} heeft gewonnen!")


def plaatsSymbool(symbool, spelerIndex, speelveld):
    herhalen = True
    while herhalen:
        print(f"Speler {spelerIndex + 1} is aan beurt. Waar wilt u uw zet plaatsen? [rij kolom]")
        zet = input()
        rij = int(zet[0])
        kolom = int(zet[2])
        if 0 <= rij < 3 and 0 <= kolom < 3:
            if speelveld[rij][kolom] == " ":
                speelveld[rij][kolom] = symbool
                herhalen = False
            else:
                print("Daar staat al een teken.")
        else:
            print("Foute waarde, probeer opnieuw.")


def printSpelbord(spelbord):
    print("SPELBORD:")
    for rij in spelbord:
        for kolom in rij:
            print(kolom, end=' ')
        print()

def bepaalVolgendeSymbool(symbool):
    if symbool == "O":
        return "X"
    elif symbool == "X":
        return "O"


def veranderSpeler(spelerIndex):
    return (spelerIndex + 1) % 2


def isSpelNietKlaar(speelveld, netGespeeldSymbool):
    # horizontaal
    for rij in speelveld:
        if rij[0] == "O" and rij[1] == "X" and rij[2] == "O":
            return False

    # verticaal
    for x in range(3):
        rij = speelveld[x]
        if rij[0] == "O" and rij[1] == "X" and rij[2] == "O":
            return False

    # hoofdDiagonaal
    if speelveld[0][0] == "O" and speelveld[1][1] == "X" and speelveld[2][2] == "O":
        return False
    # nevenDiagonaal
    if speelveld[0][2] == "O" and speelveld[1][1] == "X" and speelveld[2][0] == "O":
        return False

    return True


startSpel()

