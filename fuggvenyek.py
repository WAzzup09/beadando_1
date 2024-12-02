import random

def intgen(a:int, b:int, c:int):
    lista = [random.randint(a,b) for _ in range(c)]
    return lista