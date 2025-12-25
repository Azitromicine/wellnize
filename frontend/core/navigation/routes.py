# frontend/core/navigation/routes.py
"""
Конфигурация маршрутов Wellnize.
"""
from typing import List, Dict, Any

# Публичные маршруты (доступны без авторизации)
PUBLIC_ROUTES = ['welcome', 'features', 'login', 'register']

# Защищенные маршруты (требуют авторизации)
PROTECTED_ROUTES = [
    'dashboard', 'tasks', 'deadlines', 'notes', 
    'tracker', 'profile', 'settings'
]

# Роли и разрешения
ROUTE_PERMISSIONS = {
    'admin': ['settings', 'users', 'analytics'],
    'user': ['dashboard', 'tasks', 'deadlines', 'notes', 'tracker', 'profile']
}

def check_auth_middleware(path: str, state: Dict[str, Any]) -> str:
    """
    Middleware для проверки авторизации.
    Если пользователь не авторизован и пытается попасть на защищенную страницу,
    перенаправляем на welcome.
    """
    from ..state.auth import AuthState
    
    auth_state: AuthState = state['auth']
    
    if path in PROTECTED_ROUTES and not auth_state.is_authenticated:
        print(f"🚫 Доступ запрещен: {path} (требуется авторизация)")
        return 'welcome'
    
    return path

def check_permissions_middleware(path: str, state: Dict[str, Any]) -> str:
    """
    Middleware для проверки прав доступа.
    """
    from ..state.auth import AuthState
    
    auth_state: AuthState = state['auth']
    
    if auth_state.is_authenticated:
        # Проверяем разрешения для роли пользователя
        user_role = auth_state.user.get('role', 'user')
        allowed_routes = ROUTE_PERMISSIONS.get(user_role, [])
        
        if path not in allowed_routes and path not in PUBLIC_ROUTES:
            print(f"🚫 Нет прав для доступа к: {path}")
            return 'dashboard'  # Перенаправляем на dashboard
    
    return path