#registration_window.py

import tkinter as tk
from tkinter import messagebox
from database import add_user
from messages import show_error, show_success


class RegistrationWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Регистрация нового ученика")

        # Метки и поля ввода
        self.name_label = tk.Label(self.root, text="ФИО ученика:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self.root, width=30)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.birthdate_label = tk.Label(self.root, text="Дата рождения:")
        self.birthdate_label.grid(row=1, column=0, padx=10, pady=5)
        self.birthdate_entry = tk.Entry(self.root, width=30)
        self.birthdate_entry.grid(row=1, column=1, padx=10, pady=5)

        self.contact_label = tk.Label(self.root, text="Контактный телефон:")
        self.contact_label.grid(row=2, column=0, padx=10, pady=5)
        self.contact_entry = tk.Entry(self.root, width=30)
        self.contact_entry.grid(row=2, column=1, padx=10, pady=5)

        self.class_label = tk.Label(self.root, text="Класс ученика:")
        self.class_label.grid(row=3, column=0, padx=10, pady=5)

        # Создаем выпадающий список для выбора класса
        self.class_combo = ttk.Combobox(self.root,
                                        values=["1-А", "1-Б", "2-А", "2-Б", "3-А", "3-Б", "4-А", "4-Б", "5-А", "5-Б",
                                                "6-А", "6-Б"])
        self.class_combo.grid(row=3, column=1, padx=10, pady=5)
        self.class_combo.set("5-А")  # Устанавливаем значение по умолчанию

        # Метки и поля для логина и пароля
        self.login_label = tk.Label(self.root, text="Логин:")
        self.login_label.grid(row=4, column=0, padx=10, pady=5)
        self.login_entry = tk.Entry(self.root, width=30)
        self.login_entry.grid(row=4, column=1, padx=10, pady=5)

        self.password_label = tk.Label(self.root, text="Пароль:")
        self.password_label.grid(row=5, column=0, padx=10, pady=5)
        self.password_entry = tk.Entry(self.root, show="*", width=30)
        self.password_entry.grid(row=5, column=1, padx=10, pady=5)

        # Кнопка для отправки заявки
        self.submit_button = tk.Button(self.root, text="Отправить заявку", command=self.submit_application)
        self.submit_button.grid(row=6, column=0, columnspan=2, pady=20)

    def submit_application(self):
        name = self.name_entry.get()
        birthdate = self.birthdate_entry.get()
        contact = self.contact_entry.get()
        student_class = self.class_combo.get()
        login = self.login_entry.get()
        password = self.password_entry.get()

        # Проверка данных
        if not name or not birthdate or not contact or not student_class or not login or not password:
            show_error("Ошибка", "Все поля должны быть заполнены!")
            return

        # Добавление пользователя в базу данных
        print("Добавление пользователя в базу данных...")  # Отладочное сообщение
        add_user(name, birthdate, contact, student_class, login, password)
        print("Пользователь добавлен в базу данных.")  # Отладочное сообщение

        show_success("Успех", "Заявка успешно отправлена!")

        # Закрытие окна регистрации
        self.root.destroy()

    def run(self):
        self.root.mainloop()
