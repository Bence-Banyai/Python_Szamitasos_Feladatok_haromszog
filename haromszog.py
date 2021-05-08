import math


def haromszog_kerulet(a: float, b: float, c: float):
    return a+b+c


def haromszog_terulet(a: float, b: float, c: float):
    return math.sqrt(((a + b + c) / 2) * ((a + b + c) / 2 - a) * ((a + b + c) / 2 - b) * ((a + b + c) / 2 - c))


print('Háromszög terület és kerület számítása')
a = float(input('Adja meg az a oldalt:'))
b = float(input('Adja meg a b oldalt:'))
c = float(input('Adja meg a c oldalt:'))
if a < b + c and b < a + c and c < a + b:
    print('A kerület:', haromszog_kerulet(a, b, c))
    print('A terület:', haromszog_terulet(a, b, c))
else:
    print('Hiba: a háromszög nem szerkeszthető!')
