# frontend/pages/simple/dashboard.py
import flet as ft
from typing import Callable

def create_dashboard_page(on_navigate: Callable) -> ft.Control:
    """Дашборд Wellnize."""
    return ft.Container(
        content=ft.Column([
            ft.Text("📊 Дашборд", size=32, weight=ft.FontWeight.BOLD),
            ft.Text("Обзор вашей продуктивности", size=16, color=ft.Colors.GREY_600),
            
            ft.Container(height=30),
            
            # Статистика
            ft.Row([
                _create_stat_card("✅", "Активные задачи", "12", ft.Colors.BLUE_500, 
                                lambda e: on_navigate('tasks')),
                _create_stat_card("⏰", "Ближайшие дедлайны", "3", ft.Colors.ORANGE_500,
                                lambda e: on_navigate('deadlines')),
                _create_stat_card("📝", "Заметки", "8", ft.Colors.GREEN_500,
                                lambda e: on_navigate('notes')),
                _create_stat_card("🔥", "Дней подряд", "14", ft.Colors.RED_500,
                                lambda e: on_navigate('tracker')),
            ], spacing=20),
            
            ft.Container(height=30),
            
            # Быстрый доступ
            ft.Container(
                content=ft.Column([
                    ft.Text("Быстрый доступ", size=20, weight=ft.FontWeight.BOLD),
                    ft.Container(height=10),
                    ft.Row([
                        ft.ElevatedButton(
                            "➕ Новая задача",
                            icon=ft.Icons.ADD,
                            on_click=lambda e: on_navigate('tasks'),
                            style=ft.ButtonStyle(
                                bgcolor=ft.Colors.BLUE_100,
                                color=ft.Colors.BLUE_700
                            )
                        ),
                        ft.ElevatedButton(
                            "📅 Календарь",
                            icon=ft.Icons.CALENDAR_MONTH,
                            on_click=lambda e: print("Календарь"),
                        ),
                        ft.ElevatedButton(
                            "📊 Отчеты",
                            icon=ft.Icons.BAR_CHART,
                            on_click=lambda e: print("Отчеты"),
                        ),
                    ], spacing=10)
                ]),
                padding=20,
                bgcolor=ft.Colors.GREY_50,
                border_radius=10
            ),
            
            # Советы
            ft.Container(
                content=ft.Column([
                    ft.Text("💡 Советы на сегодня", size=20, weight=ft.FontWeight.BOLD),
                    ft.Container(height=10),
                    ft.Text("• Начните день с определения 3 главных задач"),
                    ft.Text("• Используйте технику Pomodoro для фокусировки"),
                    ft.Text("• Сделайте 5-минутную паузу каждый час"),
                ]),
                padding=20,
                bgcolor=ft.Colors.BLUE_50,
                border_radius=10,
                margin=ft.margin.only(top=30)
            )
        ]),
        expand=True,
        padding=30
    )

def _create_stat_card(icon: str, title: str, value: str, color, on_click=None) -> ft.Control:
    """Создает карточку статистики."""
    return ft.Container(
        content=ft.Column([
            ft.Text(icon, size=24),
            ft.Text(title, size=12, color=ft.Colors.GREY_600),
            ft.Text(value, size=28, weight=ft.FontWeight.BOLD),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
        width=150,
        padding=20,
        bgcolor=ft.Colors.WHITE,
        border_radius=10,
        shadow=ft.BoxShadow(blur_radius=5, color=ft.Colors.BLACK12),
        border=ft.border.all(2, color),
        on_click=on_click if on_click else None
    )