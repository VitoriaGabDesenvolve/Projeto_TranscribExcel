import pandas as pd

def formatar(dados_excel):
    linhas = excel.shape[0]

    dados = []

    for linha in range(linhas):
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

    with open(f'{nome_arquivo}.txt', 'w') as arquivo_txt:
        for linha_formatada in dados:
            arquivo_txt.write(f"{linha_formatada}\n")

    return "programa rodou perfeitamente"


filename = input("Digite o nome do arquivo excel: ")
nome_arquivo = input("Digite o nome do arquivo que será criado: ")
numero_de_abas = int(input("1 aba - digite 1\nTodas abas - digite 2: "))

info_excel = pd.ExcelFile(filename)
info_abas_planilha = info_excel.sheet_names

if numero_de_abas == 1:
    nome_aba = input("Digite o nome da aba: ")

    for aba in info_abas_planilha:
        if nome_aba == aba:
            print("formatar")
            excel = pd.read_excel(filename, sheet_name=nome_aba)
            executar = formatar(excel)
        else:
            print("aba não encontrada")


elif numero_de_abas == 2:

    nome_original = nome_arquivo
    for aba in info_abas_planilha:
        nome_arquivo = f"{nome_original}_{aba}"

        excel = pd.read_excel(filename, sheet_name=aba)
        executar = formatar(excel)
