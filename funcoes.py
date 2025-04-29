import random 

def rolar_dados(qtd_dados):
    dados_rolados = [random.randint(1,6) for _ in range(qtd_dados)] 

    return dados_rolados

