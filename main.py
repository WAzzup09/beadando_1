#ASCII képek generálása

import random
import os

def menu():
    os.system('cls')

    rajzok = ["(0) Kilépés", "(1) Háromszög", "(2) Négyzet", "(3) Fenyőfa", "(4) Csillag", "(5) Kör",
              "(6) Gyémánt"]
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
            sziv(10)
        
        
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

#Szív
def sziv(n):
    '''
    def draw_heart():
    for row in range(6):
        for col in range(7):
            if (row == 0 and (col == 1 or col == 5)) or \
               (row == 1 and (col == 0 or col == 6)) or \
               (row == 2 and (col == 0 or col == 6)) or \
               (row == 3 and (col == 1 or col == 5)) or \
               (row == 4 and (col == 2 or col == 4)) or \
               (row == 5 and col == 3):
                print('*', end='')
            else:
                print(' ', end='')
        print()
    '''
    for sor in range(n):
        for oszlop in range(n+1):
            if (sor == n-6 and (oszlop == n-5 or oszlop == n-1)) or \
               (sor == n-5 and (oszlop == n-6 or oszlop == n)) or \
               (sor == n-4 and (oszlop == n-6 or oszlop == n)) or \
               (sor == n-3 and (oszlop == n-5 or oszlop == n-1)) or \
               (sor == n-2 and (oszlop == n-4 or oszlop == n-2)) or \
               (sor == n-1 and oszlop == n-3):
                print('*', end='')
            else:
                print(' ', end='')
        print()

menu()