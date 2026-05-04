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