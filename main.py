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

# Відповідь на друге питання — Чесной Владислав
def second_answer():
    try:
        with open("students_questions.txt", "a", encoding="utf-8") as file:
            file.write("Відповідь Чесного Владислава\n")
            file.write(
                "Множина (set) — це невпорядкована колекція унікальних елементів у Python. "
                "Множини не можуть містити дублікати і не підтримують індексацію.\n"
                "Операції з множинами:\n"
                "- Об'єднання (union): set1 | set2 або set1.union(set2)\n"
                "- Перетин (intersection): set1 & set2 або set1.intersection(set2)\n"
                "- Різниця (difference): set1 - set2 або set1.difference(set2)\n"
                "Приклад: {1, 2, 3} | {3, 4, 5} = {1, 2, 3, 4, 5}\n"
            )
        print("Відповідь Чесного Владислава успішно додана до файлу.")
    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
    except PermissionError:
        print("Помилка: немає дозволу на запис у файл.")
    except Exception as e:
        print(f"Несподівана помилка: {e}")

second_answer()


# Третє питання — Чесной Владислав
def third_question():
    try:
        with open("students_questions.txt", "a", encoding="utf-8") as file:
            file.write("\nПитання Чесного Владислава\n")
            file.write("3. Що таке словник (dictionary) у Python і як додати, змінити або видалити елемент зі словника?\n")
        print("Питання Чесного Владислава успішно додане до файлу.")
    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
    except PermissionError:
        print("Помилка: немає дозволу на запис у файл.")
    except Exception as e:
        print(f"Несподівана помилка: {e}")

third_question()

# Відповідь на третє питання — Пилипчук Єлизавета
def third_answer():
    try:
        with open("students_questions.txt", "a", encoding="utf-8") as file:
            file.write("Відповідь Пилипчук Єлизавети \n")
            file.write(
                "Словник у Python — це структура даних, яка зберігає інформацію у\n"
                "форматі «ключ — значення». Ключі мають бути унікальними та незмінними,\n"
                "наприклад, рядки або числа, а значення можуть бути будь-якого типу.\n"
                "Щоб створити словник, використовуємо фігурні дужки. Наприклад:\n"
                "person = {name: Олена, age(: 30}\n"
                "Щоб додати новий елемент, просто присвоюємо значення новому ключу:\n"
                "person[city] = Київ\n"
                "Щоб змінити значення — звертаємось до ключа і присвоюємо нове:\n"
                "person[age] = 31\n"
                "Щоб видалити елемент, можна використати del:\n"
                "del person[name]\n"
                "або метод pop(), який ще й повертає значення:\n"
                "person.pop(city)\n"
            )
        print("Відповідь Пилипчук Єлизавети успішно додана до файлу.")
    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
    except PermissionError:
        print("Помилка: немає дозволу на запис у файл.")
    except Exception as e:
        print(f"Несподівана помилка: {e}")

third_answer()

# Четверте питання — Пилипчук Єлизавета
def fourth_question():
    try:
        with open("students_questions.txt", "a", encoding="utf-8") as file:
            file.write("\nПитання Пилипчук Єлизавети\n")
            file.write("4. Як у Python відкрити текстовий файл і прочитати його вміст?\n")
        print("Питання Пилипчук Єлизавети успішно додане до файлу.")
    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
    except PermissionError:
        print("Помилка: немає дозволу на запис у файл.")
    except Exception as e:
        print(f"Несподівана помилка: {e}")

fourth_question()

read_file()