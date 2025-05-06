import random

def rolar_dados(qtd_dados):
    dados_rolados = [random.randint(1, 6) for _ in range(qtd_dados)]
    return dados_rolados

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    dado = dados_rolados.pop(dado_para_guardar)
    dados_no_estoque.append(dado)
    return [dados_rolados, dados_no_estoque]

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    dado = dados_no_estoque.pop(dado_para_remover)
    dados_rolados.append(dado)
    return [dados_rolados, dados_no_estoque]

def calcula_pontos_regra_simples(dados):
    pontos = {i: 0 for i in range(1, 7)}
    for dado in dados:
        if 1 <= dado <= 6:
            pontos[dado] += dado
    return pontos

def calcula_pontos_soma(dados):
    return sum(dados)

def calcula_pontos_sequencia_baixa(dados):
    l_ordem = []
    for n in dados:
        if n not in l_ordem:
            l_ordem.append(n)
    l_ordem = sorted(l_ordem)
    if len(l_ordem) < 4:
        return 0
    for i in range(len(l_ordem) - 3):
        if l_ordem[i+1] == l_ordem[i] + 1 and l_ordem[i+2] == l_ordem[i] + 2 and l_ordem[i+3] == l_ordem[i] + 3:
            return 15
    return 0

def calcula_pontos_sequencia_alta(dados):
    l_ordem = []
    for n in dados:
        if n not in l_ordem:
            l_ordem.append(n)
    if len(l_ordem) < 5:
        return 0
    l_ordem = sorted(l_ordem)
    for i in range(len(l_ordem) - 1):
        if l_ordem[i+1] != l_ordem[i] + 1:
            return 0
    return 30

def calcula_pontos_full_house(lista_inteiros):
    dic = {}
    for inteiro in lista_inteiros:
        dic[inteiro] = dic.get(inteiro, 0) + 1
    valores = dic.values()
    soma = 0
    if 3 in valores and 2 in valores:
        for numero in dic:
            soma += numero * dic[numero]
    return soma

def calcula_pontos_quadra(dados):
    contagem = {}
    for dado in dados:
        contagem[dado] = contagem.get(dado, 0) + 1
    for qtd in contagem.values():
        if qtd >= 4:
            return sum(dados)
    return 0

def calcula_pontos_quina(lista_inteiros):
    dic = {}
    for num in lista_inteiros:
        dic[num] = dic.get(num, 0) + 1
    for qtd in dic.values():
        if qtd >= 5:
            return 50
    return 0

def calcula_pontos_regra_avancada(dados):
    return {
        'cinco_iguais': calcula_pontos_quina(dados),
        'full_house': calcula_pontos_full_house(dados),
        'quadra': calcula_pontos_quadra(dados),
        'sem_combinacao': calcula_pontos_soma(dados),
        'sequencia_alta': calcula_pontos_sequencia_alta(dados),
        'sequencia_baixa': calcula_pontos_sequencia_baixa(dados)
    }

def faz_jogada(dados, categoria, cartela):
    if categoria in ['1', '2', '3', '4', '5', '6']:
        pontos_simples = calcula_pontos_regra_simples(dados)
        cartela['regra_simples'][int(categoria)] = pontos_simples[int(categoria)]
    else:
        pontos_avancados = calcula_pontos_regra_avancada(dados)
        if categoria in pontos_avancados:
            cartela['regra_avancada'][categoria] = pontos_avancados[categoria]
        else:
            cartela['regra_avancada'][categoria] = 0
    return cartela

def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)
