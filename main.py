import employees
import crud

def EmpresaAPI():
    print("---------------------------------------- Bem-Vindo a API da Empresa blabla ----------------------------------------\n")
    print("Informe a acao que deseja realizar:\n")
    opcao = input("0 - Criar\n1 - Visualizar\n2 - Editar\n3 - Deletar\n>")
    print("Informe a tabela em que deseja fazer a acao:\n")
    tabela = input("0 - Funcionarios\n1 - Projetos\n>")

    if (opcao == "0"):
        if (tabela == "0"):
            employees.create_employee()
        elif (tabela == "1"):
            crud.criarProjeto()
        else:
            print("Tabela nao encontrada!")
    elif (opcao == "1"):
        if (tabela == "0"):
            employees.get_all_employees()
        elif (tabela == "1"):
            crud.listarProjetos()
        else:
            print("Tabela nao encontrada!")
    elif (opcao == "2"):
        if (tabela == "0"):
            employees.edit_employee()
        elif (tabela == "1"):
            crud.editarProjeto()
        else:
            print("Tabela nao encontrada!")
    elif (opcao == "3"):
        if (tabela == "0"):
            employees.delete_employee()
        elif (tabela == "1"):
            crud.apagarProjeto()
        else:
            print("Tabela nao encontrada!")
    else:
        print("Opcao nao encontrada!")

EmpresaAPI()