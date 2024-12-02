import tkinter as tk
from tkinter import ttk
from database import add_user, add_student  # Импортируем add_student
from messages import show_error, show_success
from validators import is_valid_birthdate


class SchoolRegistrationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Регистрация нового учителя")

        # Заголовок окна
        self.title_label = tk.Label(self.root, text="Регистрация нового учителя", font=("Arial", 16))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Метки и поля ввода
        self.name_label = tk.Label(self.root, text="ФИО учителя:")
        self.name_label.grid(row=1, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self.root, width=30)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)

        self.birthdate_label = tk.Label(self.root, text="Дата рождения (дд-мм-гггг):")
        self.birthdate_label.grid(row=2, column=0, padx=10, pady=5)
        self.birthdate_entry = tk.Entry(self.root, width=30)
        self.birthdate_entry.grid(row=2, column=1, padx=10, pady=5)

        self.contact_label = tk.Label(self.root, text="Контактный телефон:")
        self.contact_label.grid(row=3, column=0, padx=10, pady=5)
        self.contact_entry = tk.Entry(self.root, width=30)
        self.contact_entry.grid(row=3, column=1, padx=10, pady=5)

        self.class_label = tk.Label(self.root, text="Классы учителя:")
        self.class_label.grid(row=4, column=0, padx=10, pady=5)

        # Создаем выпадающий список для выбора класса
        self.class_combo = ttk.Combobox(self.root,
                                        values=["1-4", "5-9", "10-11"])
        self.class_combo.grid(row=4, column=1, padx=10, pady=5)
        self.class_combo.set("5-А")  # Устанавливаем значение по умолчанию

        # Логин и пароль
        self.login_label = tk.Label(self.root, text="Логин:")
        self.login_label.grid(row=5, column=0, padx=10, pady=5)
        self.login_entry = tk.Entry(self.root, width=30)
        self.login_entry.grid(row=5, column=1, padx=10, pady=5)

        self.password_label = tk.Label(self.root, text="Пароль:")
        self.password_label.grid(row=6, column=0, padx=10, pady=5)
        self.password_entry = tk.Entry(self.root, width=30, show="*")
        self.password_entry.grid(row=6, column=1, padx=10, pady=5)

        # Кнопка для отправки заявки
        self.submit_button = tk.Button(self.root, text="Отправить заявку", command=self.submit_application)
        self.submit_button.grid(row=7, column=0, columnspan=2, pady=20)

        # Кнопка для добавления ученика
        self.add_student_button = tk.Button(self.root, text="Добавить ученика", command=self.add_student)
        self.add_student_button.grid(row=8, column=0, columnspan=2, pady=20)

    def submit_application(self):
        # Получаем данные из полей
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

        # Валидация даты рождения
        if not is_valid_birthdate(birthdate):
            show_error("Ошибка", "Неверный формат даты рождения! Используйте формат дд-мм-гггг.")
            return

        # Добавление пользователя в базу данных
        try:
            add_user(name, birthdate, contact, student_class, login, password)
            show_success("Успех", "Заявка успешно отправлена!")
            self.root.destroy()  # Закрытие окна регистрации после успешной отправки
        except Exception as e:
            show_error("Ошибка базы данных", f"Произошла ошибка при добавлении пользователя: {str(e)}")

    def add_student(self):
        # Окно для добавления ученика
        add_student_window = tk.Toplevel(self.root)
        add_student_window.title("Добавить ученика")
        add_student_window.geometry("400x300")

        # Выбор класса
        self.class_label = tk.Label(add_student_window, text="Выберите класс:")
        self.class_label.grid(row=0, column=0, padx=10, pady=5)

        self.class_combo = ttk.Combobox(add_student_window, values=[str(i) for i in range(1, 12)])
        self.class_combo.grid(row=0, column=1, padx=10, pady=5)

        # Выбор буквы класса
        self.section_label = tk.Label(add_student_window, text="Выберите букву класса:")
        self.section_label.grid(row=1, column=0, padx=10, pady=5)

        self.section_combo = ttk.Combobox(add_student_window, values=["а", "б", "в", "г", "д", "е"])
        self.section_combo.grid(row=1, column=1, padx=10, pady=5)

        # Ввод ФИО ученика
        self.name_label = tk.Label(add_student_window, text="ФИО ученика:")
        self.name_label.grid(row=2, column=0, padx=10, pady=5)

        self.student_name_entry = tk.Entry(add_student_window, width=30)
        self.student_name_entry.grid(row=2, column=1, padx=10, pady=5)

        # Кнопка для добавления ученика
        self.add_button = tk.Button(add_student_window, text="Добавить ученика", command=lambda: self.submit_student(add_student_window))
        self.add_button.grid(row=3, column=0, columnspan=2, pady=20)

    def submit_student(self, add_student_window):
        student_class = self.class_combo.get()  # только номер класса
        student_letter = self.section_combo.get()  # буква класса
        student_name = self.student_name_entry.get()

        if not student_name:
            show_error("Ошибка", "ФИО ученика обязательно!")
            return

        try:
            # Передаем 3 параметра: ФИО, номер класса и букву
            add_student(student_name, student_class, student_letter)
            show_success("Успех", f"Ученик {student_name} успешно добавлен в класс {student_class} {student_letter}!")
            add_student_window.destroy()
        except Exception as e:
            show_error("Ошибка базы данных", f"Произошла ошибка при добавлении ученика: {str(e)}")

    def run(self):
        self.root.mainloop()
