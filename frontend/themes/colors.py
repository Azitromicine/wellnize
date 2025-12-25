# frontend/themes/colors.py
"""
Цветовая палитра Wellnize.
"""
from typing import Dict

WELLNIZE_COLORS: Dict[str, str] = {
    # Основные
    'primary': '#4361EE',      # Синий Wellnize
    'secondary': '#7209B7',    # Фиолетовый
    'success': '#4CC9F0',      # Голубой
    'warning': '#F72585',      # Розовый
    'error': '#FF6B6B',        # Красный
    
    # Текст
    'text_primary': '#2B2D42',
    'text_secondary': '#8D99AE',
    'text_light': '#EDF2F4',
    
    # Фоны
    'background': '#FFFFFF',
    'surface': '#F8F9FA',
    'card': '#FFFFFF',
    
    # Акценты
    'accent_blue': '#4CC9F0',
    'accent_purple': '#7209B7',
    'accent_pink': '#F72585',
    'accent_green': '#06D6A0',
    
    # Градиенты
    'gradient_primary': 'linear-gradient(135deg, #4361EE 0%, #3A0CA3 100%)',
    'gradient_success': 'linear-gradient(135deg, #4CC9F0 0%, #4361EE 100%)',
    'gradient_warning': 'linear-gradient(135deg, #F72585 0%, #7209B7 100%)',
}

def get_color(color_name: str) -> str:
    """Получить цвет по имени."""
    return WELLNIZE_COLORS.get(color_name, '#4361EE')

def get_theme_colors(theme: str = 'light') -> Dict[str, str]:
    """Получить цвета для темы."""
    if theme == 'dark':
        return {
            'background': '#121212',
            'surface': '#1E1E1E',
            'card': '#2D2D2D',
            'text_primary': '#FFFFFF',
            'text_secondary': '#B0B0B0',
        }
    
    return WELLNIZE_COLORS