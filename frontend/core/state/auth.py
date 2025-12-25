# frontend/core/state/auth.py
class AuthState:
    """Состояние авторизации (совместимость со старой структурой)."""
    
    def __init__(self):
        self.is_authenticated = False
        self.user = None
        print("🔐 AuthState инициализирован (legacy)")
    
    def login(self, user_data: dict, token: str):
        """Авторизация пользователя."""
        # Синхронизируем с AppState синглтоном
        from .app import AppState
        app_state = AppState()
        app_state.login(user_data, token)
        
        # И локально сохраняем для обратной совместимости
        self.is_authenticated = True
        self.user = user_data
        print(f"🔑 AuthState: пользователь {user_data.get('username')} авторизован")
    
    def logout(self):
        """Выход пользователя."""
        # Синхронизируем с AppState синглтоном
        from .app import AppState
        app_state = AppState()
        app_state.logout()
        
        # И локально очищаем для обратной совместимости
        self.is_authenticated = False
        self.user = None
        print("👋 AuthState: пользователь вышел")
    
    @property
    def username(self):
        """Имя пользователя для обратной совместимости."""
        return self.user.get('username') if self.user else None