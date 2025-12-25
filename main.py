# main.py
import flet as ft
from frontend.app import WellnizeApp

def main(page: ft.Page):
    """Основная функция - точка входа."""
    print("=" * 50)
    print("🚀 Запуск Wellnize")
    print("=" * 50)
    
    # Создаем приложение и запускаем
    app = WellnizeApp(page)
    
    # Запускаем асинхронно
    import asyncio
    asyncio.create_task(app.start())

# Запуск приложения
if __name__ == "__main__":
    ft.run(main, view=ft.AppView.FLET_APP, assets_dir="assets")