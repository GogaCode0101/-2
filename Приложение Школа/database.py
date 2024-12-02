import sqlite3

def initialize_database():
    """Функция для инициализации базы данных, создания необходимых таблиц."""
    try:
        # Подключаемся к базе данных
        conn = sqlite3.connect('school_database.db')
        cursor = conn.cursor()

        # Создаем таблицу пользователей, если она не существует
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            birthdate TEXT,
                            contact TEXT,
                            student_class TEXT,
                            login TEXT,
                            password TEXT)''')

        # Создаем таблицу расписания, если она не существует
        cursor.execute('''CREATE TABLE IF NOT EXISTS schedules (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER,
                            schedule TEXT,
                            FOREIGN KEY (user_id) REFERENCES users(id))''')

        # Создаем таблицу студентов, если она не существует
        cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            grade TEXT,
                            class_letter TEXT)''')

        # Создаем таблицу оценок, если она не существует
        cursor.execute('''CREATE TABLE IF NOT EXISTS grades (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            student_id INTEGER,
                            subject TEXT,
                            grade INTEGER,
                            FOREIGN KEY (student_id) REFERENCES students(id))''')

        # Сохраняем изменения и закрываем соединение
        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        raise Exception(f"Произошла ошибка при инициализации базы данных: {e}")

def add_user(name, birthdate, contact, student_class, login, password):
    """Добавить пользователя в базу данных."""
    try:
        conn = sqlite3.connect('school_database.db')
        cursor = conn.cursor()

        cursor.execute('''INSERT INTO users (name, birthdate, contact, student_class, login, password) 
                          VALUES (?, ?, ?, ?, ?, ?)''',
                          (name, birthdate, contact, student_class, login, password))

        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        raise Exception(f"Произошла ошибка при добавлении пользователя: {e}")

def authenticate_user(login, password):
    """Аутентификация пользователя по логину и паролю."""
    try:
        conn = sqlite3.connect('school_database.db')
        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM users WHERE login = ? AND password = ?''', (login, password))
        user = cursor.fetchone()

        conn.close()

        if user:
            return user
        else:
            return None

    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        raise Exception(f"Произошла ошибка при аутентификации пользователя: {e}")

def get_users():
    """Получить всех пользователей из базы данных."""
    try:
        conn = sqlite3.connect('school_database.db')
        cursor = conn.cursor()

        cursor.execute('''SELECT id, name, login FROM users''')
        users = cursor.fetchall()

        conn.close()
        return users

    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        raise Exception(f"Произошла ошибка при получении пользователей: {e}")

def add_schedule(user_id, schedule_content):
    """Добавить расписание для пользователя."""
    try:
        conn = sqlite3.connect('school_database.db')
        cursor = conn.cursor()

        cursor.execute('''INSERT INTO schedules (user_id, schedule) VALUES (?, ?)''',
                       (user_id, schedule_content))
        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        raise Exception(f"Произошла ошибка при добавлении расписания: {e}")

def get_schedule(user_id):
    """Получить расписание для пользователя."""
    try:
        conn = sqlite3.connect('school_database.db')
        cursor = conn.cursor()

        cursor.execute('''SELECT schedule FROM schedules WHERE user_id = ? ORDER BY id DESC LIMIT 1''', (user_id,))
        result = cursor.fetchone()

        conn.close()
        return result[0] if result else None

    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        raise Exception(f"Произошла ошибка при получении расписания: {e}")

def add_student(name, grade, class_letter):
    """Добавить студента в базу данных."""
    try:
        conn = sqlite3.connect('school_database.db')
        cursor = conn.cursor()

        cursor.execute('''INSERT INTO students (name, grade, class_letter) 
                          VALUES (?, ?, ?)''', (name, grade, class_letter))

        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        raise Exception(f"Произошла ошибка при добавлении студента: {e}")

def add_grade(student_id, subject, grade):
    """Добавить оценку для студента."""
    try:
        conn = sqlite3.connect('school_database.db')
        cursor = conn.cursor()

        cursor.execute('''INSERT INTO grades (student_id, subject, grade) 
                          VALUES (?, ?, ?)''', (student_id, subject, grade))

        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        raise Exception(f"Произошла ошибка при добавлении оценки: {e}")

def get_grades(student_id):
    """Получить оценки для студента."""
    try:
        conn = sqlite3.connect('school_database.db')
        cursor = conn.cursor()

        cursor.execute('''SELECT subject, grade FROM grades WHERE student_id = ?''', (student_id,))
        result = cursor.fetchall()

        conn.close()
        return result if result else None

    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        raise Exception(f"Произошла ошибка при получении оценок: {e}")

