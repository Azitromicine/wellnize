# tests/unit/test_components.py (обновленная версия)
import sys
import os

# Добавляем путь к проекту
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import flet as ft

class TestComponents:
    """Тесты для UI компонентов с поддержкой Flet 0.80.0."""
    
    def test_flet_version(self):
        """Тест версии Flet."""
        print(f"\n🧪 Версия Flet: {ft.__version__}")
        assert ft.__version__ >= "0.80.0", "Требуется Flet 0.80.0+"
        return True
    
    def test_animation_api(self):
        """Тест API анимаций Flet 0.80.0."""
        print("\n🧪 Тест API анимаций")
        
        # Проверяем что ft.Animation существует
        assert hasattr(ft, 'Animation'), "ft.Animation должен существовать"
        assert hasattr(ft, 'AnimationCurve'), "ft.AnimationCurve должен существовать"
        
        # Тестируем создание анимации
        anim = ft.Animation(duration=300, curve=ft.AnimationCurve.EASE_IN_OUT)
        assert anim.duration == 300, "Длительность должна быть 300ms"
        assert anim.curve == ft.AnimationCurve.EASE_IN_OUT, "Кривая должна быть EASE_IN_OUT"
        
        print("✅ API анимаций работает корректно")
        return True
    
    def test_header_creation(self):
        """Тест создания header."""
        print("\n🧪 Тест создания header")
        
        from frontend.ui.components.header import create_header
        
        # Мокируем callback функции
        def mock_navigate(page):
            return f"Навигация на: {page}"
        
        def mock_logout():
            return "Выход из системы"
        
        def mock_toggle():
            return "Toggle sidebar"
        
        # Тестируем header для гостя
        guest_header = create_header(
            is_authenticated=False,
            user_name=None,
            on_navigate=mock_navigate,
            on_logout=mock_logout,
            on_toggle_sidebar=mock_toggle,
            sidebar_expanded=True
        )
        
        assert guest_header is not None, "Header должен создаваться"
        assert isinstance(guest_header, ft.Container), "Header должен быть Container"
        assert guest_header.height == 60, f"Высота header должна быть 60, а не {guest_header.height}"
        
        print("✅ Header для гостя создается корректно")
        
        # Тестируем header для авторизованного пользователя
        auth_header = create_header(
            is_authenticated=True,
            user_name="test_user",
            on_navigate=mock_navigate,
            on_logout=mock_logout,
            on_toggle_sidebar=mock_toggle,
            sidebar_expanded=False
        )
        
        assert auth_header is not None, "Header должен создаваться"
        
        print("✅ Header для авторизованного пользователя создается корректно")
        return True
    
    def test_sidebar_creation_expanded(self):
        """Тест создания развернутого sidebar."""
        print("\n🧪 Тест создания развернутого sidebar")
        
        from frontend.ui.components.sidebar import create_sidebar
        
        def mock_navigate(page):
            return f"Навигация на: {page}"
        
        # Тестируем sidebar для гостя (развернутый)
        guest_sidebar = create_sidebar(
            is_authenticated=False,
            current_page="features",
            on_navigate=mock_navigate,
            expanded=True
        )
        
        assert guest_sidebar is not None, "Sidebar должен создаваться"
        assert guest_sidebar.width == 250, f"Развернутый sidebar должен иметь ширину 250, имеет: {guest_sidebar.width}"
        
        # Проверяем анимацию
        assert hasattr(guest_sidebar, 'animate'), "Sidebar должен иметь атрибут animate"
        assert guest_sidebar.animate is not None, "Анимация должна быть установлена"
        
        print("✅ Развернутый sidebar создается корректно с анимацией")
        return True
    
    def test_sidebar_creation_collapsed(self):
        """Тест создания свернутого sidebar."""
        print("\n🧪 Тест создания свернутого sidebar")
        
        from frontend.ui.components.sidebar import create_sidebar
        
        def mock_navigate(page):
            return f"Навигация на: {page}"
        
        # Тестируем sidebar для авторизованного пользователя (свернутый)
        auth_sidebar = create_sidebar(
            is_authenticated=True,
            current_page="dashboard",
            on_navigate=mock_navigate,
            expanded=False
        )
        
        assert auth_sidebar is not None, "Sidebar должен создаваться"
        assert auth_sidebar.width == 80, f"Свернутый sidebar должен иметь ширину 80, имеет: {auth_sidebar.width}"
        
        # Проверяем анимацию
        assert hasattr(auth_sidebar, 'animate'), "Sidebar должен иметь атрибут animate"
        assert auth_sidebar.animate is not None, "Анимация должна быть установлена"
        
        print("✅ Свернутый sidebar создается корректно с анимацией")
        return True
    
    def test_sidebar_states(self):
        """Тест разных состояний sidebar."""
        print("\n🧪 Тест разных состояний sidebar")
        
        from frontend.ui.components.sidebar import create_sidebar
        
        page_counts = []
        
        def mock_navigate(page):
            page_counts.append(page)
            return f"Навигация на: {page}"
        
        # Создаем sidebar в разных состояниях
        sidebar_expanded_guest = create_sidebar(
            is_authenticated=False,
            current_page="welcome",
            on_navigate=mock_navigate,
            expanded=True
        )
        
        sidebar_collapsed_guest = create_sidebar(
            is_authenticated=False,
            current_page="welcome",
            on_navigate=mock_navigate,
            expanded=False
        )
        
        sidebar_expanded_auth = create_sidebar(
            is_authenticated=True,
            current_page="dashboard",
            on_navigate=mock_navigate,
            expanded=True
        )
        
        sidebar_collapsed_auth = create_sidebar(
            is_authenticated=True,
            current_page="dashboard",
            on_navigate=mock_navigate,
            expanded=False
        )
        
        # Проверяем все создались
        sidebars = [sidebar_expanded_guest, sidebar_collapsed_guest,
                   sidebar_expanded_auth, sidebar_collapsed_auth]
        
        for i, sidebar in enumerate(sidebars):
            assert sidebar is not None, f"Sidebar {i} должен создаваться"
            assert hasattr(sidebar, 'animate'), f"Sidebar {i} должен иметь анимацию"
            assert sidebar.animate is not None, f"Анимация sidebar {i} должна быть установлена"
        
        # Проверяем ширины
        assert sidebar_expanded_guest.width == 250, "Развернутый должен быть 250px"
        assert sidebar_collapsed_guest.width == 80, "Свернутый должен быть 80px"
        assert sidebar_expanded_auth.width == 250, "Развернутый должен быть 250px"
        assert sidebar_collapsed_auth.width == 80, "Свернутый должен быть 80px"
        
        print("✅ Все состояния sidebar создаются корректно с анимацией")
        return True
    
    def test_sidebar_animation_details(self):
        """Тест деталей анимации sidebar."""
        print("\n🧪 Тест деталей анимации sidebar")
        
        from frontend.ui.components.sidebar import create_sidebar
        
        def mock_navigate(page):
            return f"Навигация на: {page}"
        
        sidebar = create_sidebar(
            is_authenticated=True,
            current_page="dashboard",
            on_navigate=mock_navigate,
            expanded=True
        )
        
        # Проверяем тип анимации
        assert isinstance(sidebar.animate, ft.Animation), "Анимация должна быть ft.Animation"
        
        # Проверяем параметры анимации
        anim = sidebar.animate
        assert anim.duration == 300, f"Длительность анимации должна быть 300ms, а не {anim.duration}"
        assert anim.curve == ft.AnimationCurve.EASE_IN_OUT, f"Кривая должна быть EASE_IN_OUT"
        
        print(f"✅ Анимация: duration={anim.duration}ms, curve={anim.curve}")
        return True

def run_tests():
    """Запускает все тесты компонентов."""
    print("=" * 70)
    print("🚀 ТЕСТЫ UI КОМПОНЕНТОВ (Flet 0.80.0 с анимацией)")
    print("=" * 70)
    
    test_suite = TestComponents()
    passed = 0
    total = 0
    
    # Получаем все методы тестов
    test_methods = [
        test_suite.test_flet_version,
        test_suite.test_animation_api,
        test_suite.test_header_creation,
        test_suite.test_sidebar_creation_expanded,
        test_suite.test_sidebar_creation_collapsed,
        test_suite.test_sidebar_states,
        test_suite.test_sidebar_animation_details,
    ]
    
    for test_method in test_methods:
        total += 1
        test_name = test_method.__name__.replace('_', ' ').title()
        
        print(f"\n🔍 Тест: {test_name}")
        print("-" * 40)
        
        try:
            result = test_method()
            if result is True:
                passed += 1
                print(f"✅ Пройден")
            else:
                print(f"❌ Не пройден (вернул {result})")
        except AssertionError as e:
            print(f"❌ AssertionError: {e}")
        except ImportError as e:
            print(f"❌ ImportError: {e}")
            print("  Убедитесь, что обновили sidebar.py")
        except AttributeError as e:
            print(f"❌ AttributeError: {e}")
            print("  Проблема с API Flet 0.80.0")
        except Exception as e:
            print(f"💥 Неожиданная ошибка: {type(e).__name__}: {e}")
            import traceback
            traceback.print_exc()
    
    print(f"\n{'='*70}")
    print(f"📊 РЕЗУЛЬТАТЫ: {passed}/{total} тестов пройдено")
    
    if passed == total:
        print("🎉 ВСЕ ТЕСТЫ КОМПОНЕНТОВ ПРОЙДЕНЫ!")
    else:
        print(f"⚠️ {total - passed} тестов не пройдено")
    
    print("=" * 70)
    
    return passed == total

def run_all_tests():
    """Алиас для совместимости."""
    return run_tests()

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)