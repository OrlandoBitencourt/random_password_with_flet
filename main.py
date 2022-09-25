from subprocess import CalledProcessError
from generate_password import generate_random_password
from copy_to_clipboard import copy2clip

from flet import Page, app, Row, Text, Checkbox, ElevatedButton, TextField, IconButton, icons, theme
import flet


def main(page: Page):
    page.window_width = 600    
    page.window_height = 600
    page.title = "Gerador de senha aleatoria"
    page.horizontal_alignment = "center"
    page.vertical_alignment="center"  
    page.theme_mode = "dark"
    page.update()

    def generate_pwd(e):
        pwd_lenght = 0
        try:
            pwd_lenght = int(field_lenght.value)
        except:
            output_error.value = "O tamanho da senha precisa ser numerico."
            output_error.color = "red"
            output_error.visible = True
        
        if pwd_lenght <= 0:
            output_error.value = "O tamanho da senha precisa ser maior e maior que 0."
            output_error.color = "red"
            output_error.visible = True
        else:
            if not checkbox_letters.value and not checkbox_digits.value and not checkbox_symbols.value:
                output_error.value = "Ao menos uma das opcões de senhas deve estar selecionada."
                output_error.color = "red"
                output_error.visible = True
            else:
                while True:
                    pwd = generate_random_password(pwd_lenght, checkbox_letters.value, checkbox_digits.value, checkbox_symbols.value)
                    output_password.value = pwd
                    output_password.color = "blue"
                    
                    output_error.visible = True
                    output_error.color = "green"
                    output_error.value = "Senha gerada com sucesso e copiada."
                    
                    try:
                        copy2clip(pwd)
                    except CalledProcessError:
                        continue
                    
                    break
                
        page.update()
        
    def minus_click(e):
        field_lenght.value = int(field_lenght.value) - 1
        page.update()

    def plus_click(e):
        field_lenght.value = int(field_lenght.value) + 1
        page.update()
        
    field_lenght = TextField(value="20", text_align="right", width=100, border_color="white")

    checkbox_letters = Checkbox(label="Senha com letras", value=True)

    checkbox_digits = Checkbox(label="Senha com números", value=True)

    checkbox_symbols = Checkbox(label="Senha com símbolos", value=True)

    output_password = TextField(value="", border_color="white")

    output_error = Text("output", visible=False)

    button_generate = ElevatedButton(text="     Gerar senha     ", on_click=generate_pwd)

    page.add(
        Row([Text("Selecione o tamanho da senha:", size=20)], alignment="center"),
        Row(
            [
                IconButton(icons.REMOVE, on_click=minus_click), 
                field_lenght, 
                IconButton(icons.ADD, on_click=plus_click),
            ],
            alignment="center",
        ),
        
        Row([Text(" ", size=8)], alignment="center"),
        Row([Text("Opções de caracteres:", size=18)], alignment="center"),
        Row([checkbox_letters],  alignment="center"),
        Row([checkbox_digits],  alignment="center"),
        Row([checkbox_symbols],  alignment="center"),
        
        Row([Text(" ", size=8)], alignment="center"),
        Row([Text("Senha:", size=18)], alignment="center"),        
        Row([output_password], alignment="center"),
        Row([output_error], alignment="center"),
        Row([button_generate], alignment="center"),
    )

flet.app(target=main)
