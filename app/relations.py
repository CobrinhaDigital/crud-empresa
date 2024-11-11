from tabulate import tabulate


# relação departamento e projeto
def add_departamento_projeto(numero_departamento: int, numero_projeto: int):
    with open("tables/departamento_projeto.txt", "a") as arquivo:
        arquivo.write(f"{numero_departamento}|{numero_projeto}|\n")

# relação entre funcionário e projeto
def add_funcionario_projeto(numero_funcionario: int, numero_projeto: int):
    with open("tables/funcionario_projeto.txt", "a") as arquivo:
        arquivo.write(f"{numero_funcionario}|{numero_projeto}|\n")
        arquivo.close()

def tabela_departamento_projeto():
    try:
        with open("tables/departamento_projeto.txt", "r") as arquivo:
            relacoes = arquivo.readlines()
            
        tabela = []
        for relacao in relacoes:
            numero_departamento, numero_projeto = relacao.strip().split("|")
            tabela.append([numero_departamento, numero_projeto])
        
        
        print("Relações Departamento-Projeto:")
        print(tabulate(tabela, headers=["Número do Departamento", "Número do Projeto"], tablefmt="grid"))
        arquivo.close()

    except FileNotFoundError:
        print("Arquivo departamento_projeto.txt não encontrado. Nenhuma relação criada.")

def tabela_funcionario_projeto():
    try:
        with open("tables/funcionario_projeto.txt", "r") as arquivo:
            relacoes = arquivo.readlines()
            
        tabela = []
        for relacao in relacoes:
            numero_funcionario, numero_projeto = relacao.strip().split("|")
            tabela.append([numero_funcionario, numero_projeto])
        
        # Exibindo a tabela formatada
        print("Relações Funcionário-Projeto:")
        print(tabulate(tabela, headers=["Número do Funcionário", "Número do Projeto"], tablefmt="grid"))
        arquivo.close()

    except FileNotFoundError:
        print("Arquivo funcionario_projeto.txt não encontrado. Nenhuma relação criada.")


def delete_departamento_projeto():
    with open("tables/departamento_projeto.txt", "r") as arquivo:
        relacoes = arquivo.readlines()

    tabela_departamento_projeto()
    
    numDepartamento = int(input("Informe o numero do departamento da relacao:\n>"))
    numProjeto = int(input("Informe o numero do projeto da relacao:\n>"))
    foiApagado = False
    
    for i in range(len(relacoes) - 1, -1, -1): 
        dados = relacoes[i].strip().split("|")  
        if len(dados) >= 2: 
            departamento = int(dados[0])
            projeto = int(dados[1])
            if departamento == numDepartamento and projeto == numProjeto:
                del relacoes[i]
                foiApagado = True
    
    with open("tables/departamento_projeto.txt", "w") as arquivo:
        arquivo.writelines(relacoes)
    
    if foiApagado:
        print("\nRelação apagada com sucesso!\n")
    else:
        print("\nRelação não encontrada!\n")




def delete_funcionario_projeto():
    with open("tables/funcionario_projeto.txt", "r") as arquivo:
        relacoes = arquivo.readlines()

    tabela_funcionario_projeto()  
    
    numFuncionario = int(input("Informe o numero do funcionario da relacao:\n>"))
    numProjeto = int(input("Informe o numero do projeto da relacao:\n>"))
    foiApagado = False
    
    for i in range(len(relacoes) - 1, -1, -1):  
        dados = relacoes[i].strip().split("|")  
        if len(dados) >= 2:
            funcionario = int(dados[0])
            projeto = int(dados[1])
            if funcionario == numFuncionario and projeto == numProjeto:
                del relacoes[i]
                foiApagado = True
    
    with open("tables/funcionario_projeto.txt", "w") as arquivo:
        arquivo.writelines(relacoes)
    
    if foiApagado:
        print("\nRelação apagada com sucesso!\n")
    else:
        print("\nRelação não encontrada!\n")