import flet as ft
from tkinter import filedialog
from main import executarFormatacao

filename = str
nome_da_aba = str
opcao_selecionada = int
nome_do_arquivo = str
def main(page: ft.Page):

    def selecionar_filename(e):
        global filename
        filename = filedialog.askopenfilename()
        if filename:
            print("Arquivo selecionado:", filename)
            btn_filename.color = ft.colors.GREEN
            btn_filename.text = 'arquivo selecionado'
            label_arquivo_selecionado.value = f'arquivo selecionado: {filename}'
            label_arquivo_selecionado.color = ft.colors.WHITE,
            label_arquivo_selecionado.update()
            btn_filename.update()


    def pegar_dados(e):
        global opcao_selecionada, nome_do_arquivo, nome_da_aba

        opcao_selecionada = selecionar_abas.value
        
        if opcao_selecionada == '1':
            entrada_nome_aba.disabled = False
            nome_da_aba = entrada_nome_aba.value
            page.update()
        elif opcao_selecionada == '2':
            entrada_nome_aba.disabled = True
            page.update()

        nome_do_arquivo = entrada_nome_arquivo.value

        return [filename, nome_do_arquivo, opcao_selecionada, nome_da_aba]

    def fechar_dialog(e):
        page.close(caixa_dialog)
    # Configurações da janela

    page.bgcolor = ft.colors.BLACK38  # cor de backgroud da janela
    page.title = 'TranscribExcel' # titulo da janela

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER # alinhamento horizontal
    page.vertical_alignment = ft.MainAxisAlignment.CENTER # alinhamento vertical

    page.spacing = 20 # espaço entre elementos
    page.padding = ft.padding.all(25)  # espaço da borda

    page.window.height = 600  # altura da janela
    page.window.width = 380 # largura da tela
    page.window.resizable = False # não permitir alterar o tamanho da tela

    page.window.always_on_top = True # Ficar com a janela sempre em primeiro plano.
    page.window.always_on_top = True

    # fim da estilização da tela

    # entrada de dados

    btn_filename = ft.ElevatedButton(
        text = 'Selecione o arquivo Excel',
        color = ft.colors.BLUE_500,
        on_click = selecionar_filename,
        icon= ft.icons.FILE_UPLOAD_OUTLINED
    )

    label_arquivo_selecionado = ft.Text(
        value=f'arquivo não foi selecionado',
        color=ft.colors.TRANSPARENT,
        size=8.5,
        text_align=ft.alignment.center)

    entrada_nome_arquivo = ft.TextField(
        label='Nome do arquivo que será criado',
        label_style= ft.TextStyle(size=13),
        text_size=13,
        border_color=ft.colors.BLUE_500,
        border_radius=20,
        border_width=1,
        height=43,
        on_change = pegar_dados

    )

    label_numero_abas = ft.Text(
        value='FORMATAR:',
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
        bgcolor= ft.colors.BLACK38,
        height=43,
        width=400,
        text_size=13,
        alignment=ft.alignment.center,
        on_change=pegar_dados
    )

    entrada_nome_aba = ft.TextField(
        label='Digite o nome da Aba',
        disabled=True,
        label_style=ft.TextStyle(size=13),
        text_size=13,
        border_color=ft.colors.BLUE_500,
        border_radius=20,
        border_width=1,
        height=43,
        on_change=pegar_dados
    )


    def executar(e):
        dados = pegar_dados(e)
        executarFormatacao(dados[0], dados[1], dados[2], dados[3]),
        page.open(caixa_dialog)


    btn_executar = ft.ElevatedButton(
        text='Formatar',
        color=ft.colors.BLUE_500,
        on_click=executar,
    )

    caixa_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Sucesso!"),
        content = ft.Text("O arquivo foi txt foi criado"),
        actions=[
            ft.TextButton("OK", on_click=fechar_dialog)
        ]
    )

    page.add(btn_filename, label_arquivo_selecionado, entrada_nome_arquivo, label_numero_abas, selecionar_abas, entrada_nome_aba, btn_executar)
    page.update()

ft.app(target=main, assets_dir= 'assents')

