# Створення текстового файлу з обробкою виключень - Бобошко Вадим
def create_file():
    try:
        # спробуємо створити файл для запису
        file = open("students_questions.txt", "w", encoding="utf-8")
        file.write("Файл для питань і відповідей з Python\n")
        file.close()
    except FileNotFoundError:
        print("Помилка: не знайдено шлях до файлу.")
    except PermissionError:
        print("Помилка: немає дозволу на запис у файл.")

create_file()
