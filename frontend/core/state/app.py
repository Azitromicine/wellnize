# frontend/core/state/app.py
class SingletonMeta(type):
    """
    Метакласс для создания синглтонов.
    Гарантирует, что у класса будет только один экземпляр.
    """
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        # Если экземпляр еще не создан - создаем
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
            print(f"✅ Создан новый экземпляр {cls.__name__} (синглтон)")
        return cls._instances[cls]

class AppState(metaclass=SingletonMeta):
    """Глобальное состояние Wellnize (синглтон)."""
    
    def __init__(self):
        # Защита от повторной инициализации
        if not hasattr(self, '_initialized'):
            self.current_page = "welcome"
            self.previous_page = None
            self.theme = "light"  # 'light' или 'dark'
            self.is_loading = False
            self.sidebar_expanded = True
            self.notifications = []
            self._current_user = None
            self._auth_token = None
            self._initialized = True
            print("🎮 AppState инициализирован")
    
    @property
    def is_authenticated(self) -> bool:
        """Проверяет, авторизован ли пользователь."""
        return self._auth_token is not None and self._current_user is not None
    
    @property
    def user(self) -> dict:
        """Возвращает данные текущего пользователя."""
        return self._current_user or {}
    
    def login(self, user_data: dict, token: str):
        """Авторизация пользователя."""
        self._current_user = user_data
        self._auth_token = token
        print(f"🔑 Пользователь {user_data.get('username', 'Unknown')} авторизован")
    
    def logout(self):
        """Выход пользователя."""
        print(f"👋 Пользователь {self.user.get('username', 'Unknown')} вышел")
        self._current_user = None
        self._auth_token = None
        self.notifications.clear()
    
    def navigate_to(self, page_name: str):
        """Переход на страницу."""
        self.previous_page = self.current_page
        self.current_page = page_name
        print(f"📍 Навигация: {self.previous_page} → {self.current_page}")
    
    def toggle_theme(self):
        """Переключение темы."""
        self.theme = "dark" if self.theme == "light" else "light"
        print(f"🎨 Тема переключена на: {self.theme}")
        return self.theme
    
    def toggle_sidebar(self):
        """Переключение боковой панели."""
        self.sidebar_expanded = not self.sidebar_expanded
        print(f"📌 Sidebar: {'развернут' if self.sidebar_expanded else 'свернут'}")
        return self.sidebar_expanded
    
    def add_notification(self, message: str, level: str = "info"):
        """Добавляет уведомление."""
        notification = {
            "id": len(self.notifications) + 1,
            "message": message,
            "level": level,  # 'info', 'success', 'warning', 'error'
            "timestamp": "now"  # В реальном приложении используйте datetime
        }
        self.notifications.append(notification)
        print(f"🔔 Добавлено уведомление: {message}")
    
    def clear_notifications(self):
        """Очищает все уведомления."""
        self.notifications.clear()
        print("🧹 Уведомления очищены")
    
    def __str__(self):
        """Строковое представление состояния."""
        return (f"AppState(page={self.current_page}, "
                f"theme={self.theme}, "
                f"sidebar={'expanded' if self.sidebar_expanded else 'collapsed'}, "
                f"user={'authenticated' if self.is_authenticated else 'guest'})")