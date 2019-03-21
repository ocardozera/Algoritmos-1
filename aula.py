# bebe, criança, adolescente, jovem, adulto e idoso


idade = int(input("Olá, digite sua idade: "))

if ( idade < 0 ):
    print("Idade inválida")
elif ( idade < 3):
    print("Você é um bebê")
elif ( idade <= 12):
    print("Você é uma criança")
elif ( idade <= 18):
    print("Você é adolescente")
elif ( idade <= 24):
    print("Você é jovem")
elif ( idade < 60):
    print("Você é adulto")
else:
    print("Você é idoso")




opcao1 = "1"
opcao2 = "2"
opcao3 = "3"
opcao4 = "4"
opcao5 = "5"

print(""" CADASTRO DE ALUNOS \n \"1)Cadastrar"/ """)
