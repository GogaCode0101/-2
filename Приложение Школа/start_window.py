#start_window.py

import tkinter as tk
from ui import SchoolRegistrationApp
from login_window import LoginWindow
from database import initialize_database

class StartWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Школа: Начальное окно")

        # Инициализация базы данных
        initialize_database()

        # Заголовок
        self.title_label = tk.Label(self.root, text="Добро пожаловать в систему школы", font=("Arial", 16))
        self.title_label.pack(pady=20)

        # Кнопки для перехода
        self.register_button = tk.Button(self.root, text="Зарегистрироваться", command=self.open_registration_window)
        self.register_button.pack(pady=10)

        self.login_button = tk.Button(self.root, text="Авторизоваться", command=self.open_login_window)
        self.login_button.pack(pady=10)

    def open_registration_window(self):
        # Открытие окна регистрации
        registration_window = tk.Toplevel(self.root)
        app = SchoolRegistrationApp(registration_window)
        app.run()

    def open_login_window(self):
        # Открытие окна авторизации
        login_window = tk.Toplevel(self.root)
        login_app = LoginWindow(login_window)
        login_app.run()

    def run(self):
        self.root.mainloop()