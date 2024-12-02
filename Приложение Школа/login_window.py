#login_window.py

import tkinter as tk
from tkinter import messagebox
from main_window import MainWindow

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Авторизация")
        self.root.geometry("400x300")

        # Лейбл и поля для ввода логина и пароля
        self.label_login = tk.Label(self.root, text="Логин:", font=('Arial', 14))
        self.label_login.pack(pady=10)
        self.entry_login = tk.Entry(self.root, font=('Arial', 14))
        self.entry_login.pack(pady=5)

        self.label_password = tk.Label(self.root, text="Пароль:", font=('Arial', 14))
        self.label_password.pack(pady=10)
        self.entry_password = tk.Entry(self.root, show="*", font=('Arial', 14))
        self.entry_password.pack(pady=5)

        # Кнопка для входа
        self.button_login = tk.Button(self.root, text="Войти", command=self.login, font=('Arial', 14), bg="#4CAF50", fg="white", width=20)
        self.button_login.pack(pady=20)

    def login(self):
        """Обработчик кнопки входа."""
        login = self.entry_login.get()
        password = self.entry_password.get()

        from database import authenticate_user

        user = authenticate_user(login, password)
        if user:
            messagebox.showinfo("Успешно", "Добро пожаловать!")
            # Открытие главного окна
            self.root.destroy()  # Закрыть окно авторизации
            root = tk.Tk()
            MainWindow(root, user)
            root.mainloop()
        else:
            messagebox.showerror("Ошибка", "Неверный логин или пароль.")