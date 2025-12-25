import flet as ft

def create_primary_button(text: str, on_click, icon=None) -> ft.Control:
    """Создает основную кнопку Wellnize."""
    content = [ft.Text(text, weight=ft.FontWeight.BOLD)]
    if icon:
        content.insert(0, ft.Icon(icon))
    
    return ft.ElevatedButton(
        content=ft.Row(content, spacing=10),
        on_click=on_click,
        style=ft.ButtonStyle(
            padding=ft.padding.symmetric(horizontal=20, vertical=12),
            bgcolor=ft.Colors.BLUE_600,
            color=ft.Colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=8)
        )
    )

def create_secondary_button(text: str, on_click, icon=None) -> ft.Control:
    """Создает второстепенную кнопку."""
    content = [ft.Text(text)]
    if icon:
        content.insert(0, ft.Icon(icon))
    
    return ft.OutlinedButton(
        content=ft.Row(content, spacing=10),
        on_click=on_click,
        style=ft.ButtonStyle(
            padding=ft.padding.symmetric(horizontal=20, vertical=12),
            shape=ft.RoundedRectangleBorder(radius=8)
        )
    )

def create_icon_button(icon, on_click, color=None, tooltip=None) -> ft.Control:
    """Создает кнопку с иконкой."""
    return ft.IconButton(
        icon=icon,
        on_click=on_click,
        icon_color=color,
        tooltip=tooltip
    )