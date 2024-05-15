from tkinter import *
from tkinter import filedialog
import subprocess


root = Tk()

root.geometry("374x200")
root.configure(background="#AB88DF")

filename = ""
nome_arquivo = ""

def selecionar_excel():
    global filename
    filename = filedialog.askopenfilename()
    if filename:
        print("Arquivo selecionado:", filename)
        button_excel.configure(background="#76E080", text="ARQUIVO SELECIONADO")


def formatar():
    global nome_arquivo
    nome_arquivo = entry_name.get()
    print(nome_arquivo)

    aba = var_qtd_aba.get()
    if aba == '1':
        nome_aba = label_nome_aba.get()
        print(nome_aba)
    elif aba == '2':
        print('aaaa')
    else:
        print('selecione a quantidade de abas')

    subprocess.run(['python', 'py\converter.py', filename, nome_arquivo])

    



label_excel = Label(root, text="EXCEL", background="#AB88DF")
button_excel = Button(root, text="SELECIONE O ARQUIVO EXCEL", width=51, borderwidth=0, background="#FFFFFF", command=selecionar_excel)


label_excel.pack()
button_excel.pack()


label_name = Label(root, text="NOME",  background="#AB88DF")
entry_name = Entry(root, width=60, borderwidth=0)


label_name.pack()
entry_name.pack()


var_qtd_aba = StringVar()

radio_uma_aba = Radiobutton(root, text="FORMATAR 1 ABA", value=1,  background="#AB88DF", variable=var_qtd_aba )
radio_todas_abas = Radiobutton(root, text="TODAS AS ABAS", value=2,  background="#AB88DF", variable=var_qtd_aba)

label_nome_aba = Entry(root, width=60)


radio_uma_aba.pack()
label_nome_aba.pack()
radio_todas_abas.pack()


button_formatar = Button(root, text="FORMATAR", borderwidth=0, background="#FFFFFF", command=formatar)
button_formatar.pack()

root.mainloop()