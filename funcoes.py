import random
def rolar_dados (n):
    dados = []
    for i in range(n):
        dados.append(random.randint(1, 6))
    return dados

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    novo_estoque = []
    for x in dados_no_estoque:
        novo_estoque.append(x)
    novo_estoque.append(dados_rolados[dado_para_guardar])
    
    novos_rolados = []
    for i in range(len(dados_rolados)):
        if i != dado_para_guardar:
            novos_rolados.append(dados_rolados[i])
    
    return [novos_rolados, novo_estoque]

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    novos_rolados = []
    for x in dados_rolados:
        novos_rolados.append(x)
    novos_rolados.append(dados_no_estoque[dado_para_remover])
    
    novo_estoque = []
    for i in range(len(dados_no_estoque)):
        if i != dado_para_remover:
            novo_estoque.append(dados_no_estoque[i])
    
    return [novos_rolados, novo_estoque]

def calcula_pontos_regra_simples(dados):
    resultado = {}
    for face in range(1, 7):
        pontos = 0
        for dado in dados:
            if dado == face:
                pontos += face
        resultado[face] = pontos
    return resultado

def calcula_pontos_soma(dados):
    total = 0
    for dado in dados:
        total += dado
    return total