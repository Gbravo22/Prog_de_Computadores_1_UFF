import time
class item ():
    def __init__(self, id, data, categoria, preco, quantidade, vtotal, vendedor):
        self.id = id
        self.data = data
        self.categoria = categoria
        try:
            self.preco = float(preco)
        except ValueError:
            self.preco = 0.0
        try:
            self.quantidade = int(quantidade) 
        except ValueError:
            self.quantidade = 0
        try:
            self.vtotal = float(vtotal)
        except ValueError:
            self.vtotal = 0.0 
        self.vendedor = vendedor
    def set_id (self,id):
        self.id = id
    def set_data (self, data):
        self.data = data
    def set_categoria (self, categoria):
        self.categoria = categoria
    def set_preco (self, preco):
        self.preco = float(str(preco).replace(',', '.'))
    def set_quantidade (self, quantidade):
        self.quantidade = int(quantidade)
    def set_vtotal (self, vtotal):
        self.vtotal = float(str(vtotal).replace(',', '.'))
    def set_vendedor (self, vendedor):
        self.vendedor = vendedor
    def get_id (self):
        return self.id
    def get_data (self):
        return self.data
    def get_categoria (self):
        return self.categoria
    def get_preco (self):
        return self.preco
    def get_quantidade (self):
        return self.quantidade
    def get_vtotal (self):
        return self.vtotal
    def get_vendedor (self):
        return self.vendedor
def acesso (arquivo):
    tempoinicial = time.time()
    vendas_lidas = [] 
    try:
        with open(arquivo, "r", encoding='utf-8') as arq:
            lista_linhas = arq.readlines()
            if not lista_linhas:
                return []
            if len(lista_linhas) < 2:
                return []
            for i in range (1, len(lista_linhas)):
                linha = lista_linhas[i].strip()
                if not linha:
                    continue
                partes = linha.split(",")
                if len(partes) != 7:
                    continue
                venda_id, data, categoria, preco_str, quantidade_str, vtotal_str, vendedor = partes
                preco_limpo = preco_str.replace('R$', '').replace(',', '.').strip()
                vtotal_limpo = vtotal_str.replace('R$', '').replace(',', '.').strip()
                quantidade_limpa = quantidade_str.strip()

                produto = item(venda_id, data, categoria, preco_limpo, quantidade_limpa, vtotal_limpo, vendedor)
                vendas_lidas.append(produto)
        tempofinal = time.time()
        tempototal = tempofinal - tempoinicial
        return vendas_lidas
    except FileNotFoundError:
        return None
    except Exception as e:
        return None
if __name__ == "__main__":
    arquivo = input("Qual arquivo voce deseja acessar? \n")
    lista = acesso(arquivo)
    if lista:
        if len(lista) > 1:
            print (f"Categoria do item 2 (ID: {lista[1].get_id()}): {lista[1].get_categoria()}")
            print (f"Preço do item 2: R$ {lista[1].get_preco():.2f}")
            print (f"Quantidade do item 2: {lista[1].get_quantidade()}")
            print (f"Valor total do item 2: R$ {lista[1].get_vtotal():.2f}")
        elif len(lista) == 1:
            print (f"Categoria do item 1 (ID: {lista[0].get_id()}): {lista[0].get_categoria()}")
            print (f"Preço do item 1: R$ {lista[0].get_preco():.2f}")
            print (f"Quantidade do item 1: {lista[0].get_quantidade()}")
            print (f"Valor total do item 1: R$ {lista[0].get_vtotal():.2f}")
        else:
            print("Nenhum item na lista após carregamento.")
    else:
        print("Não foi possível carregar a lista de vendas.")