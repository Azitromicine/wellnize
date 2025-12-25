# tests/run_all_tests.py
import sys
import os
import importlib.util

def color_text(text, color_code):
    """Цветной вывод в терминал."""
    colors = {
        'green': '\033[92m',
        'yellow': '\033[93m',
        'red': '\033[91m',
        'blue': '\033[94m',
        'reset': '\033[0m'
    }
    return f"{colors.get(color_code, '')}{text}{colors['reset']}"

def run_test_module(module_path, module_name):
    """Запускает тестовый модуль."""
    print(color_text(f"\n{'='*70}", 'blue'))
    print(color_text(f"🧪  ТЕСТ: {module_name}", 'blue'))
    print(color_text('='*70, 'blue'))
    
    # Добавляем путь к проекту
    original_path = sys.path.copy()
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
    
    try:
        # Динамически импортируем модуль
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Ищем функцию для запуска тестов
        if hasattr(module, 'run_all_tests'):
            result = module.run_all_tests()
        elif hasattr(module, 'run_tests'):
            result = module.run_tests()
        else:
            print(color_text("⚠️  Модуль не содержит стандартной функции запуска тестов", 'yellow'))
            
            # Пробуем найти любую тестовую функцию
            test_functions = [name for name in dir(module) 
                            if name.startswith('test_') and callable(getattr(module, name))]
            
            if test_functions:
                print(color_text(f"📋  Найдены тестовые функции: {', '.join(test_functions)}", 'yellow'))
                # Запускаем первую найденную тестовую функцию
                for func_name in test_functions:
                    try:
                        test_func = getattr(module, func_name)
                        result = test_func()
                        break
                    except:
                        continue
            else:
                return False
        
        return result if isinstance(result, bool) else True
        
    except Exception as e:
        print(color_text(f"💥  Критическая ошибка: {e}", 'red'))
        import traceback
        traceback.print_exc()
        return False
    finally:
        sys.path = original_path

def main():
    """Запускает все тесты."""
    print(color_text("\n" + "="*70, 'green'))
    print(color_text("🚀  ПОЛНЫЙ ТЕСТОВЫЙ ПРОХОД WELLNIZE", 'green'))
    print(color_text("="*70, 'green'))
    
    # Определяем пути ко всем тестам
    base_dir = os.path.dirname(__file__)
    
    test_suites = [
        # Unit тесты
        ("🧠  Unit Тесты", [
            (os.path.join(base_dir, "unit", "test_singleton.py"), "Singleton"),
            (os.path.join(base_dir, "unit", "test_state.py"), "App State"),
            (os.path.join(base_dir, "unit", "test_components.py"), "UI Components"),
            (os.path.join(base_dir, "unit", "test_utils.py"), "Utilities"),
        ]),
        
        # Интеграционные тесты
        ("🔗  Интеграционные тесты", [
            (os.path.join(base_dir, "integration", "test_layout.py"), "Layout"),
            (os.path.join(base_dir, "integration", "test_navigation.py"), "Navigation"),
        ]),
    ]
    
    overall_results = []
    
    for suite_name, tests in test_suites:
        print(color_text(f"\n📁  {suite_name}", 'yellow'))
        print(color_text("-" * 50, 'yellow'))
        
        suite_results = []
        
        for test_path, test_name in tests:
            if os.path.exists(test_path):
                success = run_test_module(test_path, test_name)
                suite_results.append((test_name, success))
                overall_results.append((f"{suite_name} - {test_name}", success))
            else:
                print(color_text(f"⏭️   Файл не найден: {os.path.basename(test_path)}", 'yellow'))
                suite_results.append((test_name, False))
                overall_results.append((f"{suite_name} - {test_name}", False))
        
        # Отчет по сьюите
        suite_passed = sum(1 for _, success in suite_results if success)
        suite_total = len(suite_results)
        
        print(color_text(f"\n📊  Результаты {suite_name}: {suite_passed}/{suite_total}", 
                        'green' if suite_passed == suite_total else 'yellow'))
    
    # Итоговый отчет
    print(color_text("\n" + "="*70, 'blue'))
    print(color_text("📋  ИТОГОВЫЙ ОТЧЕТ", 'blue'))
    print(color_text("="*70, 'blue'))
    
    passed = sum(1 for _, success in overall_results if success)
    total = len(overall_results)
    
    print(color_text(f"\n📈  ОБЩИЙ РЕЗУЛЬТАТ: {passed}/{total} тестов пройдено", 
                    'green' if passed == total else 'yellow'))
    
    if passed == total:
        print(color_text("\n🎉  🎉  🎉  ВСЕ ТЕСТЫ УСПЕШНО ПРОЙДЕНЫ!  🎉  🎉  🎉", 'green'))
    else:
        print(color_text(f"\n⚠️   {total - passed} тестов не пройдено:", 'yellow'))
        
        for test_name, success in overall_results:
            if not success:
                print(color_text(f"    ❌  {test_name}", 'red'))
    
    print(color_text("\n" + "="*70, 'blue'))
    
    # Возвращаем код успеха для CI/CD
    return passed == total

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print(color_text("\n\n⚠️   Тестирование прервано пользователем", 'yellow'))
        sys.exit(1)