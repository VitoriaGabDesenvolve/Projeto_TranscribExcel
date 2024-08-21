import pandas as pd

def formatar(excel, nome_arquivo):

    linhas = excel.shape[0] # pegar numeros de linhas
    dados = []

    for linha in range(linhas): # percorrer pelas linhas e formatar
        linha_formatada = ""

        for coluna in range(0, 9):
            valor_celula = excel.iloc[linha, coluna]

            if coluna == 1 or coluna == 2 or coluna == 4 or coluna == 5:
                valor_celula = "{:>03}".format(valor_celula)

            elif coluna == 6:
                valor_celula = "{: <010}".format(valor_celula)

            elif coluna == 7:
                valor_celula = valor_celula.strftime("%Y%m%d")

            elif coluna == 8:
                valor_celula: str = str("{:.2f}".format(valor_celula)).replace('.', '')
                valor_celula = "{:>08}".format(valor_celula)

            linha_formatada += str(valor_celula)

        dados.append(linha_formatada)
    
    # escrever arquivo com as informações formatadas

    with open(f'{nome_arquivo}.txt', 'w') as arquivo_txt: 
        for linha_formatada in dados:
            arquivo_txt.write(f"{linha_formatada}\n")

    print('sucesso')

# Função que será importada na interface para executar a formatação

def executarFormatacao(filename, nome_arquivo, numero_de_abas, nome_aba):

    info_excel = pd.ExcelFile(filename)
    info_abas_planilha = info_excel.sheet_names # pega quantas abas possui na planilha

    if numero_de_abas == '1':

        for aba in info_abas_planilha:
            if nome_aba.lower() == aba.lower():
                print("formatar")
                excel = pd.read_excel(filename, sheet_name=aba)
                formatar(excel, nome_arquivo)
                break
            else:
                print("aba não encontrada")


    elif numero_de_abas == '2':
        nome_original = nome_arquivo

        for aba in info_abas_planilha:
            nome_arquivo = f"{nome_original}_{aba}"

            excel = pd.read_excel(filename, sheet_name=aba)
            formatar(excel, nome_arquivo)