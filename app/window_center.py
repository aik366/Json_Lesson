def center_window(window, width, height):
    # Получаем размеры экрана
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Рассчитываем координаты для размещения окна по центру экрана
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Устанавливаем окно по центру экрана
    window.geometry(f"{width}x{height}+{x}+{y}")
