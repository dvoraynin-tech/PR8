# Створення текстового файлу та вивід вмісту файлу - Бобошко Вадим
def create_file():
    try:
        file = open("students_questions.txt", "w", encoding="utf-8")
        file.write("Файл для питань і відповідей з Python\n")
        file.close()
    except FileNotFoundError:
        print("Помилка: не знайдено шлях до файлу.")
    except PermissionError:
        print("Помилка: немає дозволу на запис у файл.")
create_file()

def read_file():
    try:
        file = open("students_questions.txt", "r", encoding="utf-8")
        print("Вміст файлу:")
        print("--------------------------")
        print(file.read())
        file.close()
    except FileNotFoundError:
        print("Помилка: файл не знайдено.")

# Перше питання - Бобошко Вадим
def first_question():
    try:
        file = open("students_questions.txt", "a", encoding="utf-8")
        file.write("Питання Бобошка Вадима\n")
        file.write("1. Що таке список (list) у Python і як можна додати елемент у список?\n")
        file.close()
    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
    except PermissionError:
        print("Помилка: немає дозволу на запис у файл.")
first_question()






read_file()
