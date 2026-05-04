import random
def rolar_dados (n):
    dados = []
    for i in range(n):
        dados.append(random.randint(1, 6))
    return dados

def guardar_dado(d, dg, p):
    dg[p] = d[p]
    return dg 