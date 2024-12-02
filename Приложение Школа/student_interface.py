#student_interface

import tkinter as tk

class StudentInterface:
    def __init__(self, root, name, student_class):
        self.root = root
        self.root.title(f"Личный кабинет: {name}")

        # Заголовок окна
        self.title_label = tk.Label(self.root, text=f"Привет, {name}!", font=("Arial", 16))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Информация о студенте
        self.info_label = tk.Label(self.root, text=f"Класс: {student_class}", font=("Arial", 14))
        self.info_label.grid(row=1, column=0, columnspan=2, pady=10)

    def run(self):
        self.root.mainloop()