def criarDepartamento(): 
    #cria departamento e pede nome e gerente 
    print("""=== CRIAR DEPARTAMENTO === \b 
    Para criar DEPARTAMENTO, informe -> \b""")
    nome = str(input("Nome do departamento: \b"))
    gerente = int(input("Número do gerente: \b"))
    numero = int(input("Número do departamento: \b"))

    with open("tables/departamentos.txt", "a") as file: 
        file.write("\n" + nome + " | " + gerente + " | " + numero + "\b")
        
    file.close()

def verDepartamento(): 
    #mostra todos os departamentos 
    with open("tables/departamentos.txt", "r") as file: 
        content = file.read()
        print(content)

def apagarDepartamento(): 
    print("""=== APAGAR DEPARTAMENTO === \b
    Para apagar departamento, informe ->""")
    nome = int(input("Número do departamento: \b"))
    
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
    print("""=== EDITAR DEPARTAMENTO === \b
    Para editar departamento, selecione -> \b""")
    selecaoNum = int(input("""
    0 - Nome do departamento
    1 - Gerente do departamento
    2 - Número do departamento \n"""))
    
    if selecaoNum == "0": 
        nomeAntigo = int(input("Digite o número do departamento: \b"))
        nomeNovo = input("Digite o novo nome do departamento: \b")
        
        with open("tables/departamentos.txt", "r") as file:
            linhas = file.readlines()
            
        with open("tables/departamentos.txt", "w") as file:
            for linha in linhas: 
                if nomeAntigo in linha:
                    linha = linha.replace(nomeAntigo, nomeNovo)
                file.write(linha)
                
        file.close()
            
    elif selecaoNum == "1":
        gerenteAntigo = int(input("Digite o número do gerente: \b"))
        gerenteNovo = int(input("Digite o novo número do gerente: \b"))
        
        with open("tables/departamentos.txt", "r") as file:
            linhas = file.readlines()
            
        with open("tables/departamentos.txt", "w") as file:
            for linha in linhas: 
                if gerenteAntigo in linha:
                    linha = linha.replace(gerenteAntigo, gerenteNovo)
                file.write(linha)
                
        file.close()
        
    elif selecaoNum == "2": 
        numeroAntigo = int(input("Digite o número do departamento: \b"))
        numeroNovo = int(input("Digite o novo número do departamento: \b"))
        
        with open("tables/departamentos.txt", "r") as file:
            linhas = file.readlines()
            
        with open("tables/departamentos.txt", "w") as file:
            for linha in linhas: 
                if numeroAntigo in linha:
                    linha = linha.replace(numeroAntigo, numeroNovo)
                file.write(linha)
                
        file.close()