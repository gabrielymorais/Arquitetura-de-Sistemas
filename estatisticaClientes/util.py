
def calcular_media(lista, chave):
    
    total = sum(cliente[chave] for cliente in lista)
    return total / len(lista)
