import flet as ft

def main(page: ft.Page):
    page.title = 'Counter'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    text_number = ft.TextField(value=0, text_align=ft.TextAlign.RIGHT, width=100)
    
    def increase(e):
        text_number.value = str(int(text_number.value)+1)
        page.update()
        
    def decrease(e):
        text_number.value = str(int(text_number.value)-1)
        page.update()
        
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=decrease),
                text_number,
                ft.IconButton(ft.icons.ADD, on_click=increase),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    
ft.app(target=main)