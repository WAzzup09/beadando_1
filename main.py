#ASCII képek generálása

import random
import os

def menu():
    os.system('cls')

    rajzok = ["(0) Kilépés", "(1) Háromszög", "(2) Négyzet", "(3) Fenyőfa", "(4) Csillag", "(5) Kör", "(6) Gyémánt", "(7) Szív", "(8) Kockás Minta", "(9) Szinusz Hullám", "(10) Random Generált Útvesztő"]
    art = -1

    while art != 0:
        for i in range(len(rajzok)):
            print(rajzok[i])

        art = int(input("Kérem adja meg, melyik ASCII rajzot szeretné megtekinteni: "))

        if art == 0:
            print("KIléptél.")
            return
        elif art == 1:
            haromszog(6)
        elif art == 2:
            negyszog(4)
        elif art == 3:
            karifa(75)
        elif art == 4:
            csillag(5) #NE VÁLTOZTASD MEG AZ n-T (5-re van optimalizálva)
        elif art == 5:
            kor(25)
        elif art == 6:
            gyemant(20)
        elif art == 7:
            sziv()
        elif art == 8:
            kocka_minta(75, 75)
        elif art == 9:
            szinusz(10, 6, 100)
        elif art == 10:
            utveszto(10, 10)
        else:
            continue
        
        
# Sierpiński-háromszög
def haromszog(n:int):
    minta = ["*"]
    for i in range(n):
        szokoz = " " * (2**i)
        minta = [szokoz + x + szokoz for x in minta] + [x + " " + x for x in minta]
    print("\n".join(minta))

# Sierpiński-szőnyeg
def negyszog(n):
    minta = ["#"]
    for i in range(n):
        minta = [x + x + x for x in minta] + [x + x.replace("#", " ")+ x for x in minta] + [x + x + x for x in minta]
    print("\n".join(minta))

# Fenyőfa
def karifa(n):
    # Levelek
    for i in range(n + 1):
        print(' '*(n-i), '*'*((2*i)-1))

    # Törzs
    for i in range(5):
        print(' '*(n-3), '*'*(3))

# Csillag
def csillag(n):
    # Teteje
    minta1 = []
    for i in range(n-2):
        print(' '*(n-i-1), '*'*((2*i)-1))

    # Közepe
    for i in range(n):
        minta1.append(' '*(n-i) + '*'*((2*i)-1))
    temp = minta1[::-1]
    temp = [temp[0],temp[1]]
    print('\n'.join(temp))

    # Alja
    minta2 = []
    for i in range(n):
        minta2.append(' '*(n-3) + '*'*(n-i) + ' '*((2*i)-n) + '*'*(n-i))
    temp = [minta2[i-1], minta2[i]]
    print('\n'.join(temp))

# Kör
def kor(atmero):
    sugar = atmero / 2 - .5
    r = (sugar + .25)**2 + 1

    eredmeny = ''

    for i in range(atmero):
        y = (i - sugar)**2
        for j in range(atmero):
            x = (j - sugar)**2
            if x + y <= r:
                eredmeny = eredmeny + '#    '
            else:
                eredmeny = eredmeny + '     '
        eredmeny = eredmeny + '\n\n'

    print(eredmeny)

# Gyémánt
def gyemant(n):
    minta = []
    minta1 = []

    # Teteje
    for i in range(n):
        minta.append(' '*(n-i) + '*'*((2*i)-1))
    if n <= 10:
        temp = [minta[i-1], minta[i]]
    else:
        temp = [minta[i-2], minta[i-1], minta[i]]
    print('\n'.join(temp))

    # Alja
    for i in range(n-1):
        minta1.append(' '*(n-i) + '*'*((2*i)-1))
    print('\n'.join(minta1[::-1]))

# Szív
def sziv():
    for sor in range(6):
        for oszlop in range(7):
            if (sor == 0 and (oszlop == 1 or oszlop == 5)) or \
               (sor == 1 and (oszlop == 0 or oszlop == 3 or oszlop == 6)) or \
               (sor == 2 and (oszlop == 0 or oszlop == 6)) or \
               (sor == 3 and (oszlop == 1 or oszlop == 5)) or \
               (sor == 4 and (oszlop == 2 or oszlop == 4)) or \
               (sor == 5 and oszlop == 3):
                print('*', end='')
            else:
                print(' ', end='')
        print()

# Kocka Minta
def kocka_minta(sor, oszlop):
    for i in range(sor):
        for j in range(oszlop):
            if (i + j) % 2 == 0:
                print("#", end=" ")
            else:
                print(" ", end=" ")
        print()

# Szinusz hullám
def szinusz(bőség, frekvencia, szélesség):
    import math

    for i in range(szélesség):
        y = int(bőség * math.sin(frekvencia * i * (math.pi / szélesség)))
        print(" " * (y + bőség) + "*")

# Random Generált útvesztő
def utveszto(szelesseg, magassag):
    utveszto = [["#" for _ in range(szelesseg)] for _ in range(magassag)]
    
    for i in range(1, magassag - 1, 2):
        for j in range(1, szelesseg - 1, 2):
            utveszto[i][j] = " "
            irany = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
            utveszto[i + irany[0]][j + irany[1]] = " "
    
    for sor in utveszto:
        print("".join(sor))

menu()