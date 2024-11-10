def criarDepartamento(): 
    #cria departamento e pede nome e gerente 
    print("""=== CRIAR DEPARTAMENTO === \b 
    Para criar DEPARTAMENTO, informe -> \b""")
    nome = input("Nome do departamento: \b") 
    gerente = input("Nome do gerente: \b") 
    numero = input("Número do departamento: \b")

    with open("departamentos.txt", "a") as file: 
        file.write("\n" + nome + " | " + gerente + " | " + numero + "\b")
        
    file.close()

def verDepartamento(): 
    #mostra todos os departamentos 
    with open("departamentos.txt", "r") as file: 
        content = file.read()
        print(content)

def apagarDepartamento(): 
    print("""=== APAGAR DEPARTAMENTO === \b
    Para apagar departamento, informe ->""")
    nome = input("Nome do departamento: \b")
    
    with open("departamentos.txt", "r") as file: 
        linhas = file.readlines()
        linhasMantidas = []
        
        for linha in linhas: 
            if nome not in linha: 
                linhasMantidas.append(linha)
                
    with open("departamentos.txt", "w") as file: 
         file.writelines(linhasMantidas)
         
    file.close()
                
def editarDepartamento(): 
    print("""=== EDITAR DEPARTAMENTO === \b
    Para editar departamento, selecione -> \b""")
    selecaoNum = input("""
    0 - Nome do departamento
    1 - Gerente do departamento
    2 - Número do departamento \n""")
    
    if selecaoNum == "0": 
        nomeAntigo = input("Digite o nome do departamento: \b")
        nomeNovo = input("Digite o novo nome do departamento: \b")
        
        with open("departamentos.txt", "r") as file:
            linhas = file.readlines()
            
        with open("departamentos.txt", "w") as file:
            for linha in linhas: 
                if nomeAntigo in linha:
                    linha = linha.replace(nomeAntigo, nomeNovo)
                file.write(linha)
                
        file.close()
            
    elif selecaoNum == "1":
        gerenteAntigo = input("Digite o nome do gerente: \b")
        gerenteNovo = input("Digite o novo nome do gerente: \b") 
        
        with open("departamentos.txt", "r") as file:
            linhas = file.readlines()
            
        with open("departamentos.txt", "w") as file:
            for linha in linhas: 
                if gerenteAntigo in linha:
                    linha = linha.replace(gerenteAntigo, gerenteNovo)
                file.write(linha)
                
        file.close()
        
    elif selecaoNum == "2": 
        numeroAntigo = input("Digite o número do departamento: \b")
        numeroNovo = input("Digite o novo número do departamento: \b")
        
        with open("departamentos.txt", "r") as file:
            linhas = file.readlines()
            
        with open("departamentos.txt", "w") as file:
            for linha in linhas: 
                if numeroAntigo in linha:
                    linha = linha.replace(numeroAntigo, numeroNovo)
                file.write(linha)
                
        file.close()