def ler_valores_compras():
    entrada_str = input("Digite os valores das compras, separados por vírgula: ")
    lista_de_compras = list(map(int, entrada_str.split(',')))
    return lista_de_compras
def calcular_locacoes_gratis(compras):
    """Recebe uma lista de compras e retorna uma lista com o número de locações grátis para cada uma."""
    locacoes_calculadas = []
    for valor_compra in compras:
        num_locacoes = valor_compra // 10
        locacoes_calculadas.append(num_locacoes)
    return locacoes_calculadas
if __name__ == "__main__":
    lista_de_compras_usuario = ler_valores_compras()
    resultado_final = calcular_locacoes_gratis(lista_de_compras_usuario)
    print("O número de locações grátis para cada compra é:")
    print(resultado_final)
