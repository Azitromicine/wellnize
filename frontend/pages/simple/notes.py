import flet as ft
from typing import Callable

def create_notes_page(on_navigate: Callable) -> ft.Control:
    return ft.Container(
        content=ft.Column([
            ft.Text("📝 Заметки", size=32, weight=ft.FontWeight.BOLD),
            ft.Text("Страница в разработке", size=16),
            ft.ElevatedButton(
                "Вернуться на дашборд",
                on_click=lambda e: on_navigate('dashboard')
            )
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20),
        expand=True,
        alignment=ft.alignment.center
    )