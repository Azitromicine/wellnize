# tests/integration/test_sidebar_integration.py
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

def test_sidebar_toggle_in_real_app():
    """Тест интеграции sidebar в реальном приложении."""
    import flet as ft
    from frontend.ui.layout.manager import LayoutManager
    
    class MockPage:
        def __init__(self):
            self.controls = []
            self.update_called = False
        
        def add(self, control):
            self.controls.append(control)
        
        def update(self):
            self.update_called = True
    
    # 1. Создаем LayoutManager
    mock_page = MockPage()
    layout_manager = LayoutManager(mock_page)
    
    # 2. Имитируем настройку для авторизованного пользователя
    layout_manager.update_layout(
        page_name="dashboard",
        is_authenticated=True,
        user_name="test_user",
        on_navigate=lambda x: print(f"Navigate: {x}"),
        on_logout=lambda: print("Logout"),
        on_toggle_sidebar=layout_manager.toggle_sidebar
    )
    
    # 3. Проверяем начальное состояние
    sidebar = layout_manager.sidebar_area.content
    assert sidebar.width == 250, f"Начальная ширина должна быть 250, а не {sidebar.width}"
    assert layout_manager.is_sidebar_expanded == True, "Начальное состояние должно быть развернуто"
    
    # 4. Сворачиваем
    layout_manager.toggle_sidebar()
    
    # 5. Проверяем свернутое состояние
    sidebar = layout_manager.sidebar_area.content
    assert sidebar.width == 80, f"Свернутая ширина должна быть 80, а не {sidebar.width}"
    assert layout_manager.is_sidebar_expanded == False, "Должно быть свернуто"
    
    print("✅ Интеграция sidebar работает корректно")
    return True

if __name__ == "__main__":
    test_sidebar_toggle_in_real_app()