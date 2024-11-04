import os 
# import touch 
from pathlib import Path 

def criarDep(): 
    inputDep = input() 
    # depPath = "empresa/departamentos/{inputDep}"

    os.mkdir("departamentos/juridico")

    os.mkdir("departamentos/juridico/projetos")
    with open("lista.txt", "w") as file:
        file.write("")

    os.mkdir("departamentos/juridico/funcionarios")
    with open("lista.txt", "w") as file:
        file.write("")

def verDep(): 
    #lista todos os departamentos
    print(os.listdir("./departamentos"))

# def editarDep():
#     #edita nome do departamento 

# def apagarDep():  
#     #apaga pasta do departamento 

verDep()
