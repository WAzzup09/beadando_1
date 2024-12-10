#ASCII képek generálása

import random
import os

def menu():
    os.system('cls')

    rajzok = ["(0) Kilépés", "(1) Háromszög", "(2) Négyzet", "(3) Fenyőfa", "(4) Csillag", "(5) Kör"]
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
            csillag(5) #NE VÁLTOZTASD MEG AZ n-T
        elif art == 5:
            kor(25)
        
        
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
    for i in range(n + 1):
        print(' '*(n-i), '*'*((2*i)-1))

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

menu()