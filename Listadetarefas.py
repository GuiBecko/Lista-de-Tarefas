verdadeiro = '1';
tarefas = [] #lista vazia
while (verdadeiro == '1'):
    print("***********************\n")
    print("LISTA DE TAREFAS\n")

    print("1.adicionar uma tarefa\n")
    print("2.remover uma tarefa\n")

    escolha = input("escolha uma opcaoo: \n")


    if escolha == '1':
        tarefa = input("Nome da tarefa: ")
        tarefas.append(tarefa) #adiciona um item na lista
        print(tarefas)

        with open("Lista de tarefas.txt", "w") as myFile:
            myFile.write(str(tarefas))

        verdadeiro = input("Quer continuar no programa? (0 para fechar, 1 para continuar): ")
    elif escolha == '2':
        print(tarefas)
        escolha2 = int(input("Selecione o numero da tarefa que voce quer remover: "))
        tarefas.pop(escolha2 - 1) #remove um item da lista
        print(tarefas)

        with open("Lista de tarefas.txt", "w") as myFile:
            myFile.write(str(tarefas))

        verdadeiro = input("Quer continuar no programa? (0 para fechar, 1 para continuar): ")


#usuário executa por terminal
#modifica sua lista de tarefas
#programa salva a lista em um arquivo txt