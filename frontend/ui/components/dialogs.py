import flet as ft

def create_confirm_dialog(page: ft.Page, title: str, message: str, 
                         on_confirm, on_cancel=None) -> ft.AlertDialog:
    """Создает диалог подтверждения."""
    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text(title),
        content=ft.Text(message),
        actions=[
            ft.TextButton("Отмена", on_click=lambda e: _close_dialog(page, dialog, on_cancel)),
            ft.TextButton("Подтвердить", on_click=lambda e: _close_dialog(page, dialog, on_confirm))
        ]
    )
    return dialog

def create_info_dialog(page: ft.Page, title: str, message: str) -> ft.AlertDialog:
    """Создает информационный диалог."""
    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text(title),
        content=ft.Text(message),
        actions=[
            ft.TextButton("OK", on_click=lambda e: page.close(dialog))
        ]
    )
    return dialog

def _close_dialog(page: ft.Page, dialog: ft.AlertDialog, callback=None):
    """Закрывает диалог и вызывает callback."""
    page.close(dialog)
    if callback:
        callback()