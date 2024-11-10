import app.relations as relations

def criarProjeto():
    arquivo = open("tables/projetos.txt", "a")
    númeroProjeto = int(input("Insira o número do projeto que deseja criar:\n> "))
    nomeProjeto = str(input("Insira o nome do novo projeto:\n> "))
    localProjeto = str(input("Insira o local do novo projeto:\n> "))
    
    quantidadeFuncionários = int(input("Insira quantos funcionários irão trabalhar nesse projeto:\n> "))
    for i in quantidadeFuncionários:
        númeroFuncionário = int(input(f"Insira o número do {i}º funcionário a trabalhar nesse projeto:\n> "))
        relations.add_funcionario_projeto(númeroFuncionário, númeroProjeto)

    quantidadeDepartamentos = int(input("Insira quantos departamentos irão atuar nesse projeto:\n> "))
    for i in quantidadeDepartamentos:
        númeroDepartamento = int(input(f"Insira o número do {i}º departamento a atuar nesse projeto:\n> "))
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

    númeroProjetoEditar = int(input("Insira o número do projeto que deseja editar:\n> "))
    itemProjetoEditar = int(input("\nInsira o item que deseja editar do projeto escolhido:\n0 - Número do Projeto\n1 - Nome do Projeto\n2 - Local do Projeto\n> "))
    valorNovo = input("\nDigite o novo valor a ser inserido:\n> ")
    quebraLinha = "\n"
    foiEditado = False

    for i,v in enumerate(projetos):
        if v[0] == númeroProjetoEditar:
            if itemProjetoEditar == 2:
                v[itemProjetoEditar] = f"{valorNovo}{quebraLinha}"
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
    
    númeroProjetoApagar = int(input("Insira o número do projeto que deseja apagar:\n> "))
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
