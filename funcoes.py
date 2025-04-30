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

def calcula_pontos_regra_simples(dados):
    pontos = {i: 0 for i in range(1,7)}
    for dado in dados:
        if 1 <= dado <= 6:
            pontos[dado] += dado
    return pontos

def calcula_pontos_soma(dados):
    total = 0 
    for dado in dados:
        total += dado
    return total

def calcula_pontos_sequencia_baixa(dados):
    dados_unicos = sorted(set(dados)) 

    sequencias_baixas = [
        [1, 2, 3, 4]
        [2, 3, 4, 5]
        [3, 4, 5, 6]
    ]

    for sequencia in sequencias_baixas:
        if all(numero in dados_unicos for numero in sequencia):
            return 15
    return 0 

def calcula_pontos_sequencia_baixa (dados):

    l_ordem = []

    for n in dados:
        if n not in l_ordem:
            l_ordem.append(n)
    
    l_ordem = sorted(l_ordem)

    if len(l_ordem)<4:
        return 0

    for i in range(len(l_ordem) - 3):

        cond1 = l_ordem[i+1] == l_ordem[i] + 1 and l_ordem[i+2] == l_ordem[i] + 2 and l_ordem[i+3] == l_ordem[i] + 3

        if cond1:

            return 15
    
    return 0

def calcula_pontos_sequencia_alta(dados):
    
    l_ordem = []

    for n in dados:


        if n not in l_ordem:
            l_ordem.append(n)

    
    if len(l_ordem)<5:
        return 0

    l_ordem = sorted(l_ordem)

    for i in range(len(l_ordem)-1):
        proximo = l_ordem[i] + 1


        if l_ordem[i+1] != proximo:

            return 0
    return 30

def calcula_pontos_full_house(lista_inteiros):
    dic={}
    for inteiro in lista_inteiros:
        if inteiro not in dic.keys():
            dic[inteiro]=1
        else:
            dic[inteiro]+=1
    valores = dic.values()
    soma=0
    if 3 in valores and 2 in valores:
        for numero in dic.keys():
            if dic[numero]==3:
                soma+=(3*numero)
            else:
                soma+=(2*numero)
    return soma