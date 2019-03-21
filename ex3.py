# Construa um programa que recebe três valores, A, B e C. Em seguida, apresente na tela somente o maior deles.


a = int(input("Olá, digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite mais outro número: "))

if(a>b and a>c):
    print(a, "é o maior valor")
elif(b>a and b>c):
    print(b, "é o maior valor")
elif(c>a and c>b):
    print(c, "é o maior valor")
