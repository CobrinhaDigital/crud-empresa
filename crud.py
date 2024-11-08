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

def verDeps(): 
    #lista todos os departamentos
    with open("lista.txt", "r") as file: 
        file.read

# def editarDep():
#     #edita nome do departamento 

# def apagarDep():  
#     #apaga pasta do departamento 


verDep()