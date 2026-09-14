# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
# if a + b > c:
#     if a + c > b:
#         if b + c > a:
#             print('tak')
#         else:
#             print("nie")
#     else:
#         print('nie')    
# else:
#     print('nie')        

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a + b > c and a + c > b and b + c > a:
    print("tak")
else:
    print("nie")