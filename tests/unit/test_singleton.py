# tests/unit/test_singleton.py
import sys
import os

# Добавляем путь к проекту
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from frontend.core.state.app import AppState

def test_singleton():
    """Тестирует работу синглтона."""
    print("\n🧪 Тест синглтона AppState")
    
    # Создаем несколько "экземпляров"
    state1 = AppState()
    state2 = AppState()
    state3 = AppState()
    
    # Проверяем, что это один и тот же объект
    assert state1 is state2, "state1 и state2 должны быть одним объектом"
    assert state2 is state3, "state2 и state3 должны быть одним объектом"
    assert id(state1) == id(state2) == id(state3), "Все ID должны совпадать"
    
    print("✅ Создан новый экземпляр AppState (синглтон)")  
    print("✅ Все объекты - один и тот же синглтон")
    return True

def run_tests():
    """Запускает все тесты в этом файле."""
    print("=" * 60)
    print("🚀 ЗАПУСК ТЕСТОВ SINGLETON")
    print("=" * 60)
    
    try:
        test_singleton()
        print("\n✅ Все тесты синглтона пройдены!")
        return True
    except AssertionError as e:
        print(f"\n❌ Тест не пройден: {e}")
        return False
    except Exception as e:
        print(f"\n💥 Ошибка: {e}")
        return False

# Функция для автоматического запуска
def run_all_tests():
    """Алиас для совместимости."""
    return run_tests()

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)