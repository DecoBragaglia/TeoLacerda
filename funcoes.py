import random 

def rolar_dados(qtd_dados):
    dados_rolados = [random.randint(1,6) for _ in range(qtd_dados)] 

    return dados_rolados

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):

    dado = dados_rolados.pop(dado_para_guardar)
    dados_no_estoque.append(dado)

    return [dados_rolados, dados_no_estoque]


def remover_dado(dados_rolados,dados_no_estoque,dado_para_remover):

    dado = dados_no_estoque.pop(dado_para_remover)
    dados_rolados.append(dado)
    return [dados_rolados, dados_no_estoque]