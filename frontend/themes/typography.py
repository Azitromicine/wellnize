# frontend/themes/typography.py
"""
Типография Wellnize.
"""
from typing import Dict

WELLNIZE_TYPOGRAPHY: Dict[str, Dict] = {
    'h1': {'size': 48, 'weight': 'bold', 'font_family': 'Inter'},
    'h2': {'size': 36, 'weight': 'bold', 'font_family': 'Inter'},
    'h3': {'size': 28, 'weight': 'bold', 'font_family': 'Inter'},
    'h4': {'size': 24, 'weight': 'bold', 'font_family': 'Inter'},
    'h5': {'size': 20, 'weight': 'bold', 'font_family': 'Inter'},
    'h6': {'size': 18, 'weight': 'bold', 'font_family': 'Inter'},
    'subtitle1': {'size': 16, 'weight': 'normal', 'font_family': 'Inter'},
    'subtitle2': {'size': 14, 'weight': 'normal', 'font_family': 'Inter'},
    'body1': {'size': 16, 'weight': 'normal', 'font_family': 'Inter'},
    'body2': {'size': 14, 'weight': 'normal', 'font_family': 'Inter'},
    'button': {'size': 14, 'weight': 'bold', 'font_family': 'Inter'},
    'caption': {'size': 12, 'weight': 'normal', 'font_family': 'Inter'},
    'overline': {'size': 10, 'weight': 'bold', 'font_family': 'Inter'},
}

def get_font_style(style_name: str) -> Dict:
    """Получить стиль шрифта по имени."""
    return WELLNIZE_TYPOGRAPHY.get(style_name, {})