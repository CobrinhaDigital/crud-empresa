# Função para Criar um funcionário no arquivo.
def create_employee():
    employee = open("tables/funcionarios.txt", "a")

    name = str(input("Insira o nome do funcionario que deseja cadastrar:\n> "))
    numEmployee = int(input("Insira o numero do funcionario:\n> "))
    cpf = str(input("Insira o CPF do funcionario:\n> "))
    address = str(input("Insira o endereco do funcionario:\n> "))
    salary = float(input("Insira o salario do funcionario:\n> "))
    gender = str(input("Insira o genero do funcionario:\n> "))
    birth = str(input("Insira a data de nascimento do funcionario:\n> "))
    dep = int(input("Insira o numero do departamento que o funcionario faz parte:\n> "))

    employee.write(f"{name}|{numEmployee}|{cpf}|{address}|{salary}|{gender}|{birth}|{dep}|\n")
    employee.close()

    print("\nFuncionario cadastrado com sucesso!\n")

    pass

# Função para Editar um funcionário no arquivo.
def edit_employee():
    archive = open("tables/funcionarios.txt", "r")
    employees = archive.readlines()
    
    for i,v in enumerate(employees):
        employees[i] = employees[i].split("|")
    
    archive.close()
    
    get_all_employees()

    numEmployeeEdit = int(input("Insira o número do funcionario que deseja editar:\n> "))
    employeeEdit = int(input("\nInforme o campo que deseja editar:\n0 - Nome\n1 - Numero do funcionario\n2 - CPF\n3 - Endereco\n4 - Salario\n5 - Genero\n6 - Data de Nascimento\n7 - Numero do Departamento\n> "))
    newValue = input("\nDigite o novo valor a ser inserido:\n> ")
    quebraLinha = "\n"
    foiEditado = False

    for i,v in enumerate(employees):
        if v[1] == numEmployeeEdit:
            if employeeEdit == 7:
                v[employeeEdit] = f"{newValue}{quebraLinha}"
            v[employeeEdit] = newValue
            foiEditado = not foiEditado
    
    for i,v in enumerate(employees):
        employees[i] = f"{v[0]}|{v[1]}|{v[2]}|{v[3]}|{v[4]}|{v[5]}|{v[6]}|{v[7]}|\n"
    
    archive = open("tables/funcionarios.txt", "w")
    archive.writelines(employees)
    
    if foiEditado == True:
        print("\nCampo editado com sucesso!\n")
    else:
        print("\nCampo ou funcionario não encontrado!\n")
    
    archive.close()

    pass

# Função para Deletar um funcionário no arquivo.
def delete_employee():
    archive = open("tables/funcionarios.txt", "r")
    employees = archive.readlines()
    
    for i,v in enumerate(employees):
        employees[i] = employees[i].split("|")
    
    archive.close()
    
    get_all_employees()
    
    numEmployeeDelete = int(input("Insira o número do funcionario que deseja deletar:\n"))
    foiApagado = False 

    for i,v in enumerate(employees):
        if v[1] == numEmployeeDelete:
            del employees[i]
            foiApagado = not foiApagado

    for i,v in enumerate(employees):
        employees[i] = f"{v[0]}|{v[1]}|{v[2]}|{v[3]}|{v[4]}|{v[5]}|{v[6]}|{v[7]}|\n"
    
    archive = open("tables/funcionarios.txt", "w")
    archive.writelines(employees)

    if foiApagado == True:
        print("\nFuncionario deletado com sucesso!\n>")
    else:
        print("\nFuncionario não encontrado!\n")

    archive.close()

    pass

# Função para Visualizar os funcionários cadastrados no arquivo.
def get_all_employees():
    archive = open("tables/funcionarios.txt", "r")
    employees = archive.readlines()
    
    for i,v in enumerate(employees):
        employees[i] = employees[i].split("|")
    
    print("Funcionarios cadastrados:\n")

    for i in employees:
        print(f"Nome: {i[0]}\n")
        print(f"Numero do Funcionario: {i[1]}\n")
        print(f"CPF: {i[2]}\n")
        print(f"Endereco: {i[3]}\n")
        print(f"Salario: {i[4]}\n")
        print(f"Sexo: {i[5]}\n")
        print(f"Data de Nascimento: {i[6]}\n")
        print(f"Numero do Departamento: {i[7]}\n")
        print("----------------------------------------------------------------------------------------------------")
    
    archive.close()
    pass
