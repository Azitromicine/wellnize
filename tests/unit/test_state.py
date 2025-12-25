# tests/unit/test_state.py
import sys
import os

# Добавляем путь к проекту для импортов
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from frontend.core.state.app import AppState

class TestAppStateSingleton:
    """Тесты для синглтона AppState."""
    
    def test_singleton_property(self):
        """Проверяем, что AppState действительно синглтон."""
        print("\n🧪 Тест синглтона AppState")
        
        # Создаем несколько "экземпляров"
        state1 = AppState()
        state2 = AppState()
        state3 = AppState()
        
        # Проверяем, что это один и тот же объект
        assert state1 is state2, "state1 и state2 должны быть одним объектом"
        assert state2 is state3, "state2 и state3 должны быть одним объектом"
        assert id(state1) == id(state2) == id(state3), "Все ID должны совпадать"
        
        print("✅ Все объекты - один и тот же синглтон")
    
    def test_state_persistence(self):
        """Проверяем сохранение состояния."""
        print("\n🧪 Тест сохранения состояния")
        
        state1 = AppState()
        state2 = AppState()
        
        # Меняем через state1
        original_page = state1.current_page
        state1.current_page = "dashboard"
        
        # Проверяем через state2
        assert state2.current_page == "dashboard", \
            f"Ожидалось 'dashboard', получено '{state2.current_page}'"
        
        # Возвращаем исходное состояние
        state1.current_page = original_page
        
        print("✅ Состояние сохраняется между экземплярами")
    
    def test_sidebar_toggle(self):
        """Тестируем переключение sidebar."""
        print("\n🧪 Тест переключения sidebar")
        
        state = AppState()
        original_state = state.sidebar_expanded
        
        # Переключаем
        new_state = state.toggle_sidebar()
        
        assert state.sidebar_expanded == (not original_state), \
            f"Sidebar должен переключиться с {original_state} на {not original_state}"
        assert state.sidebar_expanded == new_state, \
            f"Метод должен возвращать новое состояние"
        
        # Возвращаем в исходное
        state.toggle_sidebar()
        
        print("✅ Переключение sidebar работает корректно")
    
    def test_navigation(self):
        """Тестируем навигацию."""
        print("\n🧪 Тест навигации")
        
        state = AppState()
        original_page = state.current_page
        
        # Навигация на новую страницу
        state.navigate_to("dashboard")
        
        assert state.current_page == "dashboard", \
            f"Текущая страница должна быть 'dashboard'"
        assert state.previous_page == original_page, \
            f"Предыдущая страница должна быть '{original_page}'"
        
        # Возвращаемся
        state.navigate_to(original_page)
        
        print("✅ Навигация работает корректно")
    
    def test_authentication(self):
        """Тестируем авторизацию."""
        print("\n🧪 Тест авторизации")
        
        state = AppState()
        
        # Проверяем начальное состояние
        assert not state.is_authenticated, \
            "По умолчанию пользователь не авторизован"
        assert state.user == {}, \
            "По умолчанию данные пользователя пустые"
        
        # Логинимся
        test_user = {"username": "test_user", "email": "test@example.com"}
        test_token = "test_token_123"
        
        state.login(test_user, test_token)
        
        assert state.is_authenticated, \
            "После login пользователь должен быть авторизован"
        assert state.user["username"] == "test_user", \
            "Данные пользователя должны сохраниться"
        
        # Логаут
        state.logout()
        
        assert not state.is_authenticated, \
            "После logout пользователь не должен быть авторизован"
        assert state.user == {}, \
            "После logout данные пользователя должны очиститься"
        
        print("✅ Авторизация работает корректно")

def run_all_tests():
    """Запускает все тесты."""
    print("=" * 50)
    print("🚀 ЗАПУСК ТЕСТОВ AppState")
    print("=" * 50)
    
    test_suite = TestAppStateSingleton()
    
    # Список методов тестов
    test_methods = [
        test_suite.test_singleton_property,
        test_suite.test_state_persistence,
        test_suite.test_sidebar_toggle,
        test_suite.test_navigation,
        test_suite.test_authentication,
    ]
    
    passed = 0
    failed = 0
    
    for test_method in test_methods:
        try:
            test_method()
            passed += 1
        except AssertionError as e:
            failed += 1
            print(f"❌ {test_method.__name__} не прошел: {e}")
        except Exception as e:
            failed += 1
            print(f"💥 {test_method.__name__} упал с ошибкой: {e}")
    
    print("\n" + "=" * 50)
    print(f"📊 РЕЗУЛЬТАТЫ: {passed} пройдено, {failed} не пройдено")
    print("=" * 50)
    
    return failed == 0

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)