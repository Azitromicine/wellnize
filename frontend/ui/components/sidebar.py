# frontend/ui/components/sidebar.py
import flet as ft
import asyncio
from typing import Callable

def create_sidebar(is_authenticated: bool,
                  current_page: str,
                  on_navigate: Callable,
                  expanded: bool = True) -> ft.Control:
    """
    Создает sidebar Wellnize в свернутом или развернутом состоянии.
    Для Flet 0.80.0+ с правильной анимацией.
    """
    # Создаем alignment объекты для Flet 0.80.0+
    center_alignment = ft.alignment.Alignment(0, 0)      # x=0, y=0 - центр
    top_left_alignment = ft.alignment.Alignment(-1, -1)  # x=-1, y=-1 - верхний левый угол
    
    if is_authenticated:
        # Навигация для авторизованных пользователей
        nav_items = [
            _create_nav_item("🏠", "Дашборд", "dashboard", current_page, on_navigate, expanded),
            _create_nav_item("✅", "Задачи", "tasks", current_page, on_navigate, expanded),
            _create_nav_item("⏰", "Дедлайны", "deadlines", current_page, on_navigate, expanded),
            _create_nav_item("📝", "Заметки", "notes", current_page, on_navigate, expanded),
            _create_nav_item("📈", "Трекер", "tracker", current_page, on_navigate, expanded),
            ft.Divider(height=20) if expanded else ft.Divider(height=10),
            _create_nav_item("⚙️", "Настройки", "settings", current_page, on_navigate, expanded),
            _create_nav_item("ℹ️", "О Wellnize", "features", current_page, on_navigate, expanded),
        ]
    else:
        # Навигация для гостей
        nav_items = [
            _create_nav_item("ℹ️", "О приложении", "features", current_page, on_navigate, expanded)
        ]
    

    return ft.Container(
        content=ft.Column([
            # ЗАГОЛОВОК ТОЛЬКО В РАЗВЕРНУТОМ СОСТОЯНИИ
            *([
                ft.Container(
                    content=ft.Text("Меню", size=16, weight=ft.FontWeight.BOLD),
                    padding=ft.padding.only(left=15, top=20, bottom=10),
                    alignment=top_left_alignment
                )
            ] if expanded else []),
            
            *nav_items
        ], 
        spacing=0,
        horizontal_alignment=(
            ft.CrossAxisAlignment.CENTER if not expanded 
            else ft.CrossAxisAlignment.STRETCH
        )),
        width=250 if expanded else 80,
        bgcolor=ft.Colors.GREY_50,
        border=ft.border.only(right=ft.border.BorderSide(1, ft.Colors.GREY_200)),
        animate=ft.Animation(duration=300, curve=ft.AnimationCurve.EASE_IN_OUT)
    )

def _create_nav_item(icon: str, text: str, page: str, 
                    current_page: str, on_navigate: Callable,
                    expanded: bool = True, is_authenticated: bool = True) -> ft.Control:
    """Создает элемент навигации."""
    is_active = current_page == page
    
    if expanded:
        # Полный вид с текстом (используем эмодзи как текст)
        content = ft.ListTile(
            leading=ft.Text(icon, size=18),
            title=ft.Text(
                text, 
                size=14,
                weight=ft.FontWeight.BOLD if is_active else None,
                color=ft.Colors.BLUE_700 if is_active else ft.Colors.GREY_700
            ),
            on_click=lambda e: asyncio.create_task(on_navigate(page)),
            selected=is_active,
            dense=True,
        )
        
        container = ft.Container(
            content=content,
            bgcolor=ft.Colors.BLUE_50 if is_active else None,
            border_radius=5,
            margin=ft.margin.symmetric(horizontal=10, vertical=2)
        )
    else:
        icon_mapping_auth = {
            "🏠": ft.Icons.HOME,
            "✅": ft.Icons.TASK_ALT,               
            "⏰": ft.Icons.ACCESS_TIME,            
            "📝": ft.Icons.NOTE_ADD,               
            "📈": ft.Icons.TRENDING_UP,            
            "⚙️": ft.Icons.SETTINGS,               
            "ℹ️": ft.Icons.INFO,                    
        }
        
        icon_mapping_guest = {
            "ℹ️": ft.Icons.INFO,
        }
        
        # ВЫБИРАЕМ ПРАВИЛЬНЫЙ МАППИНГ
        if is_authenticated:
            flet_icon = icon_mapping_auth.get(icon, ft.Icons.QUESTION_MARK)
        else:
            # Для гостей только одна иконка INFO
            flet_icon = icon_mapping_guest.get(icon, ft.Icons.QUESTION_MARK)
        
        container = ft.Container(
            content=ft.IconButton(
                icon=flet_icon,
                icon_size=20,
                tooltip=text,
                on_click=lambda e: asyncio.create_task(on_navigate(page)),
                style=ft.ButtonStyle(
                    color=ft.Colors.BLUE_600 if is_active else ft.Colors.GREY_600,
                    bgcolor=ft.Colors.BLUE_50 if is_active else None,
                )
            ),
            margin=ft.margin.symmetric(vertical=4),
            alignment=ft.alignment.Alignment(0, 0)
        )
    
    return container