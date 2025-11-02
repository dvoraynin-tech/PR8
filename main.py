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

# Відповідь на перше питання — Подоляка Ярослав
def first_answer():
    try:
        with open("students_questions.txt", "a", encoding="utf-8") as file:
            file.write("Відповідь Подоляки Ярослава\n")
            file.write(
                "Список (list) — це змінна впорядкована структура даних у Python, "
                "яка може містити елементи різних типів (числа, рядки, інші списки тощо).\n"
                "Списки дозволяють змінювати свій вміст після створення — додавати, видаляти "
                "або змінювати елементи.\n"
                "Основні способи додавання елементів у список, append, insert і extend.\n"
            )
        print("Відповідь Подоляки Ярослава успішно додана до файлу.")
    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
    except PermissionError:
        print("Помилка: немає дозволу на запис у файл.")
    except Exception as e:
        print(f"Несподівана помилка: {e}")

first_answer()


# Друге питання — Подоляка Ярослав
def second_question():
    try:
        with open("students_questions.txt", "a", encoding="utf-8") as file:
            file.write("\nПитання Подоляки Ярослава\n")
            file.write("2. Що таке множина (set) у Python? Як виконати операції об’єднання, перетину та різниці множин?\n")
        print("Питання Подоляки Ярослава успішно додане до файлу.")
    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
    except PermissionError:
        print("Помилка: немає дозволу на запис у файл.")
    except Exception as e:
        print(f"Несподівана помилка: {e}")

second_question()


read_file()
