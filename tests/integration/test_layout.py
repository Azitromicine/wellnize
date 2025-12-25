# tests/integration/test_layout.py
import sys
import os
import flet as ft

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

class TestLayoutIntegration:
    """Интеграционные тесты для LayoutManager."""
    
    def test_layout_manager_creation(self):
        """Тест создания LayoutManager."""
        print("\n🧪 Тест создания LayoutManager")
        
        # Создаем mock страницу
        class MockPage:
            def __init__(self):
                self.controls = []
                self.updates = 0
            
            def add(self, control):
                self.controls.append(control)
            
            def update(self):
                self.updates += 1
        
        mock_page = MockPage()
        
        from frontend.ui.layout.manager import LayoutManager
        
        layout_manager = LayoutManager(mock_page)
        
        assert layout_manager is not None, \
            "LayoutManager должен создаваться"
        assert len(mock_page.controls) == 1, \
            f"На страницу должен добавиться 1 контроль, добавлено: {len(mock_page.controls)}"
        
        print("✅ LayoutManager создается корректно")
        return True
    
    def test_sidebar_toggle_integration(self):
        """Тест интеграции переключения sidebar."""
        print("\n🧪 Тест интеграции sidebar")
        
        from frontend.core.state.app import AppState
        from frontend.ui.components.sidebar import create_sidebar
        
        # Получаем синглтон
        app_state = AppState()
        
        # Создаем sidebar в развернутом состоянии
        sidebar_expanded = create_sidebar(
            is_authenticated=True,
            current_page="dashboard",
            on_navigate=lambda x: print(f"Навигация: {x}"),
            expanded=True
        )
        
        assert sidebar_expanded.width == 250, \
            f"Развернутый sidebar должен иметь ширину 250, имеет: {sidebar_expanded.width}"
        
        # Создаем sidebar в свернутом состоянии
        sidebar_collapsed = create_sidebar(
            is_authenticated=True,
            current_page="dashboard",
            on_navigate=lambda x: print(f"Навигация: {x}"),
            expanded=False
        )
        
        assert sidebar_collapsed.width == 80, \
            f"Свернутый sidebar должен иметь ширину 80, имеет: {sidebar_collapsed.width}"
        
        print("✅ Sidebar корректно меняет размер")
        return True

def run_tests():
    """Запускает все тесты в этом файле."""
    print("=" * 60)
    print("🚀 ИНТЕГРАЦИОННЫЕ ТЕСТЫ LAYOUT")
    print("=" * 60)
    
    test_suite = TestLayoutIntegration()
    passed = 0
    total = 0
    
    test_methods = [
        test_suite.test_layout_manager_creation,
        test_suite.test_sidebar_toggle_integration,
    ]
    
    for test_method in test_methods:
        total += 1
        try:
            if test_method():
                passed += 1
            else:
                print(f"❌ {test_method.__name__} не прошел")
        except AssertionError as e:
            print(f"❌ {test_method.__name__}: {e}")
        except Exception as e:
            print(f"💥 {test_method.__name__}: {e}")
    
    print(f"\n📊 Результат: {passed}/{total} тестов пройдено")
    
    if passed == total:
        print("✅ Все интеграционные тесты пройдены!")
    else:
        print(f"⚠️ {total - passed} тестов не пройдено")
    
    return passed == total

# Функция для автоматического запуска
def run_all_tests():
    """Алиас для совместимости."""
    return run_tests()

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)