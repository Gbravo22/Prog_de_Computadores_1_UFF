# etapa3
import time
from datetime import datetime
from ETAPA2 import item, acesso
CATEGORIAS = ['Camiseta básica','Camisa social','Regata','Casaco de moletom','Bermuda de moletom','Calça Jeans','Casaco de couro','Short Jeans','Bermuda de elastano']
ID_VENDEDORES = ['0001','0002','0003']

def adicionar_venda(vendas):
    print("\n--- Nova Venda ---")
    try:
        ultimo_id = int(vendas[-1].get_id()) if vendas else 0
        tam_id = len(vendas[-1].get_id()) if vendas else 5
        novo_id = str(ultimo_id + 1).zfill(tam_id)
        print("Categorias:")
        for i, c in enumerate(CATEGORIAS): print(f" {i+1}. {c}")
        categoria = CATEGORIAS[int(input("Escolha a categoria: ")) - 1]
        quantidade = int(input("Quantidade vendida: "))
        preco = float(input("Preço unitário: "))
        print("Vendedores:")
        for i, v in enumerate(ID_VENDEDORES): print(f" {i+1}. {v}")
        vendedor = ID_VENDEDORES[int(input("Escolha o vendedor: ")) - 1]
        venda = item(
            id=novo_id,
            data=datetime.now().strftime('%Y-%m-%d'),
            categoria=categoria,
            preco=preco,
            quantidade=quantidade,
            vtotal=round(quantidade * preco, 2),
            vendedor=vendedor
        )
        vendas.append(venda)
        print("Venda adicionada com sucesso!")
    except (ValueError, IndexError):
        print("Algo deu errado. Verifique os valores e tente novamente.")

def buscar_por_linha(vendas):
    print("\n--- Buscar por Linha ---")
    if not vendas:
        print("Sem vendas cadastradas.")
        return
    try:
        num = int(input(f"Digite o número da linha (1 a {len(vendas)}): ")) - 1
        if 0 <= num < len(vendas):
            venda = vendas[num]
            print("\nVenda encontrada:")
            print(f"ID Venda: {venda.get_id()}")
            print(f"Data: {venda.get_data()}")
            print(f"Categoria: {venda.get_categoria()}")
            print(f"Preço Unitário: R$ {venda.get_preco():.2f}")
            print(f"Quantidade: {venda.get_quantidade()}")
            print(f"Valor Total: R$ {venda.get_vtotal():.2f}")
            print(f"ID Vendedor: {venda.get_vendedor()}")
        else:
            print("Linha fora do intervalo.")
    except ValueError:
        print("Entrada inválida.")

def remover_venda(vendas):
    print("\n--- Remover Venda ---")
    id_venda = input("Digite o ID da venda: ")
    achou = None
    for v in vendas:
        if v.get_id() == id_venda:
            achou = v
            break
    if achou:
        print(f"Venda: ID {achou.get_id()}, Categoria {achou.get_categoria()}")
        confirma = input("Remover? (s/n): ").lower()
        if confirma == 's':
            vendas.remove(achou)
            print("Venda removida.")
        else:
            print("Remoção cancelada.")
    else:
        print("Venda não encontrada.")

def salvar_alteracoes(vendas, nome_arquivo):
    print(f"\nSalvando em '{nome_arquivo}'...")
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            f.write('id venda,data,categoria,preço unitário,quantidade,valor total,id vendedor\n')
            for v in vendas:
                linha = (
                    f"{v.get_id()},"
                    f"{v.get_data()},"
                    f"{v.get_categoria()},"
                    f"{v.get_preco()},"
                    f"{v.get_quantidade()},"
                    f"{v.get_vtotal()},"
                    f"{v.get_vendedor()}\n"
                )
                f.write(linha)
        print("Arquivo salvo com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar: {e}")

def menu_interativo():
    nome_arquivo = input("Nome do arquivo CSV para carregar: ")
    vendas = acesso(nome_arquivo)

    if vendas is None:
      print("Não foi possível iniciar o programa pois o arquivo não foi carregado.")
      return

    while True:
        print("\n===== MENU =====")
        print("1. Adicionar venda")
        print("2. Buscar por linha")
        print("3. Remover venda")
        print("4. Salvar alterações")
        print("5. Sair")

        op = input("Escolha: ")

        if op == '1':
            adicionar_venda(vendas)
        elif op == '2':
            buscar_por_linha(vendas)
        elif op == '3':
            remover_venda(vendas)
        elif op == '4':
            salvar_alteracoes(vendas, nome_arquivo)
        elif op == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu_interativo()
