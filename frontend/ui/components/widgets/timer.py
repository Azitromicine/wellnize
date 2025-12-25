import flet as ft

class TimerWidget:
    """Виджет таймера для Wellnize."""
    
    def __init__(self, page: ft.Page):
        self.page = page
        self.is_running = False
        self.time_left = 25 * 60  # 25 минут в секундах
    
    def build(self) -> ft.Control:
        return ft.Container(
            content=ft.Row([
                ft.Icon(ft.Icons.TIMER, size=20, color=ft.Colors.BLUE_500),
                ft.Text("25:00", size=14, weight=ft.FontWeight.BOLD),
                ft.IconButton(
                    icon=ft.Icons.PLAY_ARROW,
                    icon_size=20,
                    on_click=self._toggle_timer
                )
            ], spacing=5),
            padding=ft.padding.symmetric(horizontal=10, vertical=5),
            bgcolor=ft.Colors.BLUE_50,
            border_radius=20
        )
    
    def _toggle_timer(self, e):
        self.is_running = not self.is_running
        print(f"Таймер {'запущен' if self.is_running else 'остановлен'}")