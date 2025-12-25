# frontend/app.py
import flet as ft
import asyncio
from typing import Dict, Any

class WellnizeApp:
    """
    ГЛАВНЫЙ КЛАСС ПРИЛОЖЕНИЯ WELLNIZE.
    Вся инициализация и управление здесь.
    """
    
    def __init__(self, page: ft.Page):
        self.page = page
        self._setup_page()
        
        # Core компоненты
        self.state = self._init_state()
        self.services = self._init_services()
        self.router = self._init_router()
        
        # UI компоненты
        self.ui = self._init_ui()
        
        # Инициализация страниц
        self._init_pages()
    
    def _setup_page(self):
        """Настройка Flet Page."""
        self.page.title = "Wellnize"
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.padding = 0
        self.page.spacing = 0
        self.page.window_width = 1200
        self.page.window_height = 800
        self.page.window_min_width = 800
        self.page.window_min_height = 600
    
    def _init_state(self) -> Dict[str, Any]:
        """Инициализация состояния приложения."""
        from .core.state.app import AppState
        from .core.state.auth import AuthState
        
        return {
            'app': AppState(),
            'auth': AuthState()
        }
    
    def _init_services(self):
        """Инициализация сервисов (заглушки)."""
        class ServiceContainer:
            def __init__(self):
                self.task_service = None
                self.timer_service = None
                self.user_service = None
                self.deadline_service = None
                self.notes_service = None
                self.tracker_service = None
        
        return ServiceContainer()
    
    def _init_router(self):
        """Инициализация маршрутизатора."""
        from .core.navigation.router import Router
        
        return Router(
            page=self.page,
            state=self.state,
            ui_manager=self  # Передаем себя для доступа к UI
        )
    
    def _init_ui(self):
        """Инициализация UI менеджера."""
        from .ui.layout.manager import LayoutManager
        
        return LayoutManager(self.page)
    
    def _init_pages(self):
        """Регистрация всех страниц в роутере."""
        # Простые страницы
        from .pages.simple.welcome import create_welcome_page
        from .pages.simple.dashboard import create_dashboard_page
        from .pages.simple.features import create_features_page
        from .pages.simple.deadlines import create_deadlines_page
        from .pages.simple.notes import create_notes_page
        from .pages.simple.tracker import create_tracker_page
        
        # Передаем метод navigate, а не сам роутер
        self.router.add_route('welcome', lambda: create_welcome_page(self.router.navigate))
        self.router.add_route('dashboard', lambda: create_dashboard_page(self.router.navigate))
        self.router.add_route('features', lambda: create_features_page(self.router.navigate))
        self.router.add_route('deadlines', lambda: create_deadlines_page(self.router.navigate))
        self.router.add_route('notes', lambda: create_notes_page(self.router.navigate))
        self.router.add_route('tracker', lambda: create_tracker_page(self.router.navigate))
        self.router.add_route('login', lambda: ft.Text("Страница входа (в разработке)"))
        self.router.add_route('register', lambda: ft.Text("Регистрация (в разработке)"))
        
        # Сложные страницы (MVP)
        from .pages.tasks.page import TasksPage
        
        def create_tasks_page():
            return TasksPage(
                state=self.state,
                services=self.services,
                router=self.router,
                ui=self.ui
            ).build()
        
        self.router.add_route('tasks', create_tasks_page)
    
    async def update_ui_for_page(self, page_name: str):
        """
        Обновляет UI при переходе на страницу.
        """
        print(f"🔄 Обновление UI для страницы: {page_name}")
        
        # Получаем синглтон AppState
        from .core.state.app import AppState
        app_state = AppState()
        app_state.navigate_to(page_name)
        
        # Обновляем layout
        print(f"📞 Вызов ui.update_layout()")
        self.ui.update_layout(
            page_name=page_name,
            is_authenticated=self.state['auth'].is_authenticated,
            user_name=self.state['auth'].user.get('username') if self.state['auth'].user else None,
            on_navigate=self.router.navigate,
            on_logout=self._handle_logout,
            on_toggle_sidebar=self.ui.toggle_sidebar
        )
        print(f"✅ UI обновлен")

    async def _handle_logout(self):
        """Обработчик выхода из системы."""
        self.state['auth'].logout()
        await self.router.navigate('welcome')
    
    async def _handle_login(self, username: str, password: str):
        """Обработчик входа (заглушка)."""
        self.state['auth'].login(
            user_data={'username': username, 'email': f'{username}@example.com'},
            token='fake_token'
        )
        await self.router.navigate('dashboard')
    
    async def start(self):
        """Запуск приложения."""
        print("✅ Wellnize инициализирован")
        print(f"📱 Доступные страницы: {list(self.router.routes.keys())}")
        
        # Всегда начинаем с welcome для тестирования
        await self.router.navigate('welcome')
        
