import flet as ft
from typing import Dict, Any, Callable

class TasksPage:
    """Страница задач Wellnize (MVP)."""
    
    def __init__(self, state: Dict[str, Any], services, router, ui):
        self.state = state
        self.services = services
        self.router = router
        self.ui = ui
    
    def build(self) -> ft.Control:
        return ft.Container(
            content=ft.Column([
                ft.Text("✅ Задачи Wellnize", size=32, weight=ft.FontWeight.BOLD),
                ft.Text("Страница в разработке (MVP)", size=16),
                ft.ElevatedButton(
                    "Вернуться на дашборд",
                    on_click=lambda e: self.router.navigate('dashboard')
                )
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20),
            expand=True,
            alignment=ft.alignment.center
        )