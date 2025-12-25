# frontend/core/__init__.py
"""
Ядро Wellnize.
"""
from .state import AppState, AuthState
from .navigation import Router
from .services import ServiceContainer

__all__ = [
    'AppState', 'AuthState',
    'Router', 'ServiceContainer'
]