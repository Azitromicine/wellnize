# frontend/pages/simple/welcome.py
import flet as ft
from typing import Callable

def create_welcome_page(on_navigate: Callable) -> ft.Control:
    """
    Приветственная страница Wellnize.
    """
    return ft.Container(
        content=ft.Column([
            # Герой-секция
            ft.Container(
                content=ft.Column([
                    ft.Text(
                        "Wellnize", 
                        size=64, 
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE_700
                    ),
                    ft.Text(
                        "Ваш персональный помощник\nдля продуктивности и ментального здоровья", 
                        size=20, 
                        color=ft.Colors.GREY_700,
                        text_align=ft.TextAlign.CENTER
                    ),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                padding=ft.padding.only(bottom=60, top=40)
            ),
            
            # Карточки возможностей
            ft.Container(
                content=ft.Row([
                    _create_feature_card(
                        "🎯 Матрица Эйзенхауэра",
                        "Приоритизация задач по важности и срочности",
                        ft.Colors.BLUE_100
                    ),
                    _create_feature_card(
                        "⏱️ Таймер Pomodoro",
                        "Техника фокусированного внимания",
                        ft.Colors.GREEN_100
                    ),
                    _create_feature_card(
                        "📈 Трекер привычек", 
                        "Формирование полезных привычек",
                        ft.Colors.PURPLE_100
                    ),
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
                padding=ft.padding.only(bottom=40)
            ),
            
            # Призыв к действию
            ft.Container(
                content=ft.Column([
                    ft.Text(
                        "Начните свой путь к осознанной продуктивности",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE_800
                    ),
                    
                    ft.Container(height=20),
                    
                    ft.Row([
                        ft.ElevatedButton(
                            "Начать бесплатно",
                            icon=ft.Icons.ROCKET_LAUNCH,
                            on_click=lambda e: on_navigate('dashboard'),
                            style=ft.ButtonStyle(
                                padding=ft.padding.symmetric(horizontal=40, vertical=15),
                                bgcolor=ft.Colors.BLUE_600,
                                color=ft.Colors.WHITE
                            )
                        ),
                        ft.ElevatedButton(
                            "Узнать больше",
                            icon=ft.Icons.INFO,
                            on_click=lambda e: on_navigate('features'),
                            style=ft.ButtonStyle(
                                padding=ft.padding.symmetric(horizontal=40, vertical=15)
                            )
                        )
                    ], alignment=ft.MainAxisAlignment.CENTER, spacing=20)
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=ft.padding.only(bottom=40)
            ),
            
            # Футер
            ft.Container(
                content=ft.Text(
                    "Присоединяйтесь к тысячам пользователей, которые уже улучшили свою продуктивность",
                    size=14,
                    color=ft.Colors.GREY_600,
                    text_align=ft.TextAlign.CENTER
                ),
                padding=ft.padding.only(top=40)
            )
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, scroll=ft.ScrollMode.AUTO),
        expand=True,
        padding=40
    )

def _create_feature_card(title: str, description: str, bg_color) -> ft.Control:
    """Создает карточку функции."""
    return ft.Container(
        content=ft.Column([
            ft.Text(title, size=18, weight=ft.FontWeight.BOLD),
            ft.Container(height=10),
            ft.Text(description, size=14, color=ft.Colors.GREY_700),
        ], spacing=5),
        width=280,
        padding=20,
        bgcolor=bg_color,
        border_radius=12,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=10,
            color=ft.Colors.BLACK12
        )
    )