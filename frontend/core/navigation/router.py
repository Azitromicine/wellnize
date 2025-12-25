# frontend/core/navigation/router.py
import flet as ft
import asyncio

class Router:
    def __init__(self, page: ft.Page, state, ui_manager):
        self.page = page
        self.state = state
        self.ui_manager = ui_manager
        self.routes = {}
        print(f"🎯 Router инициализирован")
    
    def add_route(self, path: str, handler):
        self.routes[path] = handler
        print(f"📌 Зарегистрирован маршрут: {path}")
    
    async def navigate(self, path: str):
        print(f"📍 Навигация на: {path}")
        
        # Обновляем состояние
        self.state['app'].current_page = path
        
        # Обновляем UI через ui_manager
        if hasattr(self.ui_manager, 'update_ui_for_page'):
            await self.ui_manager.update_ui_for_page(path)
        
        if path in self.routes:
            try:
                content = self.routes[path]()
                print(f"📦 Контент страницы получен")
                
                # ВМЕСТО ЭТОГО: self.page.controls = [content]
                # ИСПОЛЬЗУЕМ: устанавливаем контент через LayoutManager
                if hasattr(self.ui_manager.ui, 'set_content'):
                    self.ui_manager.ui.set_content(content)
                    print(f"✅ Контент страницы '{path}' установлен через LayoutManager")
                else:
                    print(f"⚠️ LayoutManager не имеет метода set_content")
                    
            except Exception as e:
                print(f"❌ Ошибка загрузки страницы '{path}': {e}")
                error_content = ft.Text(f"Ошибка: {str(e)}", color="red")
                if hasattr(self.ui_manager.ui, 'set_content'):
                    self.ui_manager.ui.set_content(error_content)
        else:
            print(f"⚠️ Маршрут '{path}' не найден")