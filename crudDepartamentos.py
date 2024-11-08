import os 

def criarDepartamento(): 
    #cria departamento e pede nome e gerente 
    print(""" === CRIAR DEPARTAMENTO === \b 
    Para criar DEPARTAMENTO, informe -> \b""")
    nome = input("Nome do departamento: \b") 
    gerente = input("Nome do gerente: \b") 
    numero = input("Número do departamento: \b")

    with open("departamentos.txt", "a") as file: 
        file.write("\n" + nome + " | " + gerente + " | " + numero + "\b")

def verDepartamento(): 
    #mostra todos os departamentos 
    with open("departamentos.txt", "r") as file: 
        content = file.read()
        print(content)

# def apagarDepartamento(): 

# def editarDepartamento(): 

# verDepartamento()
# criarDepartamento()