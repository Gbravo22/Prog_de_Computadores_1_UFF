import time
class item ():
    # ------------------------- metodo construtor (cria um item)
    def __init__(self, id, data, categoria, preco, quantidade, vtotal, vendedor):
        self.id = id
        self.data = data
        self.categoria = categoria
        self.preco = preco
        self.quantidade = quantidade 
        self.vtotal = vtotal
        self.vendedor = vendedor
    # -------------------------- metodos para alteracao dos atributos (set - definir)
    def set_id (self,id):
        self.id = id
    def set_data (self, data):
        self.data = data
    def set_categoria (self, categoria):
        self.categoria = categoria
    def set_preco (self, preco):
        self.preco = preco
    def set_quantidade (self, quantidade):
        self.quantidade = quantidade
    def set_vtotal (self, vtotal):
        self.vtotal = vtotal
    def set_vendedor (self, vendedor):
        self.vendedor = vendedor
    # ------------------------------- metodos de acesso aos atributos (get - acessar)
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
    #preco = item1.get_preco
    #item.set_preco(20)
def acesso ():
    print ("Qual o nome do arquivo que você quer analisar?")
    arquivo = input()
    tempoinicial = time.time()
    with open(arquivo, "r+") as arq:
        lista = arq.readlines()
        lista_ID = []
        for i in range (1, len(lista) ):
            venda, data, categoria, preco, quantidade, vtotal, vendedor = lista[i].split(",")
            produto = item(venda, data, categoria, preco, quantidade, vtotal, vendedor)
            lista_ID.append(produto)
        print ("Qual o numero do produto que voce deseja acessar?")
        tempomedio1 = time.time()
        numero = int(input())
        tempomedio2 = time.time()
        produto = numero - 1
        print ("O que voce quer saber sobre ele dentro dos dados possiveis: id, data, categoria, preco, quantidade, valor total ou vendedor?")
        tempomedio3 = time.time()
        dado = input().upper()
        tempomedio4 = time.time()
        if dado == "ID":
            print (lista_ID[produto].get_id())
        elif dado == "DATA":
            print (lista_ID[produto].get_data())
        elif dado == "CATEGORIA":
            print (lista_ID[produto].get_categoria())
        elif dado == "PRECO":
            print (lista_ID[produto].get_preco())
        elif dado == "QUANTIDADE":
            print (lista_ID[produto].get_quantidade())
        elif dado == "VALOR TOTAL":
            print (lista_ID[produto].get_vtotal())
        else:
            print (lista_ID[produto].get_vendedor())
    tempofinal = time.time()
    tempo_total = (tempomedio1 - tempoinicial) + (tempomedio3 - tempomedio2) + (tempofinal - tempomedio4)
    print (f"O tempo que levamos para encontrar o dado {dado} do produto {numero} do arquivo {arquivo} foi: {tempo_total} ")
if __name__ == "__main__":
    acesso()
