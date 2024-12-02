#main.py

import tkinter as tk
from start_window import StartWindow

if __name__ == "__main__":
    root = tk.Tk()  # Создаем основное окно
    start_window = StartWindow(root)  # Создаем окно старта
    start_window.run()  # Запускаем его