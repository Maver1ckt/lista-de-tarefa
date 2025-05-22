tarefa = []
opcao = 0

def mostrar_lista():
    print(">>> Lista <<<")
    for i, item in enumerate(tarefa, 1):
        status = "[x]" if item['CONCLUIDA'] else "[ ]"
        print(f"{i}. {status} {item['TAREFA']}")
    print()

while opcao != 5:
    print("1 Adicionar tarefa")
    print("2 Mostrar lista de tarefas")
    print("3 Marcar tarefa como concluída")
    print("4 Remover tarefa")
    print("5 Sair\n")

    try:
        opcao = int(input("Digite uma opcão: "))
    except ValueError:
        print("Digite uma opcão valida\n")
        continue

    if opcao == 1:
        nova_tarefa = input("Digite a nova tarefa: ")
        if nova_tarefa:
            tarefa.append({"TAREFA": nova_tarefa, "CONCLUIDA": False})
            print("TAREFA ADICIONADA COM SUCESSO!\n")
        else:
            print("A TAREFA NÃO PODE ESTAR VAZIA\n")

    elif opcao == 2:
        if not tarefa:
            print("NENHUMA TAREFA CADASTRADA\n")
        else:
            mostrar_lista()

    elif opcao == 3:
        if not tarefa:
            print("NENHUMA TAREFA CADASTRADA\n")
        else:
            mostrar_lista()
            try:
                num = int(input("Escolha uma tarefa para marcar como concluída: "))
                if 1 <= num <= len(tarefa):
                    tarefa[num - 1]['CONCLUIDA'] = True
                    print("TAREFA MARCADA COMO CONCLUÍDA!\n")
                else:
                    print("Número invalido\n")
            except ValueError:
                print("Digite uma opcão valida")

    elif opcao == 4:
        if not tarefa:
            print("NENHUMA TAREFA CADASTRADA\n")
        else:
            mostrar_lista()
            try:
                num = int(input("Escolha uma tarefa para remover: "))
                if 1 <= num <= len(tarefa):
                    removida = tarefa.pop(num - 1)
                    print(f"Tarefa '{removida['TAREFA']}' removida com sucesso")
                else:
                    print("Opcão invalida\n")
            except ValueError:
                print("Escolha uma opcão invalida\n")

    elif opcao == 5:
        print("Saindo ...")
        break
    else:
        print("Escolha uma opcão entre 1 e 5\n")