# auth_window.py

import tkinter as tk
from tkinter import messagebox
from database import check_user_credentials
from student_interface import StudentInterface


class AuthWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Авторизация")

        # Заголовок окна
        self.title_label = tk.Label(self.root, text="Авторизация", font=("Arial", 16))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Логин и пароль
        self.username_label = tk.Label(self.root, text="Логин:")
        self.username_label.grid(row=1, column=0, padx=10, pady=5)
        self.username_entry = tk.Entry(self.root, width=30)
        self.username_entry.grid(row=1, column=1, padx=10, pady=5)

        self.password_label = tk.Label(self.root, text="Пароль:")
        self.password_label.grid(row=2, column=0, padx=10, pady=5)
        self.password_entry = tk.Entry(self.root, width=30, show="*")
        self.password_entry.grid(row=2, column=1, padx=10, pady=5)

        # Кнопка для авторизации
        self.login_button = tk.Button(self.root, text="Войти", command=self.login)
        self.login_button.grid(row=3, column=0, columnspan=2, pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Ошибка", "Введите логин и пароль!")
            return

        user = check_user_credentials(username, password)
        if user:
            # Если авторизация успешна, открываем интерфейс ученика
            self.root.destroy()
            student_window = tk.Tk()
            student_interface = StudentInterface(student_window, user[3], user[4])  # user[3] - имя, user[4] - класс
            student_interface.run()
        else:
            messagebox.showerror("Ошибка", "Неверный логин или пароль!")

    def run(self):
        self.root.mainloop()