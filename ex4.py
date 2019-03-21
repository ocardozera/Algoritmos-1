# Construa um programa que recebe três valores, A, B e C. Em seguida, apresente na tela os números em ordem crescente.

a = int(input("Olá, digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite mais outro número: "))

if(a>b and b>c):
    print(c,b,a)
##    3,2,1 #A, B, C
elif(a>b and c>b and a>c):
    print(b,c,a)
    ##2, 3, 1 #A, C, B]
elif(b>a and a>c):
    print(c,a,b)
    ##3 1 2 #B A C
elif(b>a and c>b):
    print(a,c,b)
    ##1 3 2 # B C A
elif(c>a and a>b):
    print(b,a,c)
    ##2 1 3 #C A B
elif(c>a and b>a ):
    print(a,b,c)
## 1 2 3 #c b a





"""a,b,c
a,c,b
b,a,c
b,c,a
c,a,b
c,b,a
"""
