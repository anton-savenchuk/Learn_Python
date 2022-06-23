####################################
# Шифр Цезаря  # TODO

# Шифр Цезаря (шифр сдвига) — один из самых простых и наиболее широко
# известных методов шифрования. Шифр Цезаря — это вид шифра подстановки,
# в котором каждый символ в открытом тексте заменяется символом,
# находящимся на некотором постоянном числе позиций левее или правее
# него в алфавите.

# Шифр подстановки — метод шифрования с заменой элементов исходного
# открытого текста другими, в соответствии с неким правилом.

# Например, в шифре со сдвигом вправо на 3 позиции символ A заменяется
# символом D, символ B — символом E, и так далее, до символа Z,
# заменяемого символом C.

# Шифр Цезаря легко взламывается и не имеет почти никакого практического
# применения.
# Математическая модель

# Если сопоставить каждый символ алфавита с его порядковым номером
# (нумеруя с 0), то шифрование и дешифрование можно выразить формулами
# модульной арифметики:

#  y = (x + k) mod  n,
#  x = (y - k) mod  n,
# где x — символ открытого текста, y — символ шифрованного текста,
# n — мощность алфавита (количество символов), а k — ключ.

# Под операцией mod подразумевается операция нахождения остатка.
# В языке Python для нахождения остатка от деления двух чисел, мы
# используем оператор %.

####################################
# Пример
# Шифрование с использованием ключа k = 3. Буква «Е» «сдвигается» на
# три буквы вперед и становится буквой «З». Твердый знак, перемещенный
# на три буквы вперед, становится буквой «Э», буква «Я», перемещенная
# на три буквы вперед, становится буквой «В», и так далее:

# Исходный алфавит: А Б В Г Д Е Ё Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я
# Шифрованный:      Г Д Е Ё Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я А Б В

# Оригинальный текст:
# Съешь же ещё этих мягких французских булок, да выпей чаю.

# Шифрованный текст:
# Фэзыя йз зьи ахлш пвёнлш чугрщцкфнлш дцосн, жг еютзм ъгб.

####################################
# Описание проекта: требуется написать программу, способную шифровать и
# дешифровать текст в соответствии с алгоритмом Цезаря. Она должна
# запрашивать у пользователя следующие данные:

#     направление: шифрование или дешифрование;
#     язык алфавита: русский или английский;
#     шаг сдвига (со сдвигом вправо).

# Примечание 1. Считайте, что в русском языке 32 буквы (буква ё
# отсутствует).

# Примечание 2. Неалфавитные символы — знаки препинания, пробелы, цифры
# — не меняются.

# Примечание 3. Сохраните регистр символов. Например, текст: "Умом
# Россию не понять" при сдвиге на одну позицию вправо будет преобразован
# в: "Фнпн Спттйя ож рпоауэ".

# Составляющие проекта:

#     Целые числа (тип int);
#     Модульная арифметика;
#     Переменные;
#     Ввод / вывод данных (функции input() и print());
#     Условный оператор (if/elif/else);
#     Цикл for/while;
#     Строковые методы.
#
####################################

eng_alphabet = "abcdefghijklmnopqrstuvwxyz"
rus_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"


def is_encryption(string: str) -> bool:
    """Determine what needs to be done."""
    while True:
        ans = input(string)
        if ans.lower() in {"шифрование", "ш", "encryption", "e"}:
            return True
        elif ans.lower() in {"дешифрование", "д", "decryption", "d"}:
            return False
        else:
            print("\nНе понял, попробуй еще раз.")


def is_language(string: str) -> str:
    """Determine which alphabet to work with."""
    while True:
        ans = input(string)
        if ans.lower() in {"английский", "анг", "а", "english", "eng", "e"}:
            return eng_alphabet
        elif ans.lower() in {"русский", "рус", "р", "russian", "rus", "r"}:
            return rus_alphabet
        else:
            print("\nНе понял, попробуй еще раз.")


def is_route(string: str) -> bool:
    """Determine the direction of the alphabet."""
    while True:
        ans = input(string)
        if ans.lower() in {"влево", "лево", "л", "left", "l"}:
            return True
        elif ans.lower() in {"вправо", "право", "п", "right", "r"}:
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


def get_encryption(row_string: str, key: int, alphabet: str) -> str:
    """Encrypt or decrypt the string using the key."""
    string_encryption = ""
    for letr in range(len(row_string)):
        if row_string[letr].isalpha():
            temp_letr = alphabet[alphabet.find(row_string[letr].lower()) - key]
            string_encryption += (
                temp_letr if row_string[letr].islower() else temp_letr.upper()
            )
        else:
            string_encryption += row_string[letr]

    return string_encryption


def caesars_cipher():
    """Encrypt by substitution - replace the elements of a string with a shift.

    A type of substitution cipher in which each character in the
    plaintext is replaced by a character located some constant number of
    positions to the left or right of it in the alphabet.
    """
    route = (
        "encrypt"
        if is_encryption("\nШифруем или дешифруем? (Ш/Д):\n")
        else "decrypt"
    )

    alphabet = is_language("\nЯзык русский или английский? (Р/А):\n")

    key = is_digit("\nШаг сдвига? (целое число):\n")

    if route == "encrypt":  # redefine the direction of the alphabet
        alphabet = (
            alphabet
            if is_route("\nСдвигаем вправо или влево? (П/Л):\n")
            else alphabet[::-1]
        )
    else:
        alphabet = (
            alphabet[::-1]
            if is_route("\nСдвигаем вправо или влево? (П/Л):\n")
            else alphabet
        )

    row_string = input("\nВведите строку которую необходимо обработать:\n")
    print("\nРезультат выполнения операции:")
    return get_encryption(row_string, key, alphabet)


if __name__ == "__main__":
    print(caesars_cipher())
