# frontend/themes/__init__.py
from .colors import get_color, get_theme_colors, WELLNIZE_COLORS
from .typography import get_font_style, WELLNIZE_TYPOGRAPHY

__all__ = [
    'get_color', 'get_theme_colors', 'WELLNIZE_COLORS',
    'get_font_style', 'WELLNIZE_TYPOGRAPHY'
]