
import util

def ler_arquivo_clientes(arquivo):

    contexto = {}
    with open(arquivo, 'r') as f:
        exec(f.read(), contexto)
    return contexto.get('clientes', [])

def main():
    clientes = ler_arquivo_clientes('clientes.txt')

    if not clientes:
        print("Nenhum cliente encontrado no arquivo.")
        return

    media_idade = util.calcular_media(clientes, 'idade')
    media_renda = util.calcular_media(clientes, 'renda')

    print(f"Média de Idade dos Clientes: {media_idade:.2f} anos")
    print(f"Média de Renda Mensal dos Clientes: R$ {media_renda:.2f}")

if __name__ == '__main__':
    main()
