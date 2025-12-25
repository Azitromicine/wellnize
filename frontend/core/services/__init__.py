# frontend/core/services/__init__.py
"""
Контейнер сервисов Wellnize.
"""
import asyncio
from typing import Optional, Callable

class ServiceContainer:
    """Контейнер всех сервисов Wellnize."""
    
    def __init__(self, base_url: str = "http://localhost:8000/api"):
        self.base_url = base_url
        self._get_token_callback: Optional[Callable] = None
        
        # Сервисы будут инициализированы позже
        self.task_service = None
        self.timer_service = None
        self.user_service = None
        self.deadline_service = None
        self.notes_service = None
        self.tracker_service = None
        self.auth_service = None
    
    def set_token_callback(self, callback: Callable):
        """Устанавливает callback для получения токена."""
        self._get_token_callback = callback
    
    async def initialize(self):
        """Инициализация всех сервисов."""
        print("🔄 Инициализация сервисов Wellnize...")
        
        # Здесь будет реальная инициализация сервисов
        # Пока создаем заглушки
        
        class TaskService:
            async def get_tasks(self):
                await asyncio.sleep(0.5)
                return [
                    {"id": 1, "title": "Пример задачи", "completed": False},
                    {"id": 2, "title": "Другая задача", "completed": True}
                ]
        
        class TimerService:
            def start_timer(self, duration: int):
                print(f"⏱️ Таймер запущен на {duration} минут")
        
        self.task_service = TaskService()
        self.timer_service = TimerService()
        
        print("✅ Сервисы Wellnize инициализированы")
    
    async def cleanup(self):
        """Очистка ресурсов сервисов."""
        print("🧹 Очистка сервисов Wellnize...")
        # Здесь будет закрытие соединений и т.д.

__all__ = ['ServiceContainer']