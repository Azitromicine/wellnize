# frontend/ui/layout/manager.py
import flet as ft
from typing import Optional, Callable
import sys
import os

# Добавляем путь для абсолютных импортов
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

class LayoutManager:
    def __init__(self, page: ft.Page, app_state=None):
        self.page = page
        print("🎯 LayoutManager создан")
        
        # Получаем синглтон AppState
        from ...core.state.app import AppState
        self.app_state = app_state or AppState()
        
        # Создаем основные области
        self.header = None
        self.sidebar = None
        self.content_area = ft.Container(expand=True)
        
        # Синхронизируем состояние sidebar с AppState
        self.is_sidebar_expanded = self.app_state.sidebar_expanded
        self.sidebar_min_width = 80
        self.sidebar_max_width = 250
        
        # Контекст для обновления sidebar
        self._current_page = self.app_state.current_page
        self._navigation_callback = None
        self._is_authenticated = False
        
        # Сразу строим layout
        self._build_base_layout()
    
    def _build_base_layout(self):
        """Строит базовую структуру layout с переменным sidebar."""
        print("🔨 Строим базовый layout...")
        
        # Создаем области как контейнеры
        self.header_area = ft.Container()
        self.sidebar_area = ft.Container()
        
        layout = ft.Column([
            self.header_area,
            ft.Row([
                self.sidebar_area,
                ft.VerticalDivider(width=1, color=ft.Colors.GREY_300),
                self.content_area
            ], expand=True, spacing=0)
        ], expand=True, spacing=0)
        
        self.page.add(layout)
        print(f"✅ Layout добавлен на страницу. Контролов: {len(self.page.controls)}")
    
    def update_layout(self, 
                     page_name: str,
                     is_authenticated: bool,
                     user_name: Optional[str] = None,
                     on_navigate: Optional[Callable] = None,
                     on_logout: Optional[Callable] = None,
                     on_toggle_sidebar: Optional[Callable] = None):
        """
        Обновляет layout при переходе на страницу.
        """
        print(f"🎨 Обновление layout для страницы: {page_name}")
        
        # Сохраняем контекст для toggle_sidebar
        self._current_page = page_name
        self._navigation_callback = on_navigate
        self._is_authenticated = is_authenticated
        
        # Обновляем AppState
        self.app_state.current_page = page_name
        
        # Обновляем header с кнопкой свертки
        self.header_area.content = self._create_header(
            is_authenticated, 
            user_name, 
            on_navigate, 
            on_logout,
            on_toggle_sidebar or self.toggle_sidebar,
            self.is_sidebar_expanded
        )
        
        # Обновляем sidebar
        self.sidebar_area.content = self._create_sidebar(
            is_authenticated, 
            page_name, 
            on_navigate,
            self.is_sidebar_expanded
        )
        
        self.page.update()
    
    def _create_header(self, is_authenticated: bool, user_name: Optional[str],
                      on_navigate: Callable, on_logout: Callable,
                      on_toggle_sidebar: Callable,
                      sidebar_expanded: bool) -> ft.Control:
        """Создает header с кнопкой свертки sidebar."""
        from ..components.header import create_header
        return create_header(
            is_authenticated, 
            user_name, 
            on_navigate, 
            on_logout,
            on_toggle_sidebar,
            sidebar_expanded
        )
    
    def _create_sidebar(self, is_authenticated: bool, current_page: str,
                       on_navigate: Callable, expanded: bool = True) -> ft.Control:
        """Создает sidebar в свернутом или развернутом состоянии."""
        from ..components.sidebar import create_sidebar
        return create_sidebar(
            is_authenticated, 
            current_page, 
            on_navigate,
            expanded
        )
    
    def toggle_sidebar(self, e=None):
        """Переключение состояния sidebar."""
        # Переключаем состояние
        self.is_sidebar_expanded = not self.is_sidebar_expanded
        self.app_state.sidebar_expanded = self.is_sidebar_expanded
        
        print(f"🔄 LayoutManager: sidebar {'развернут' if self.is_sidebar_expanded else 'свернут'}")
        
        # Обновляем sidebar с новым состоянием
        if self.sidebar_area.content:
            self.sidebar_area.content = self._create_sidebar(
                self._is_authenticated,
                self._current_page,
                self._navigation_callback,
                self.is_sidebar_expanded
            )
        
        self.page.update()
        return self.is_sidebar_expanded
    
    # Убраны set_sidebar_state и toggle_sidebar_animation как дублирующие функциональность
    
    def set_content(self, content: ft.Control):
        """Устанавливает основной контент (вызывается роутером)."""
        print(f"📥 Установка контента в content_area")
        self.content_area.content = content
        self.page.update()
    
    def show_loading(self, message: str = "Загрузка..."):
        """Показывает индикатор загрузки."""
        self.app_state.is_loading = True
        self.content_area.content = ft.Column([
            ft.ProgressRing(),
            ft.Text(message, size=16)
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20)
        self.page.update()
    
    def hide_loading(self):
        """Скрывает индикатор загрузки."""
        self.app_state.is_loading = False
    
    def show_error(self, message: str, on_retry: Optional[Callable] = None):
        """Показывает сообщение об ошибке."""
        self.app_state.add_notification(message, "error")
        
        content = [
            ft.Icon(ft.icons.ERROR_OUTLINE, size=48, color="red"),
            ft.Text("Ошибка", size=20, weight=ft.FontWeight.BOLD),
            ft.Text(message, size=16, text_align=ft.TextAlign.CENTER),
        ]
        
        if on_retry:
            content.append(
                ft.ElevatedButton("Повторить", on_click=lambda e: on_retry())
            )
        
        self.content_area.content = ft.Column(
            content,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
        self.page.update()
    
    def sync_with_app_state(self):
        """Синхронизирует состояние с AppState (опционально)."""
        self.is_sidebar_expanded = self.app_state.sidebar_expanded
        # При необходимости можно добавить другие поля