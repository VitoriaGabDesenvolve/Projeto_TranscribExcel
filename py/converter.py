import pandas as pd
from interface import filename
from interface import nome_arquivo


#Carregar arquivo excel
excel = pd.read_excel(filename)

#definir qtd de linhas do excel
linhas = excel.shape[0]

dados = []

#formatar cada linha 
for linha in range(linhas):

    linha_formatada = ""

    for coluna in range(0,9):

        valor_celula = excel.iloc[linha, coluna]

        if coluna == 1 or coluna == 2 or coluna == 4 or coluna == 5:
            valor_celula = "{:>03}".format(valor_celula)
        
        elif coluna == 6:
            valor_celula = "{: <010}".format(valor_celula)

        elif coluna == 7:
            valor_celula = valor_celula.strftime("%Y%m%d")

        elif coluna == 8:
            valor_celula = str("{:.2f}".format(valor_celula)).replace('.', '')
            valor_celula = "{:>08}".format(valor_celula)

        linha_formatada += str(valor_celula)

    dados.append(linha_formatada)

#converter para documento txt
with open(f'{nome_arquivo}.txt', 'w') as arquivo_txt:
    for linha_formatada in dados:
        arquivo_txt.write(f"{linha_formatada}\n")


print('programa rodou perfeitamente')
    





