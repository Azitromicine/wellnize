import flet as ft
from typing import Callable

def create_features_page(on_navigate: Callable) -> ft.Control:
    return ft.Container(
        content=ft.Column([
            ft.Text("🚀 Возможности Wellnize", size=32, weight=ft.FontWeight.BOLD),
            ft.Text("Все инструменты для продуктивности в одном месте", size=16),
            
            ft.Container(height=30),
            
            ft.Column([
                _create_feature("✅ Управление задачами", "Матрица Эйзенхауэра, приоритеты, теги"),
                _create_feature("⏱️ Таймер Pomodoro", "Фокус-сессии, перерывы, статистика"),
                _create_feature("📝 Умные заметки", "Быстрые записи, категории, поиск"),
                _create_feature("📅 Трекер дедлайнов", "Напоминания, календарь, уведомления"),
                _create_feature("📈 Аналитика привычек", "Графики, отчеты, цели"),
                _create_feature("🏆 Геймификация", "Очки, достижения, уровни"),
                _create_feature("🔔 Умные уведомления", "Персональные напоминания"),
                _create_feature("🌙 Дневник настроения", "Отслеживание эмоций"),
            ], spacing=10),
            
            ft.Container(height=30),
            
            ft.ElevatedButton(
                "Начать использовать",
                on_click=lambda e: on_navigate('dashboard'),
                style=ft.ButtonStyle(
                    padding=ft.padding.symmetric(horizontal=40, vertical=15),
                    bgcolor=ft.Colors.BLUE_600,
                    color=ft.Colors.WHITE
                )
            )
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20),
        expand=True,
        padding=40
    )

def _create_feature(title: str, description: str) -> ft.Control:
    return ft.Container(
        content=ft.Row([
            ft.Icon(ft.Icons.CHECK_CIRCLE, color=ft.Colors.GREEN_500, size=20),
            ft.Column([
                ft.Text(title, size=16, weight=ft.FontWeight.BOLD),
                ft.Text(description, size=14, color=ft.Colors.GREY_600),
            ], spacing=2)
        ], spacing=10),
        padding=ft.padding.symmetric(vertical=5),
        width=500
    )