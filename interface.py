import flet as ft
from tkinter import filedialog
import subprocess
def main(page: ft.Page):

    def selecionar_filename(e):
        filename = filedialog.askopenfilename()
        if filename:
            print("Arquivo selecionado:", filename)
            btn_filename.color = ft.colors.GREEN
            btn_filename.text = 'arquivo selecionado'
            btn_filename.update()
        return filename

    def executar(e):
        subprocess.run(['python', '.py'])

    def pegardados(e):
        valor_selecionado = selecionar_abas.value

        print(valor_selecionado)

        if valor_selecionado == '1':
            entrada_nome_aba.disabled = False
            page.update()
        elif valor_selecionado == '2':
            entrada_nome_aba.disabled = True
            page.update()



    page.fonts = {
        'Nunito': 'Font/NunitoSans-Italic-VariableFont_YTLC,opsz,wdth,wght.ttf'
    }
    # Configurações da janela

    page.bgcolor = ft.colors.BLACK38  # cor de backgroud da janela
    page.title = 'TranscribExcel' # titulo da janela

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER # alinhamento horizontal
    page.vertical_alignment = ft.MainAxisAlignment.CENTER # alinhamento vertical

    page.spacing = 20 # espaço entre elementos
    page.padding = ft.padding.all(25)  # espaço da borda

    page.window_height = 600  # altura da janela
    page.window_width = 380 # largura da tela
    page.window_resizable = False # não permitir alterar o tamanho da tela

    page.window_always_on_top = True # Ficar com a janela sempre em primeiro plano.

    # fim da estilização da tela

    # entrada de dados

    btn_filename = ft.ElevatedButton(
        text = 'Selecione o arquivo Excel',
        color = ft.colors.BLUE_500,
        on_click = selecionar_filename
    )

    entrada_nome_arquivo = ft.TextField(
        label='Nome do arquivo que será criado',
        label_style= ft.TextStyle(size=13),
        text_size=13,
        border_color=ft.colors.BLUE_500,
        border_radius=20,
        border_width=1,
        height=43

    )

    label_numero_abas = ft.Text(
        value='formatar:',
        style=ft.TextThemeStyle.BODY_MEDIUM,
        text_align=ft.alignment.center_right
    )

    selecionar_abas = ft.Dropdown(
        label= 'Selecione uma opção',
        value='2',
        label_style= ft.TextStyle(size=13),
        options= [
            ft.dropdown.Option(key='1', text='Uma aba'),
            ft.dropdown.Option(key='2', text='Todas as abas'),
        ],
        border_radius=20,
        border_color=ft.colors.BLUE_500,
        bgcolor= ft.colors.TRANSPARENT,
        height=43,
        width=400,
        text_size=12,
        alignment=ft.alignment.center,
        on_change=pegardados
    )

    entrada_nome_aba = ft.TextField(
        label='Digite o nome da Aba',
        disabled=True,
        label_style=ft.TextStyle(size=13),
        text_size=13,
        border_color=ft.colors.BLUE_500,
        border_radius=20,
        border_width=1,
        height=43
    )

    btn_executar = ft.ElevatedButton(
        text='Formatar',
        color=ft.colors.BLUE_500,
        on_click=executar,
    )

    page.add(btn_filename, entrada_nome_arquivo, label_numero_abas, selecionar_abas, entrada_nome_aba, btn_executar)
    page.update()

ft.app(target=main, assets_dir= 'assents')