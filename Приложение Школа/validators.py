#validators.py

def is_valid_birthdate(birthdate):
    try:
        # Проверка формата "дд-мм-гггг"
        day, month, year = map(int, birthdate.split('-'))
        return True
    except ValueError:
        return False