# etapa3.py
import time
import csv
from datetime import datetime
CATEGORIAS = ['Camiseta básica','Camisa social','Regata','Casaco de moletom','Bermuda de moletom','Calça Jeans','Casaco de couro','Short Jeans','Bermuda de elastano']
ID_VENDEDORES = ['0001','0002','0003']
def carregar_dados_do_arquivo(nome_arquivo: str) -> list:
    lista_de_vendas = []
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_csv:
            # DictReader lê cada linha como um dicionário, usando o cabeçalho como chaves
            leitor = csv.DictReader(arquivo_csv)
            for linha in leitor:
                try:
                    # Converte os tipos de dados para uso interno (números para cálculos)
                    linha['preço unitário'] = float(linha['preço unitário'].replace('R$', '').strip())
                    linha['quantidade'] = int(linha['quantidade'])
                    linha['valor total'] = float(linha['valor total'].replace('R$', '').strip())
                    lista_de_vendas.append(linha)
                except (ValueError, KeyError) as e:
                    print(f"Aviso: Linha ignorada por erro de formato ou dado ausente: {linha} | Erro: {e}")
        return lista_de_vendas
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"Erro crítico ao ler o arquivo: {e}")
        return None
def adicionar_venda(lista_de_vendas: list):
    print("\n--- Adicionando Nova Venda ---")
    try:
        ultimo_id = int(lista_de_vendas[-1]['id venda']) if lista_de_vendas else 0
        comprimento_id = len(lista_de_vendas[-1]['id venda']) if lista_de_vendas else 5
        novo_id_str = str(ultimo_id + 1).zfill(comprimento_id)
        print("Categorias disponíveis:")
        for i, cat in enumerate(CATEGORIAS): print(f" {i+1}. {cat}")
        categoria = CATEGORIAS[int(input(f"Escolha o número da categoria: ")) - 1]
        quantidade = int(input("Digite a quantidade vendida: "))
        preco_unitario = float(input("Digite o preço unitário (ex: 49.90): "))
        print("Vendedores disponíveis:")
        for i, vend in enumerate(ID_VENDEDORES): print(f" {i+1}. {vend}")
        id_vendedor = ID_VENDEDORES[int(input(f"Escolha o número do vendedor: ")) - 1]
        nova_venda = {
            'id venda': novo_id_str,
            'data': datetime.now().strftime('%Y-%m-%d'),
            'categoria': categoria,
            'preço unitário': preco_unitario,
            'quantidade': quantidade,
            'valor total': round(quantidade * preco_unitario, 2),
            'id vendedor': id_vendedor
        }
        lista_de_vendas.append(nova_venda)
        print("\n✅ Venda adicionada com sucesso!")

    except (ValueError, IndexError):
        print("\n❌ Erro: Por favor, insira uma opção ou valor válido.")
def buscar_por_linha(lista_de_vendas: list):
    print("\n--- Buscando Venda por Número da Linha ---")
    total_linhas = len(lista_de_vendas)
    if not lista_de_vendas:
        print("Não há registros para buscar.")
        return
    try:
        num_linha = int(input(f"Digite o número da linha (1 a {total_linhas}): "))
        indice = num_linha - 1
        if 0 <= indice < total_linhas:
            venda = lista_de_vendas[indice]
            print("\n✅ Registro encontrado:")
            print("---------------------------------")
            for chave, valor in venda.items():
                if isinstance(valor, float):
                    print(f"{chave.capitalize()}: R$ {valor:.2f}")
                else:
                    print(f"{chave.capitalize()}: {valor}")
            print("---------------------------------")
        else:
            print("❌ Erro: Número da linha fora do intervalo válido.")
    except ValueError:
        print("❌ Erro: Por favor, digite um número inteiro válido.")
def remover_venda(lista_de_vendas: list):
    print("\n--- Removendo Venda ---")
    id_remover = input("Digite o ID da venda que deseja remover: ")
    item_para_remover = None
    for venda in lista_de_vendas:
        if venda['id venda'] == id_remover:
            item_para_remover = venda
            break
    if item_para_remover:
        print(f"Venda encontrada: ID {item_para_remover['id venda']}, Categoria {item_para_remover['categoria']}")
        confirmacao = input("Tem certeza que deseja remover esta venda? (s/n): ").lower()
        if confirmacao == 's':
            lista_de_vendas.remove(item_para_remover)
            print("✅ Venda removida com sucesso.")
        else:
            print("Operação de remoção cancelada.")
    else:
        print("Nenhuma venda encontrada com este ID.")
def salvar_alteracoes(lista_de_vendas: list, nome_arquivo_saida: str):
    print(f"\n--- Salvando dados em '{nome_arquivo_saida}' ---")
    cabecalho = ['id venda', 'data', 'categoria', 'preço unitário', 'quantidade', 'valor total', 'id vendedor']
    try:
        with open(nome_arquivo_saida, 'w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f)
            escritor.writerow(cabecalho)
            for venda in lista_de_vendas:
                linha_para_salvar = [
                    venda['id venda'],
                    venda['data'],
                    venda['categoria'],
                    f"R${venda['preço unitário']:.2f}",
                    venda['quantidade'],
                    f"R${venda['valor total']:.2f}",
                    venda['id vendedor']
                ]
                escritor.writerow(linha_para_salvar)
        print("✅ Dados salvos com sucesso!")
    except Exception as e:
        print(f"❌ Ocorreu um erro ao salvar o arquivo: {e}")
def menu_interativo():
    nome_arquivo = input("Digite o nome do arquivo de vendas para carregar (ex: vendas.csv): ")
    inicio_leitura = time.time()
    lista_de_vendas = carregar_dados_do_arquivo(nome_arquivo)
    fim_leitura = time.time()
    if lista_de_vendas is None:
        print(f"❌ Erro ao carregar o arquivo '{nome_arquivo}'. Encerrando programa.")
        return
    print(f"\nArquivo '{nome_arquivo}' carregado. {len(lista_de_vendas)} registros lidos.")
    print(f"Tempo de leitura do arquivo: {fim_leitura - inicio_leitura:.6f} segundos.")
    while True:
        print("\n===== MENU DE OPERAÇÕES DA LOJA =====")
        print("1. Adicionar nova venda")
        print("2. Buscar venda por número da linha")
        print("3. Remover venda por ID")
        print("4. Salvar alterações em novo arquivo")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            inicio_op = time.time()
            adicionar_venda(lista_de_vendas)
            fim_op = time.time()
            print(f"-> Tempo da operação 'Adicionar': {fim_op - inicio_op:.6f} segundos.")
        elif escolha == '2':
            inicio_op = time.time()
            buscar_por_linha(lista_de_vendas)
            fim_op = time.time()
            print(f"-> Tempo da operação 'Buscar': {fim_op - inicio_op:.6f} segundos.")
        elif escolha == '3':
            inicio_op = time.time()
            remover_venda(lista_de_vendas)
            fim_op = time.time()
            print(f"-> Tempo da operação 'Remover': {fim_op - inicio_op:.6f} segundos.")
        elif escolha == '4':
            nome_saida = input("Digite o nome do novo arquivo para salvar (ex: vendas_modificado.csv): ")
            inicio_op = time.time()
            salvar_alteracoes(lista_de_vendas, nome_saida)
            fim_op = time.time()
            print(f"-> Tempo da operação 'Salvar': {fim_op - inicio_op:.6f} segundos.")
        elif escolha == '5':
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")
if __name__ == "__main__":
    menu_interativo()
