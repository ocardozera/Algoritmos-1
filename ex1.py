

print("""CADASTRO DE ALUNOS
1)Cadastrar
2)Alterar
3)Excluir
4)Consultar
5)Imprimir relatório""")
print("")

opcao = int(input("Digite sua opção: "))

if ( opcao == 1 ):
    print("Você escolheu cadastrar um aluno(a).")
elif ( opcao == 2):
    print("Você escolheu alterar um cadastro já existente.")
elif (opcao == 3):
    print("Você escolheu excluir um cadastro.")
elif (opcao == 4):
    print("Você escolheu consultar um cadastro.")
elif (opcao == 5):
    print("Você escolheu imprimir um relatório.")
else:
    print("Opção inválida.")
