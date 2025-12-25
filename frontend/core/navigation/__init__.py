# frontend/core/navigation/__init__.py
from .router import Router
from .routes import (
    PUBLIC_ROUTES, PROTECTED_ROUTES, 
    check_auth_middleware, check_permissions_middleware
)

__all__ = [
    'Router',
    'PUBLIC_ROUTES', 'PROTECTED_ROUTES',
    'check_auth_middleware', 'check_permissions_middleware'
]