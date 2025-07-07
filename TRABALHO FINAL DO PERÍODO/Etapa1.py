import random as rd
import time
import csv
from datetime import datetime, timedelta
categorias = ['Camiseta básica','Camisa social','Regata','Casaco de moletom','Bermuda de moletom','Calça Jeans','Casaco de couro','Short Jeans','Bermuda de elastano']
idvendedores = ['0001','0002','0003']
precosporcategoria = {
    'Camiseta básica' : (29.90,89.90),
    'Camisa social': (59.90,109.90),
    'Regata': (19.90,49.90),
    'Casaco de moletom': (109.90,210.90),
    'Bermuda de moletom': (59.90,89.90),
    'Calça Jeans': (129.90,189.90),
    'Casaco de couro': (219.90,349.90),
    'Short Jeans': (79.90,129.90),
    'Bermuda de elastano': (59.90,119.90)
}
def gerararquivo (arquivo,num_linhas):
    fill = len(str(num_linhas))
    tempoinicial = time.time()
    cabecalho = ['id venda','data','categoria','preço unitário','quantidade','valor total','id vendedor']
    datainiciovenda = datetime.now()
    with open(arquivo, 'w', newline = '', encoding = 'utf-8') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(cabecalho)
        for i in range(0,num_linhas):
            listalinha = []
            idvenda = i + 1
            idvenda = str(idvenda).zfill(fill)
            datainiciovenda = datainiciovenda + timedelta(hours = 7)
            data_formatada_csv = datainiciovenda.strftime('%Y-%m-%d')
            categoria = rd.choice(categorias)
            faixavalor = precosporcategoria[categoria]
            precomin = faixavalor[0]
            precomax = faixavalor[1]
            precounitario = round(rd.uniform(precomin,precomax),2)
            quantidade = rd.randint(1,5)
            precofinal = round((quantidade*precounitario),2)
            idvendedor = rd.choice(idvendedores)
            listalinha = [
                idvenda,            
                data_formatada_csv, 
                categoria,          
                f'R${precounitario}',      
                quantidade,         
                f'R${precofinal}',  
                idvendedor          
            ]
            escritor.writerow(listalinha)
        tempofinal = time.time()
        return tempofinal - tempoinicial
print('Qual o nome do arquivo que você deseja criar?')
arquivo = input()
print('Qual o número total de linhas que você deseja ter no seu arquivo?')
linhas = int(input())
tempo_teste = gerararquivo(arquivo,linhas)
print(f'O tempo que levou para gerar o arquivo {arquivo}, foi de {tempo_teste} segundos')
