# frontend/ui/components/header.py (уже правильный)
import flet as ft
import asyncio
from typing import Optional, Callable

def create_header(is_authenticated: bool, 
                 user_name: Optional[str],
                 on_navigate: Callable,
                 on_logout: Callable,
                 on_toggle_sidebar: Optional[Callable] = None,
                 sidebar_expanded: bool = True) -> ft.Control:
    """
    Создает header Wellnize с кнопкой свертки sidebar.
    """
    print(f"🎨 Создаем header. Авторизован: {is_authenticated}, пользователь: {user_name}")
    
    # Логотип и название
    logo = ft.Row([
        # Кнопка ДЛЯ ВСЕХ пользователей:
        ft.IconButton(
            icon=ft.Icons.MENU if sidebar_expanded else ft.Icons.MENU_OPEN,
            icon_color=ft.Colors.BLUE_600,
            tooltip="Свернуть/развернуть меню",
            on_click=lambda e: on_toggle_sidebar() if on_toggle_sidebar else None,
        ),  # <-- УБРАТЬ `if is_authenticated else ft.Container(width=40)`
        
        ft.Icon(ft.Icons.INSIGHTS, size=28, color=ft.Colors.BLUE_600),
        ft.Text("Wellnize", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
    ], spacing=5)
    
    if is_authenticated and user_name:
        # Header для авторизованного пользователя
        user_section = ft.Row([
            ft.Text(f"👤 {user_name}", size=14, color=ft.Colors.GREY_700),
            ft.IconButton(
                icon=ft.Icons.LOGOUT,
                icon_color=ft.Colors.RED_400,
                tooltip="Выйти",
                on_click=lambda e: asyncio.create_task(on_logout())
            )
        ], spacing=15)
    else:
        # Header для гостя
        user_section = ft.Row([
            ft.ElevatedButton(
                "Войти",
                icon=ft.Icons.LOGIN,
                on_click=lambda e: asyncio.create_task(on_navigate('login')),
                style=ft.ButtonStyle(
                    bgcolor=ft.Colors.BLUE_500,
                    color=ft.Colors.WHITE
                )
            ),
            ft.TextButton(
                "Узнать больше",
                on_click=lambda e: asyncio.create_task(on_navigate('features'))
            )
        ], spacing=10)
    
    return ft.Container(
        content=ft.Row([
            logo,
            user_section
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        padding=ft.padding.symmetric(horizontal=20, vertical=15),
        bgcolor=ft.Colors.WHITE,
        border=ft.border.only(bottom=ft.border.BorderSide(1, ft.Colors.GREY_200)),
        height=60
    )