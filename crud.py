import os 

def criarDep(): 
    inputDep = input()
    depPath = Path("/departamentos/{inputDep}")

    os.mkdir({depPath})

    os.mkdir("{depPath}/projetos")
    with open("lista.txt", "w") as file:
        file.write("")

    os.mkdir("{depPath}/funcionarios") 
    with open("lista.txt", "w") as file:
        file.write("")

def verDep(): 
    #lista todos os departamentos

def editarDep():
    #edita nome do departamento 

def apagarDep():  
    #apaga pasta do departamento 
