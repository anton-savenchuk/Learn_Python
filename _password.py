"""Генератор безопасных паролей.
------
Описание проекта: программа генерирует заданное количество паролей и
включает в себя умную настройку на длину пароля, а также на то, какие
символы требуется в него включить, а какие исключить.

Составляющие проекта:
------
- Целые числа (тип int);
- Переменные;
- Ввод / вывод данных (функции input() и print());
- Условный оператор (if/elif/else);
- Цикл for;
- Написание пользовательских функций;
- Работа с модулем random для генерации случайных чисел.

Заголовок программы:
------
- Подключите модуль random;
- Создайте строковые константы:
  - digits: 0123456789;
  - lowercase_letters: abcdefghijklmnopqrstuvwxyz;
  - uppercase_letters: ABCDEFGHIJKLMNOPQRSTUVWXYZ;
  - punctuation: !#$%&*+-=?@^_.
- Создайте переменную chars = '', которая будет содержать все
символы, которые могут быть в генерируемом пароле.

Считывание пользовательских данных:
------
Программа должна запрашивать у пользователя следующую информацию:
- Количество паролей для генерации;
- Длину одного пароля;
- Включать ли цифры 0123456789?
- Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?
- Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?
- Включать ли символы !#$%&*+-=?@^_?
- Исключать ли неоднозначные символы il1Lo0O?

Настройка генерируемых паролей:
------
На основании введенной пользователем информации, сформируйте
переменную chars, содержащую все символы, которые могут быть в
генерируемом пароле.

Генерации пароля:
------
Напишите функцию generate_password(), которая принимает два аргумента:
- length: длину пароля;
- chars: алфавит из символов которого состоит пароль;
и возвращает пароль.

Используя цикл for, сгенерируйте необходимое количество паролей.
"""

from random import sample


digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_."


def is_valid_answer(string: str) -> bool:
    """Check user answer."""
    while True:
        ans = input(string)
        if ans.lower() in {"да", "д", "yes", "y"}:
            return True
        elif ans.lower() in {"нет", "н", "no", "n"}:
            return False
        else:
            print("\nНе понял, попробуй еще раз.")


def is_digit(string: str) -> bool:
    """Check it digit."""
    while True:
        ans = input(string)
        if ans.isdigit() and ans != "0":
            return int(ans)
        else:
            print("\nНе понял, попробуй еще раз.")


def is_replace(string: str) -> str:
    """Replace ambiguous symbols."""
    for symbol in "il1Lo0O":
        if symbol in string:
            string = string.replace(symbol, "")

    return string


def generate_password(string: str, lenght: int) -> str:
    """Generate user password."""
    return "".join(sample(string, lenght))


def get_password():
    """Generate the specified number of passwords.

    Includes a smart setting for the length of the password, which
    characters include in it, and which ones to exclude.
    """
    chars = ""

    quantity_pass = is_digit("Количество паролей для генерации?:\n")
    lenght_pass = is_digit("\nМинимальная длина одного пароля?:\n")

    if is_valid_answer("\nИспользовать цифры 0123456789? (Да/Нет):\n") is True:
        chars += digits

    if is_valid_answer("\nИспользовать прописные буквы ABCD...YZ? (Да/Нет):\n") is True:
        chars += uppercase_letters

    if is_valid_answer("\nИспользовать строчные буквы abcd...yz? (Да/Нет):\n") is True:
        chars += lowercase_letters

    if is_valid_answer("\nИспользовать символы !#$%&*+-=?@^_? (Да/Нет):\n") is True:
        chars += punctuation

    if is_valid_answer("\nУбрать неоднозначные символы il1Lo0O? (Да/Нет):\n") is True:
        chars = is_replace(chars)

    if len(chars) == 0:
        return "\nПустой пароль не самый надёжный!"

    print()
    for _ in range(quantity_pass):
        print(generate_password(chars, lenght_pass))

    return "\nВозвращайся, если нужны ещё пароли."


if __name__ == "__main__":
    print(get_password())
