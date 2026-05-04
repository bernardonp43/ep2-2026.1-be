import random
def rolar_dados (d):
    dados = []
    for i in range(5):
        if i in d:
            dados.append(d[i])
        else:
            dados.append(random.randint(1, 6))
    return dados
