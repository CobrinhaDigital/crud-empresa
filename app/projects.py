import app.relations as relations

def criarProjeto():
    arquivo = open("tables/projetos.txt", "a")
    númeroProjeto = input("Insira o número do projeto que deseja criar:\n> ")
    nomeProjeto = input("Insira o nome do novo projeto:\n> ")
    localProjeto = input("Insira o local do novo projeto:\n> ")
    
    quantidadeFuncionários = int(input("Insira quantos funcionários irão trabalhar nesse projeto:\n> "))
    for i in range(quantidadeFuncionários):
        númeroFuncionário = input(f"Insira o número do {i + 1}º funcionário a trabalhar nesse projeto:\n> ")
        relations.add_funcionario_projeto(númeroFuncionário, númeroProjeto)

    quantidadeDepartamentos = int(input("Insira quantos departamentos irão atuar nesse projeto:\n> "))
    for i in range(quantidadeDepartamentos):
        númeroDepartamento = input(f"Insira o número do {i + 1}º departamento a atuar nesse projeto:\n> ")
        relations.add_departamento_projeto(númeroDepartamento, númeroProjeto)

    arquivo.write(f"{númeroProjeto}|{nomeProjeto}|{localProjeto}|\n")
    arquivo.close()
    print("\nProjeto criado com sucesso!\n")
    pass

def editarProjeto():
    arquivo = open("tables/projetos.txt", "r")
    projetos = arquivo.readlines()
    
    for i,v in enumerate(projetos):
        projetos[i] = projetos[i].split("|")
    
    arquivo.close()
    
    listarProjetos()

    númeroProjetoEditar = input("Insira o número do projeto que deseja editar:\n> ")
    itemProjetoEditar = int(input("\nInsira o item que deseja editar do projeto escolhido:\n0 - Número do Projeto\n1 - Nome do Projeto\n2 - Local do Projeto\n3- Funcionários\n4 - Departamentos\n> "))

    if (itemProjetoEditar == 3):
        quantidadeFuncionários = int(input("Insira quantos funcionários serão adicionados ao projeto:\n> "))
        for i in range(quantidadeFuncionários):
            númeroFuncionário = input("Insira o número do funcionário a ser adicionado ao projeto:\n> ")
            relations.add_funcionario_projeto(númeroFuncionário, númeroProjetoEditar)
        print("Funcionário(s) adicionado(s) com sucesso!")
    elif (itemProjetoEditar == 4):
        quantidadeDepartamentos = int(input("Insira quantos departamentos serão adicionados ao projeto:\n> "))
        for i in range(quantidadeDepartamentos):
            númeroDepartamento = input("Insira o número do departamento a ser adicionado ao projeto:\n> ")
            relations.add_departamento_projeto(númeroDepartamento, númeroProjetoEditar)
        print("Departamento(s) adicionado(s) com sucesso!")
    else:
        valorNovo = input("\nDigite o novo valor a ser inserido:\n> ")
        foiEditado = False
        for i,v in enumerate(projetos):
            if v[0] == númeroProjetoEditar:
                v[itemProjetoEditar] = valorNovo
                foiEditado = not foiEditado
        
        for i,v in enumerate(projetos):
            projetos[i] = f"{v[0]}|{v[1]}|{v[2]}|\n"
        
        arquivo = open("tables/projetos.txt", "w")
        arquivo.writelines(projetos)
        
        if foiEditado == True:
            print("\nCampo editado com sucesso!\n")
        else:
            print("\nCampo ou projeto não encontrado!\n")
        
        arquivo.close()
    pass

def apagarProjeto():
    arquivo = open("tables/projetos.txt", "r")
    projetos = arquivo.readlines()
    
    for i,v in enumerate(projetos):
        projetos[i] = projetos[i].split("|")
    
    arquivo.close()
    
    listarProjetos()
    
    númeroProjetoApagar = input("Insira o número do projeto que deseja apagar:\n> ")
    foiApagado = False 

    for i,v in enumerate(projetos):
        if v[0] == númeroProjetoApagar:
            del projetos[i]
            foiApagado = not foiApagado

    for i,v in enumerate(projetos):
        projetos[i] = f"{v[0]}|{v[1]}|{v[2]}|\n"
    
    arquivo = open("tables/projetos.txt", "w")
    arquivo.writelines(projetos)

    if foiApagado == True:
        print("\nProjeto apagado com sucesso!\n")
    else:
        print("\nProjeto não encontrado!\n")

    arquivo.close()
    pass

def listarProjetos():
    arquivo = open("tables/projetos.txt", "r")
    projetos = arquivo.readlines()
    
    for i,v in enumerate(projetos):
        projetos[i] = projetos[i].split("|")
    
    print("Projetos atuais:\n")

    for i in projetos:
        print(f"Nº do Projeto: {i[0]}")
        print(f"Nome do Projeto: {i[1]}")
        print(f"Local do Projeto: {i[2]}\n")
        print("----------------------------------------------------------------------------------------------------")
    
    arquivo.close()
    pass
