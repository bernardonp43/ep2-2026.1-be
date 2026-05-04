import random
def rolar_dados (n):
    dados = []
    for i in range(n):
        dados.append(random.randint(1, 6))
    return dados

def guardar_dado(d, dg, p):
    novo = [] 
    for x in dg:
        novo.append(x)    
    novo.append(d[p])    
    return [dg, novo]

def remover_dado(dg, p):
    x = {}
    for c in dg:
        if c != p:
            x[c] = dg[c]
    return x