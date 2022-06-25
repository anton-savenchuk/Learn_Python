"""Угадайка чисел.
------

Описание проекта:
------
Программа генерирует случайное число в диапазоне от
1 до 100 и просит пользователя угадать это число. Если догадка
пользователя больше случайного числа, то программа должна вывести
сообщение 'Слишком много, попробуйте еще раз'. Если догадка меньше
случайного числа, то программа должна вывести сообщение 'Слишком мало,
попробуйте еще раз'. Если пользователь угадывает число, то программа
должна поздравить его и вывести сообщение 'Вы угадали, поздравляем!'.

Составляющие проекта:
------
- Целые числа (тип int);
- Переменные;
- Ввод / вывод данных (функции input() и print());
- Условный оператор (if/elif/else);
- Цикл while;
- Бесконечный цикл;
- Операторы break, continue;
- Работа с модулем random для генерации случайных чисел.

Оптимальная стратегия угадывания числа
------

Чтобы гарантированно угадать задуманное число от 1 до 100 потребуется не
более 7 попыток.

Оптимальный алгоритм угадывания: положим left = 1 и right = 100.

- Называем число, равное middle = (left + right) // 2;
- Если число middle равно задуманному числу, то мы угадали!;
- Если число middle меньше задуманного числа, то положим
left = middle + 1 и продолжим алгоритм;
- Если число middle больше задуманного числа, то положим
right = middle - 1 и продолжим алгоритм.

Поскольку на каждой итерации мы отбрасываем половину чисел, то
гарантировано угадаем задуманное число за величину, равную
log_2n (двоичный логарифм) округленную до целого в большую сторону.
При n = 100 получаем 7 попыток.
"""

from random import randrange


def is_valid(num: str, right_side=100) -> bool:
    """Проверяет корректность введённого целого числа.
    От 1 до right_side включительно.
    """
    return num.isdigit() and int(num) in range(1, right_side + 1)


def check_num(num: int, rand_num: int) -> tuple:
    """Проверяет совпадение загаданного числа и числа игрока."""
    if num == rand_num:
        return True, None
    elif num - rand_num > 5:
        return False, 0
    elif rand_num - num > 5:
        return False, 1
    elif abs(num - rand_num) <= 2:
        return False, 3
    else:
        return False, 2


def guess_num():
    r_side = input("Какое максимальное число могу загадать?\n")
    while is_valid(r_side, right_side=int(r_side)) is False:
        r_side = input("Нужно загадать целое число!\n")

    mesg = {
        "lets_go": f"Число от 1 до {r_side}(включительно) загадано.",
        "num_error": f"Нужно целое число от 1 до {r_side} (включительно).",
        "help": ("Слишком много", "Слишком мало", "Тепло", "Горячо"),
        "try_again": "попробуйте еще раз.",
        "case": ("ки", "ок"),
    }

    rand_num = randrange(1, int(r_side) + 1)
    print(f"\n{mesg['lets_go']}")

    cnt = 1
    while True:
        usr_num = input("Введите ваш вариант:\n")
        if is_valid(usr_num, right_side=int(r_side)) is False:
            print(f"{mesg['num_error']}, {mesg['try_again']}")
            continue
        else:
            ans, val = check_num(int(usr_num), rand_num)
            if ans is True:
                _try = (
                    f"попыт{mesg['case'][0]}"
                    if str(cnt)[-1] == "1" and cnt != 11
                    else f"попыт{mesg['case'][1]}"
                )
                return f"\nВы угадали число с {cnt} {_try}, поздравляю!"
            else:
                print(f"\n{mesg['help'][val]}, {mesg['try_again']}")

        cnt += 1


if __name__ == "__main__":
    print(guess_num())

while True:
    ans = input("Сыграем еще раз? (Да/Нет):\n")
    if ans.lower() in {"да", "д", "yes", "y"}:
        print(guess_num())
    elif ans.lower() in {"нет", "н", "no", "n"}:
        print("Спасибо, что играли в числовую угадайку. Ещё увидимся...")
        break
