#czy to trojkat
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a + b > c:
    if a + c > b:
        if b + c > a:
            print('tak')
        else:
            print("nie")
    else:
        print('nie')    
else:
    print('nie')        


#jaki rodzaj trojkata
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a + b > c and a + c > b and b + c > a:
    if a == b and a == b and b == c:
        print('to jest troj rownoramieny')
    elif a == b or b == c or a == c:
        if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
            print("to jest troj rownoramieny prostokatny")
        else:
            print("to jest troj rownoramieny")
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
        print("to jest troj prostokatny roznoboczny")
    else:
        print("to jest troj ruznoboczny")
        
else:
    print("nie")
    
# kalkulator

import math
PI = math.pi

print('a - fig plaskie b - bryly')
inp = input(" ")
if inp == "a":
    print('q = ppkola c = ppProstokat')
    inp = input('')
    if inp == "q":
        r = float(input("r = "))
        print(f"dla r = {r} ppkola = {PI*r**2}")
    elif inp == "c":
        a = float(input('a = '))
        b = float(input('b = '))
        print(f"dla a = {a} i b = {b} ppProstokata = {a*b}")
elif inp == "b":
    print("q - szecian c - kola")
    inp = input('')
    if inp == "q":
        print('v - objetosc p - pp')
        inp = input('')
        if inp == "v":
            a = float(input("a = "))
            print(f"dla a = {a} obj szescianu = {a**3}")
        elif inp == "p":
            a = float(input('a = '))
            print(f"dla a = {a} ppszescianu = {(3 * math.sqrt(3) / 2) * (a ** 2)}")    
    elif inp == "c":
        print('v - obj p - pp')
        inp = input('')
        if inp == 'v':
            r = float(input('r = '))
            print(f"dla r = {r} obj kuli = {(4 / 3) * PI * (r**3)}")
        elif inp == "p":
            r = float(input('r = '))
            print(f"dla r = {r} pp kuli = {4 * PI * (r ** 2)}")
