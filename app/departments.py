def criarDepartamento(): 
    nome = str(input("Insira o nome do departamento que deseja criar:\n> "))
    gerente = int(input("Insira o número do novo gerente:\n> "))
    numero = int(input("Insira o número do novo departamento:\n> "))

    with open("tables/departamentos.txt", "a") as file: 
        file.write(f"{nome}|{numero}|{gerente}|\n")
        
    file.close()

def verDepartamento(): 
    #mostra todos os departamentos 
    with open("tables/departamentos.txt", "r") as file: 
        content = file.readlines()

        for i,v in enumerate(content):
            content[i] = content[i].split("|")
        
        print("Departamentos atuais:\n")

    for i in content:
        print(f"Nome do Departamento: {i[0]}")
        print(f"Número do Departamento: {i[1]}")
        print(f"Número do Gerente: {i[2]}\n")
        print("-----------------------------------------------------------------")
    
    

def apagarDepartamento(): 
    verDepartamento()
    nome = input("Insira o número do departamento que deseja apagar:\n> ")
    
    with open("tables/departamentos.txt", "r") as file: 
        linhas = file.readlines()
        linhasMantidas = []
        
        for linha in linhas: 
            if nome not in linha: 
                linhasMantidas.append(linha)
                
    with open("tables/departamentos.txt", "w") as file: 
         file.writelines(linhasMantidas)
         
    file.close()
                
def editarDepartamento(): 
    arquivo = open("tables/departamentos.txt", "r")
    departamentos = arquivo.readlines()
    
    for i,v in enumerate(departamentos):
        departamentos[i] = departamentos[i].split("|")
    
    arquivo.close()
    
    verDepartamento()

    númeroProjetoEditar = input("Insira o número do departamento que deseja editar:\n> ")
    itemProjetoEditar = int(input("\nInsira o item que deseja editar do departamento escolhido:\n0 - Nome do Departamento\n1 - Número do Departamento\n2 - Número do Gerente\n> "))
    valorNovo = input("\nDigite o novo valor a ser inserido:\n> ")
    foiEditado = False

    for i,v in enumerate(departamentos):
        if v[1] == númeroProjetoEditar:
            v[itemProjetoEditar] = valorNovo
            foiEditado = not foiEditado
    
    for i,v in enumerate(departamentos):
        departamentos[i] = f"{v[0]}|{v[1]}|{v[2]}|\n"
    
    arquivo = open("tables/departamentos.txt", "w")
    arquivo.writelines(departamentos)
    
    if foiEditado == True:
        print("\nCampo editado com sucesso!\n")
    else:
        print("\nCampo ou departamento não encontrado!\n")
    
    arquivo.close()