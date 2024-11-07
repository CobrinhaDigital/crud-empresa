import os 

def criarDepartamento(): 
    #cria departamento e pede nome e gerente 

    print(""" === CRIAR DEPARTAMENTO === \b 
    Para criar DEPARTAMENTO, informe -> \b""")
    nome = input("Nome do departamento: \b") 
    gerente = input("Nome do gerente: \b") 

    with open("departamentos.txt", "w") as file: 
        file.write(nome)
        file.write("|")
        file.write(gerente)
        file.write("\b")

def verDepartamento(): 
    #mostra todos os departamentos 
    with open("", "r") as file:


# def apagarDepartamento(): 

# def editarDepartamento(): 

criarDepartamento()