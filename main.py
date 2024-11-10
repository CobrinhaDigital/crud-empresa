import app.employees as employees
import app.projects as projects
import app.departments as departments
import app.relations as relations

print("---------------------------------------- Bem-Vindo a API da Empresa Prafrentex ----------------------------------------\n")
while True:
    print("Informe a acao que deseja realizar:\n")
    opcao = int(input("0 - Criar\n1 - Visualizar\n2 - Editar\n3 - Deletar\n4 - Sair\n> "))
    if (opcao == 4):
        break
    print("Informe a tabela em que deseja fazer a acao:\n")
    tabela = int(input("0 - Funcionarios\n1 - Projetos\n2 - Departamentos\n> "))

    if (opcao == 0):
        if (tabela == 0):
            employees.create_employee()
        elif (tabela == 1):
            projects.criarProjeto()
        else:
            print("Tabela nao encontrada!")
    elif (opcao == 1):
        if (tabela == 0):
            employees.get_all_employees()
        elif (tabela == 1):
            projects.listarProjetos()
        else:
            print("Tabela nao encontrada!")
    elif (opcao == 2):
        if (tabela == 0):
            employees.edit_employee()
        elif (tabela == 1):
            projects.editarProjeto()
        else:
            print("Tabela nao encontrada!")
    elif (opcao == 3):
        if (tabela == 0):
            employees.delete_employee()
        elif (tabela == 1):
            projects.apagarProjeto()
        else:
            print("Tabela nao encontrada!")
    else:
        print("Opcao nao encontrada!")

print("ALL IS ON BY GOD")