import tkinter as tk
from tkinter import filedialog, messagebox
from database import add_schedule, get_schedule, add_grade, get_users, get_grades

class MainWindow:
    def __init__(self, root, user):
        """
        Конструктор главного окна после авторизации.
        :param root: Главное окно приложения.
        :param user: Информация о текущем пользователе.
        """
        self.root = root
        self.user = user
        self.root.title(f"Личный кабинет - {user[1]}")
        self.root.geometry("500x400")

        # Заголовок
        self.label = tk.Label(self.root, text=f"Добро пожаловать, {user[1]}!", font=("Arial", 16))
        self.label.grid(row=0, column=0, columnspan=2, pady=20)

        # Кнопки действий
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.grid(row=1, column=0, columnspan=2, pady=10)

        actions = [
            ("Посмотреть домашнее задание", self.view_homework),
            ("Скинуть домашнее задание", self.submit_homework),
            ("Посмотреть посещаемость", self.view_attendance),
            ("Посмотреть расписание", self.view_schedule),
            ("Добавить расписание", self.add_schedule),  # Новая кнопка для добавления расписания
            ("Посмотреть успеваемость", self.view_grades),
            ("Чат с учениками", self.chat_with_teacher),
            ("Добавить оценку", self.add_grade_window),  # Кнопка для добавления оценки
        ]

        # Размещение кнопок в сетке
        row, col = 0, 0
        for text, command in actions:
            btn = tk.Button(self.buttons_frame, text=text, width=30, command=command, font=('Arial', 12), bg="#4CAF50", fg="white")
            btn.grid(row=row, column=col, pady=5, padx=5)
            row += 1
            if row > 2:  # после 3 кнопок начинаем новую колонку
                row = 0
                col += 1

        # Кнопка выхода
        self.button_logout = tk.Button(self.root, text="Выйти", font=('Arial', 14), width=20, bg="#f44336", fg="white", command=self.logout)
        self.button_logout.grid(row=2, column=0, columnspan=2, pady=20)

    def add_schedule(self):
        """Добавить расписание в базу данных."""
        file_path = filedialog.askopenfilename(title="Выберите текстовый файл расписания", filetypes=[("Text Files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    schedule_content = file.read()

                # Сохранение в базу данных
                add_schedule(self.user[0], schedule_content)  # user[0] - ID пользователя
                messagebox.showinfo("Успех", "Расписание успешно добавлено!")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось добавить расписание: {e}")

    def view_schedule(self):
        """Открыть окно для просмотра расписания."""
        schedule = get_schedule(self.user[0])  # user[0] - ID пользователя

        if schedule:
            schedule_window = tk.Toplevel(self.root)
            schedule_window.title("Ваше расписание")
            schedule_window.geometry("400x300")

            schedule_display = tk.Text(schedule_window, width=50, height=15, wrap=tk.WORD)
            schedule_display.insert(tk.END, schedule)
            schedule_display.config(state=tk.DISABLED)
            schedule_display.pack(pady=20)
        else:
            messagebox.showinfo("Расписание", "Расписание пока не добавлено.")

    def view_homework(self):
        """Открыть окно для просмотра домашнего задания."""
        homework_window = tk.Toplevel(self.root)
        homework_window.title("Домашнее задание")
        homework_window.geometry("400x300")

        homework_text = """
        1. Математика: Упражнение 5, страницы 30-35.
        2. Физика: Задача 3, страницы 22-23.
        3. Химия: Подготовить отчет о лабораторной работе.
        """

        homework_display = tk.Text(homework_window, width=50, height=15, wrap=tk.WORD)
        homework_display.insert(tk.END, homework_text)
        homework_display.config(state=tk.DISABLED)
        homework_display.pack(pady=20)

    def submit_homework(self):
        """Открыть окно для отправки домашнего задания с выбором предмета."""
        submit_window = tk.Toplevel(self.root)
        submit_window.title("Выбор предмета для сдачи домашнего задания")
        submit_window.geometry("300x200")

        subject_label = tk.Label(submit_window, text="Выберите предмет:")
        subject_label.pack(pady=10)

        subjects = ["Математика", "Физика", "Химия", "Биология", "История"]
        subject_var = tk.StringVar(submit_window)
        subject_var.set(subjects[0])

        subject_menu = tk.OptionMenu(submit_window, subject_var, *subjects)
        subject_menu.pack(pady=10)

        next_button = tk.Button(submit_window, text="Далее", command=lambda: self.choose_homework_file(submit_window, subject_var))
        next_button.pack(pady=10)

    def choose_homework_file(self, submit_window, subject_var):
        subject = subject_var.get()
        file_path = filedialog.askopenfilename(title=f"Выберите файл для {subject}", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

        if file_path:
            messagebox.showinfo("Сдача домашнего задания", f"Домашнее задание по {subject} ({file_path}) успешно отправлено!")
            submit_window.destroy()
        else:
            messagebox.showwarning("Отмена", "Вы не выбрали файл для отправки!")

    def view_attendance(self):
        """Открыть окно для просмотра посещаемости."""
        attendance_window = tk.Toplevel(self.root)
        attendance_window.title("Посещаемость")
        attendance_window.geometry("400x300")

        attendance_text = """
        Понедельник: Присутствовал
        Вторник: Пропущено 1 занятие
        Среда: Присутствовал
        Четверг: Пропущено 2 занятия
        Пятница: Присутствовал
        """

        attendance_display = tk.Text(attendance_window, width=50, height=15, wrap=tk.WORD)
        attendance_display.insert(tk.END, attendance_text)
        attendance_display.config(state=tk.DISABLED)
        attendance_display.pack(pady=20)

    def view_grades(self):
        """Открыть окно для просмотра успеваемости."""
        grades_window = tk.Toplevel(self.root)
        grades_window.title("Успеваемость")
        grades_window.geometry("400x300")

        grades_text = """
        Математика: 4
        Физика: 5
        Химия: 3
        Биология: 5
        История: 4
        """

        grades_display = tk.Text(grades_window, width=50, height=15, wrap=tk.WORD)
        grades_display.insert(tk.END, grades_text)
        grades_display.config(state=tk.DISABLED)
        grades_display.pack(pady=20)

    def chat_with_teacher(self):
        """Открыть окно чата с преподавателем."""
        chat_window = tk.Toplevel(self.root)
        chat_window.title("Чат с преподавателем")
        chat_window.geometry("400x300")

        self.text_area = tk.Text(chat_window, width=45, height=15, wrap=tk.WORD, state=tk.DISABLED)
        self.text_area.grid(row=0, column=0, padx=10, pady=10)

        self.message_entry = tk.Entry(chat_window, width=45)
        self.message_entry.grid(row=1, column=0, padx=10, pady=10)

        self.send_button = tk.Button(chat_window, text="Отправить", width=20, command=self.send_message)
        self.send_button.grid(row=2, column=0, pady=10)

    def send_message(self):
        message = self.message_entry.get()
        if message:
            self.display_message(f"Вы: {message}")
            self.message_entry.delete(0, tk.END)
            self.display_message(f"Преподаватель: Ответ на ваше сообщение.")
        else:
            messagebox.showwarning("Ошибка", "Введите сообщение для отправки.")

    def display_message(self, message):
        self.text_area.config(state=tk.NORMAL)
        self.text_area.insert(tk.END, message + "\n")
        self.text_area.config(state=tk.DISABLED)
        self.text_area.yview(tk.END)

    def logout(self):
        """Закрыть окно и вернуться на экран авторизации."""
        self.root.destroy()
        from login_window import LoginWindow
        root = tk.Tk()
        login_window = LoginWindow(root)
        login_window.run()

    def add_grade_window(self):
        """Открыть окно для добавления оценки ученику."""
        add_grade_window = tk.Toplevel(self.root)
        add_grade_window.title("Добавить оценку")
        add_grade_window.geometry("400x300")

        # Получить список учеников из базы данных
        users = get_users()
        user_names = [user[1] for user in users]  # user[1] - имя ученика

        student_label = tk.Label(add_grade_window, text="Выберите ученика:")
        student_label.pack(pady=10)

        student_var = tk.StringVar(add_grade_window)
        student_var.set(user_names[0])

        student_menu = tk.OptionMenu(add_grade_window, student_var, *user_names)
        student_menu.pack(pady=10)

        subject_label = tk.Label(add_grade_window, text="Выберите предмет:")
        subject_label.pack(pady=10)

        subjects = ["Математика", "Физика", "Химия", "Биология", "История"]
        subject_var = tk.StringVar(add_grade_window)
        subject_var.set(subjects[0])

        subject_menu = tk.OptionMenu(add_grade_window, subject_var, *subjects)
        subject_menu.pack(pady=10)

        grade_label = tk.Label(add_grade_window, text="Введите оценку:")
        grade_label.pack(pady=10)

        grade_entry = tk.Entry(add_grade_window)
        grade_entry.pack(pady=10)

        submit_button = tk.Button(add_grade_window, text="Добавить", command=lambda: self.submit_grade(student_var, subject_var, grade_entry, add_grade_window))
        submit_button.pack(pady=10)

    def submit_grade(self, student_var, subject_var, grade_entry, add_grade_window):
        """Добавить оценку в базу данных."""
        student_name = student_var.get()
        subject = subject_var.get()
        grade = grade_entry.get()

        if grade.isdigit() and 1 <= int(grade) <= 5:
            student_id = next(user[0] for user in get_users() if user[1] == student_name)
            add_grade(student_id, subject, grade)
            messagebox.showinfo("Успех", f"Оценка по {subject} для {student_name} успешно добавлена!")
            add_grade_window.destroy()
        else:
            messagebox.showwarning("Ошибка", "Пожалуйста, введите корректную оценку от 1 до 5.")
