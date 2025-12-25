# tests/unit/test_utils.py
import sys
import os
import json
from datetime import datetime, timedelta

# Добавляем путь к проекту
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

class TestUtils:
    """Тесты для утилит и вспомогательных функций."""
    
    def test_json_serialization(self):
        """Тест сериализации/десериализации JSON."""
        print("\n🧪 Тест JSON сериализации")
        
        # Тестовые данные
        test_data = {
            "user": "test_user",
            "tasks": ["task1", "task2", "task3"],
            "settings": {"theme": "dark", "notifications": True},
            "timestamp": "2024-01-01"
        }
        
        # Сериализация
        json_str = json.dumps(test_data)
        assert isinstance(json_str, str), "Сериализация должна возвращать строку"
        
        # Десериализация
        parsed_data = json.loads(json_str)
        assert parsed_data["user"] == "test_user", "Данные должны корректно десериализоваться"
        assert len(parsed_data["tasks"]) == 3, "Списки должны сохраняться"
        
        print("✅ JSON сериализация работает корректно")
        return True
    
    def test_datetime_operations(self):
        """Тест операций с датой и временем."""
        print("\n🧪 Тест операций с datetime")
        
        # Текущая дата
        now = datetime.now()
        assert isinstance(now, datetime), "Должен возвращаться объект datetime"
        
        # Добавление времени
        tomorrow = now + timedelta(days=1)
        assert tomorrow > now, "Завтра должно быть позже сегодня"
        
        # Форматирование даты
        date_str = now.strftime("%Y-%m-%d %H:%M:%S")
        assert len(date_str) > 0, "Строка даты не должна быть пустой"
        assert "-" in date_str, "Должен быть разделитель даты"
        
        print("✅ Операции с datetime работают корректно")
        return True
    
    def test_string_operations(self):
        """Тест строковых операций."""
        print("\n🧪 Тест строковых операций")
        
        test_string = "Hello, Wellnize!"
        
        # Базовые операции
        assert test_string.startswith("Hello"), "Должен начинаться с Hello"
        assert test_string.endswith("Wellnize!"), "Должен заканчиваться на Wellnize!"
        assert "Wellnize" in test_string, "Должен содержать Wellnize"
        
        # Преобразования
        upper_string = test_string.upper()
        assert upper_string.isupper(), "Должен быть в верхнем регистре"
        
        lower_string = test_string.lower()
        assert lower_string.islower(), "Должен быть в нижнем регистре"
        
        # Разделение
        parts = test_string.split(", ")
        assert len(parts) == 2, "Должен разделиться на 2 части"
        assert parts[0] == "Hello", "Первая часть должна быть Hello"
        
        print("✅ Строковые операции работают корректно")
        return True
    
    def test_list_operations(self):
        """Тест операций со списками."""
        print("\n🧪 Тест операций со списками")
        
        # Создание и базовые операции
        test_list = [1, 2, 3, 4, 5]
        
        assert len(test_list) == 5, "Длина списка должна быть 5"
        assert sum(test_list) == 15, "Сумма элементов должна быть 15"
        
        # Добавление/удаление
        test_list.append(6)
        assert len(test_list) == 6, "После добавления длина должна быть 6"
        assert test_list[-1] == 6, "Последний элемент должен быть 6"
        
        removed = test_list.pop()
        assert removed == 6, "Удаленный элемент должен быть 6"
        assert len(test_list) == 5, "После удаления длина должна быть 5"
        
        # Фильтрация
        even_numbers = [x for x in test_list if x % 2 == 0]
        assert even_numbers == [2, 4], "Четные числа должны быть 2 и 4"
        
        # Сортировка
        reversed_list = sorted(test_list, reverse=True)
        assert reversed_list == [5, 4, 3, 2, 1], "Отсортированный список должен быть в обратном порядке"
        
        print("✅ Операции со списками работают корректно")
        return True
    
    def test_dictionary_operations(self):
        """Тест операций со словарями."""
        print("\n🧪 Тест операций со словарями")
        
        # Создание словаря
        test_dict = {
            "name": "Wellnize",
            "version": "1.0.0",
            "features": ["tasks", "notes", "tracker"],
            "settings": {"theme": "light", "language": "ru"}
        }
        
        # Базовые операции
        assert "name" in test_dict, "Ключ 'name' должен присутствовать"
        assert test_dict["version"] == "1.0.0", "Версия должна быть 1.0.0"
        
        # Добавление/обновление
        test_dict["author"] = "Team Wellnize"
        assert "author" in test_dict, "Ключ 'author' должен быть добавлен"
        
        test_dict["version"] = "1.0.1"
        assert test_dict["version"] == "1.0.1", "Версия должна обновиться"
        
        # Удаление
        del test_dict["author"]
        assert "author" not in test_dict, "Ключ 'author' должен быть удален"
        
        # Ключи и значения
        keys = list(test_dict.keys())
        assert "name" in keys and "version" in keys, "Должны присутствовать ключи name и version"
        
        values = list(test_dict.values())
        assert "Wellnize" in values, "Должно присутствовать значение Wellnize"
        
        print("✅ Операции со словарями работают корректно")
        return True
    
    def test_error_handling(self):
        """Тест обработки ошибок."""
        print("\n🧪 Тест обработки ошибок")
        
        # Тест обработки исключений
        try:
            # Намеренная ошибка
            result = 10 / 0
            assert False, "Должно было возникнуть исключение"
        except ZeroDivisionError:
            print("✅ ZeroDivisionError корректно перехвачено")
            return True
        except Exception as e:
            print(f"❌ Перехвачено не то исключение: {type(e).__name__}")
            return False
    
    def test_file_operations(self):
        """Тест файловых операций."""
        print("\n🧪 Тест файловых операций")
        
        import tempfile
        
        # Создание временного файла
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp:
            tmp_path = tmp.name
            tmp.write("Test content for Wellnize\nSecond line")
        
        try:
            # Чтение файла
            with open(tmp_path, 'r') as f:
                content = f.read()
            
            assert "Wellnize" in content, "Файл должен содержать 'Wellnize'"
            assert "\n" in content, "Файл должен содержать перенос строки"
            
            # Проверка существования файла
            assert os.path.exists(tmp_path), "Файл должен существовать"
            
            print("✅ Файловые операции работают корректно")
            return True
            
        finally:
            # Очистка
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
    
    def test_environment_variables(self):
        """Тест работы с переменными окружения."""
        print("\n🧪 Тест переменных окружения")
        
        import os
        
        # Устанавливаем тестовую переменную
        test_key = "WELLNIZE_TEST_ENV"
        test_value = "test_value_123"
        
        os.environ[test_key] = test_value
        
        # Проверяем чтение
        read_value = os.environ.get(test_key)
        assert read_value == test_value, f"Должно быть {test_value}, а не {read_value}"
        
        # Проверяем отсутствие переменной
        nonexistent = os.environ.get("WELLNIZE_NONEXISTENT")
        assert nonexistent is None, "Несуществующая переменная должна возвращать None"
        
        # Очищаем (опционально)
        if test_key in os.environ:
            del os.environ[test_key]
        
        print("✅ Работа с переменными окружения корректна")
        return True

def run_tests():
    """Запускает все тесты утилит."""
    print("=" * 60)
    print("🚀 ТЕСТЫ УТИЛИТ И ВСПОМОГАТЕЛЬНЫХ ФУНКЦИЙ")
    print("=" * 60)
    
    test_suite = TestUtils()
    passed = 0
    total = 0
    
    # Получаем все методы тестов
    test_methods = [
        test_suite.test_json_serialization,
        test_suite.test_datetime_operations,
        test_suite.test_string_operations,
        test_suite.test_list_operations,
        test_suite.test_dictionary_operations,
        test_suite.test_error_handling,
        test_suite.test_file_operations,
        test_suite.test_environment_variables,
    ]
    
    for test_method in test_methods:
        total += 1
        test_name = test_method.__name__.replace('_', ' ').title()
        
        print(f"\n🔍 Тест: {test_name}")
        print("-" * 40)
        
        try:
            if test_method():
                passed += 1
                print(f"✅ Пройден")
            else:
                print(f"❌ Не пройден (вернул False)")
        except AssertionError as e:
            print(f"❌ AssertionError: {e}")
        except Exception as e:
            print(f"💥 Неожиданная ошибка: {e}")
    
    print(f"\n{'='*60}")
    print(f"📊 РЕЗУЛЬТАТЫ: {passed}/{total} тестов пройдено")
    
    if passed == total:
        print("🎉 ВСЕ ТЕСТЫ УТИЛИТ ПРОЙДЕНЫ!")
    else:
        print(f"⚠️ {total - passed} тестов не пройдено")
    
    print("=" * 60)
    
    return passed == total

# Функция для автоматического запуска
def run_all_tests():
    """Алиас для совместимости."""
    return run_tests()

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)