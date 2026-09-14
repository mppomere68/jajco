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
