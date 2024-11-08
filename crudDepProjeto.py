import os 

# def criarDepProjeto(): 
#     print("""=== CRIAR PROJETO - DEPARTAMENTO === \b
#     Para criar um projeto para um departamento, informe -> \b""")
#     numeroProjeto = input("Número do projeto: \b")
#     numeroDepartamento = input("Número do departamento: \b")

#     with open("depProjetos.txt", "a") as file: 
#         file.write("\n" + numeroProjeto + " | " + numeroDepartamento + "\b")

def verDepProjetos(): 
    with open("depProjetos.txt", "r") as file: 
        content = file.read()
        print(content)

# def apagarDepProjeto():

# def editarDepProjeto(): 

# criarDepProjeto()
# verDepProjetos()