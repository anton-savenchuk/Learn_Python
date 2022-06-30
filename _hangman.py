"""Угадайка слов.
------

Описание проекта:
------
Программа загадывает слово, а пользователь должен его угадать.
Изначально все буквы слова неизвестны. Также рисуется виселица с петлей.
Пользователь предлагает букву, которая может входить в это слово. Если
такая буква есть в слове, то программа ставит букву столько раз, сколько
она встречается в слове. Если такой буквы нет, к виселице добавляется
круг в петле, изображающий голову. Пользователь продолжает отгадывать
буквы до тех пор, пока не отгадает всё слово. За каждую неудачную
попытку добавляется еще одна часть туловища висельника (обычно их 6:
голова, туловище, 2 руки и 2 ноги.

Составляющие проекта:
------
- Целые числа (тип int);
- Переменные;
- Ввод / вывод данных (функции input("",) и print("",));
- Условный оператор (if/elif/else);
- Цикл while;
- Бесконечный цикл;
- Операторы break, continue;
- Создание пользовательских функций;
- Списочные выражения;
- Работа с модулем random для генерации случайных чисел.
"""

from random import choice, shuffle


word_list = {
    "animal": (
        "Альпака", "Баран", "Бегемот", "Белка", "Броненосец", "Вомбат",
        "Голубь", "Горилла", "Горностай", "Дельфин", "Жираф", "Ирбис",
        "Касатка", "Квокка", "Коала", "Колибри", "Кошка", "Ласка", "Лебедь",
        "Лемур", "Ленивец ", "Леопард", "Лошадь", "Медведь", "Овечка",
        "Опоссум", "Панда", "Пеликан", "Песец", "Пингвин", "Сайгак", "Свинья",
        "Скворец", "Собака", "Сурикат", "Тюлень", "Фламинго", "Хамелеон ",
        "Шимпанзе", "Шиншилла",
    ),
    "building": (
        "Акрополь", "Алькатрас", "Амбуаз", "Амритсар", "Атомиум", "Веласка",
        "Гуггенхайм", "Джоканг", "Кааба", "Колизей", "Консьержери", "Крайслер",
        "Кремль", "Линкольн", "Лувр", "Мавзолей", "Марторана", "Метрополь",
        "Милуоки", "Мирадор", "Олимпийский", "Пантеон", "Парфенон", "Пентагон",
        "Петергоф", "Петронас", "Прамбанан", "Призма", "Рейксмузеум",
        "Рейхстаг", "Рюген", "Санджаклар", "Сорбонна", "Стейнвей", "Тайбэй",
        "Флэтайрон", "Фултон", "Хабитат", "Хофбург", "Эспланада",
    ),
    "cities": (
        "Амстердам", "Багдад", "Бангкок", "Барселона", "Богота", "Брюссель",
        "Будапешт", "Ванкувер", "Варшава", "Вашингтон", "Венеция", "Гонконг",
        "Даллас", "Джакарта", "Дубай", "Ибица", "Иерусалим", "Лагос", "Лондон",
        "Луанда", "Мадрид", "Майами", "Манила", "Мехико", "Москва", "Мумбаи",
        "Мюнхен", "Осака", "Париж", "Пекин", "Сантьяго", "Сингапур", "Стамбул",
        "Тегеран", "Токио", "Торонто", "Филадельфия", "Фукуока", "Чикаго",
        "Шанхай",
    ),
    "color": (
        "Аквамариновый", "Баклажановый", "Белый", "Ванильный", "Васильковый",
        "Гелиотроп", "Голубой", "Горчичный", "Желтый", "Зеленый", "Золотой",
        "Изумрудный", "Индиго", "Каштановый", "Кирпичный", "Коричневый",
        "Красный", "Кремовый", "Лазурный", "Лиловый", "Нефритовый",
        "Оливковый", "Оранжевый", "Персиковый", "Песочный", "Пурпурный",
        "Розовый", "Сангрия", "Сепия", "Серый", "Синий", "Сиреневый",
        "Сливовый", "Тыквенный", "Ультрамариновый", "Умбра", "Фиолетовый",
        "Фуксия", "Хаки", "Шоколадный",
    ),
    "food": (
        "Авокадо", "Ананас", "Апельсин", "Артишок", "Баклажан", "Банан",
        "Виноград", "Вишня", "Горох", "Гранат", "Груша", "Гуава", "Джекфрут",
        "Дуриан", "Капуста", "Карамбола", "Картофель", "Клубника", "Корнишон",
        "Кукуруза", "Лимон", "Лонган", "Манго", "Морковь", "Огурец", "Папайя",
        "Перец", "Персик", "Помело", "Помидор", "Рамбутан", "Редька",
        "Руккола", "Свекла", "Спаржа", "Томат", "Тыква", "Цуккини", "Шпинат",
        "Яблоко",
    ),
    "home": (
        "Антресоль", "Буфетница", "Ведро", "Вешалка", "Выключатель", "Дверь",
        "Диван", "Занавеска", "Зеркало", "Камин", "Картина", "Книга",
        "Колыбель", "Компьютер", "Кондиционер", "Кофемашина", "Кресло",
        "Кровать", "Лампочка", "Наволочка", "Обогреватель", "Подушка",
        "Этажерка", "Половик", "Раскладушка", "Светильник", "Сервант",
        "Скатерть", "Стеллаж", "Сундук", "Табурет", "Телевизор", "Трельяж",
        "Умывальник", "Унитаз", "Холодильник", "Швабра", "Шезлонг", "Ширма",
        "Шкафчик",
    ),
    "job": (
        "Авиадиспетчер", "Автомеханник", "Агроном", "Адвока", "Администратор",
        "Аналитик", "Аниматор", "Архитектор", "Банкир", "Бармен", "Биолог",
        "Брокер", "Бухгалтер", "Ветеринал", "Визажист", "Водитель",
        "Геодезист", "Дегустатор", "Диетолог", "Дизайнер", "Журналист",
        "Звукорежиссер", "Инструктор", "Искусствовед", "Кассир", "Кинолог",
        "Кондитер", "Копирайтер", "Косметолог", "Криминалист", "Лингвист",
        "Массажист", "Менеджер", "Нотариус", "Оператор", "Официант",
        "Парикмахер", "Программист", "Психотерапевт", "Строитель",
    ),
    "nature": (
        "Болото", "Ветер", "Вода", "Воздух", "Вулкан", "Гора", "Гроза",
        "Дерево", "Дождь", "Закат", "Звезда", "Земля", "Камень", "Каньон",
        "Кислород", "Космос", "Ледник", "Листва", "Минерал", "Молния",
        "Облако", "Огонь", "Озеро", "Океан", "Остров", "Песок", "Пещера",
        "Планета", "Пляж", "Пустыня", "Равнина", "Радуга", "Рассвет", "Река",
        "Снежинка", "Солнце", "Трава", "Туман", "Цветок", "Шторм",
    ),
    "sport": (
        "Акробатика", "Бильярд", "Бобслей", "Бодибилдинг", "Борьба", "Боулинг",
        "Волейбол", "Гандбол", "Гимнастика", "Гольф", "Гребля", "Дайвинг",
        "Дзюдо", "Каратэ", "Керлинг", "Киберспорт", "Кикбоксинг", "Коньки",
        "Крикет", "Лапта", "Мотоспорт", "Пауэрлифтинг", "Плавание",
        "Планеризм", "Прыжки", "Регби", "Рыболовство", "Скалолазание",
        "Скелетон", "Сноуборд", "Софтбол", "Стрельба", "Тхэквондо", "Теннис",
        "Триатлон", "Фехтование", "Фридайвинг", "Футбол", "Хоккей", "Шахматы",
    ),
    "transport": (
        "Аэростат", "Вагонетка", "Велосипед", "Вертолет", "Гироскутер",
        "Грузовик", "Дельтаплан", "Дирижабль", "Дрезина", "Картинг", "Катер",
        "Коньки", "Корабль", "Лайнер", "Лодка", "Лыжи", "Метро", "Моноколесо",
        "Монорельс", "Мотоцикл", "Параплан", "Паром", "Парусник", "Питбайк",
        "Подлодка", "Поезд", "Ракета", "Самокат", "Самолет", "Сигвей",
        "Скейтборд", "Скутер", "Снегоход", "Танкер", "Теплоход", "Трамвай",
        "Троллейбус", "Фуникулер", "Электричка", "Яхта",
    ),
}

messages = {
    "need_ltr": "\033[0;0;94m\nНужна буква русского алфавита.\033[0;0m",
    "used_ltr": "\033[0;0;93mТакая буква уже была!\n\033[0;0m",
    "used_ltrs": "\033[0;0;33mИСПОЛЬЗОВАННЫЕ БУКВЫ:\033[0;0m",
    "guessed_ltr": "\033[0;0;92mЕсть такая буква!\n\033[0;0m",
    "missing_ltr": "\033[0;0;91mНет такой буквы!\n\033[0;0m",
    "used_word": "\033[0;0;93mТакое слово уже было!\n\033[0;0m",
    "used_words": "\033[0;0;33mИСПОЛЬЗОВАННЫЕ СЛОВА:\033[0;0m",
    "guessed_word": "\033[0;0;92mВерное слово!\n\033[0;0m",
    "missing_word": "\033[0;0;91mНе верное слово!\n\033[0;0m",
    "user_win": "\033[32;1;42m   Вы выиграли, поздравляю!   \033[0;0m",
    "user_lose": "\033[31;1;41m   Вы проиграли!   \033[0;0m",
    "secret_word": "\033[0;0;95mЗАГАДАННЫМ СЛОВОМ, БЫЛО:\033[0;0m",
    "promt": "\033[0;0;96mПОДСКАЗКА:\033[0;0m",
    "try_again": "\033[0;0;94mНе понял, попробуй еще раз.\033[0;0m",
    "select_theme": "\033[0;0;95m\nВыбери тему, я загадаю слово:\033[0;0m",
    "select_level": "\033[0;0;95m\nВыбери сложность игры:\033[0;0m",
    "user_input": "\033[0;0;95m\nВведи букву или слово целиком: \033[0;0m",
}


def get_theme(_question: str) -> str:
    """Define question theme."""
    _themes = {
        "Животные": "animal",
        "Здания": "building",
        "Города": "cities",
        "Цвета": "color",
        "Еда": "food",
        "Дом": "home",
        "Работа": "job",
        "Природа": "nature",
        "Спорт": "sport",
        "Транспорт": "transport",
    }

    while True:
        _theme = input(f"{_question}\n{', '.join(_themes.keys())}\n").title()

        if _theme in _themes:
            return _themes[_theme]
        else:
            print(messages["try_again"])


def get_level(_question: str) -> str:
    """Check the level game."""
    _levels = {"Легкий": "low", "Средний": "medium", "Сложный": "hard"}

    while True:
        _level = input(f"{_question}\n{', '.join(_levels.keys())}\n").title()

        if _level.lower() in {"легкий", "л", "low", "l"}:
            return _levels["Легкий"]
        elif _level.lower() in {"средний", "ср", "medium", "m"}:
            return _levels["Средний"]
        elif _level.lower() in {"сложный", "сл", "hard", "h"}:
            return _levels["Сложный"]
        else:
            print(messages["try_again"])


def get_promt(_scrt_word: str, _promt=None) -> list:
    """Get a prompt by difficulty level."""
    _used_ltrs = []

    if not isinstance(_promt, type(None)):
        [_used_ltrs.append(ltr) for ltr in _promt if ltr not in _used_ltrs]

        return _used_ltrs

    if len(_scrt_word) <= 5:
        [
            _used_ltrs.append(ltr)
            for ltr in choice(_scrt_word)
            if ltr not in _used_ltrs and _scrt_word.count(ltr) == 1
        ]
    else:
        while len(_used_ltrs) != 2:
            [
                _used_ltrs.append(ltr)
                for ltr in choice(_scrt_word)
                if ltr not in _used_ltrs and _scrt_word.count(ltr) == 1
            ]

    return _used_ltrs


def get_word(_theme: str, _level: str) -> tuple:
    """Get random word by key "theme"."""
    _scrt_word = choice(word_list.get(_theme)).upper()
    _closed_ltrs = " * " * len(_scrt_word)

    if _level == "low":

        _promt = list(_scrt_word)
        shuffle(_promt)
        _used_ltrs = get_promt(_scrt_word, _promt)
        return _scrt_word, _closed_ltrs, _used_ltrs, "".join(_promt)

    elif _level == "medium":

        _used_ltrs = get_promt(_scrt_word)
        _closed_ltrs = get_open_ltr(_scrt_word, _used_ltrs)
        return _scrt_word, _closed_ltrs, _used_ltrs, None

    else:
        _used_ltrs = []
        return _scrt_word, _closed_ltrs, _used_ltrs, None


def get_open_ltr(_word: str, _ltrs: list) -> str:
    """Open a letter in a secret word."""
    return "".join(f" {_ltr} " if _ltr in _ltrs else " * " for _ltr in _word)


def is_valid_alpha(_question: str) -> str:
    """Check the correctness of the entered word or letter."""
    while True:
        _usr_ans = input(_question)

        if _usr_ans not in "abcdefghijklmnopqrstuvwxyz" and _usr_ans.isalpha():
            return _usr_ans
        else:
            print(messages["need_ltr"])


def is_valid_answer(_question: str) -> bool:
    """Check user answer."""
    while True:
        _ans = input(_question)

        if _ans.lower() in {"да", "д", "yes", "y", ""}:
            return True
        elif _ans.lower() in {"нет", "н", "no", "n"}:
            return False
        else:
            print(messages["try_again"])


def is_ltr(
    _scrt_word: str,
    _usr_ans: str,
    _closed_ltrs: str,
    _used_ltrs: list,
    _tries: int,
) -> tuple:
    """Check a letr in a secret word."""
    if _usr_ans in _used_ltrs:
        print(messages["used_ltr"])

    elif _usr_ans in _scrt_word:

        print(messages["guessed_ltr"])
        _used_ltrs.append(_usr_ans)
        _closed_ltrs = get_open_ltr(_scrt_word, _used_ltrs)

    else:
        print(messages["missing_ltr"])
        _tries -= 1
        _used_ltrs.append(_usr_ans)

    return _closed_ltrs, _used_ltrs, _tries


def is_word(
    _scrt_word: str,
    _usr_ans: str,
    _closed_ltrs: str,
    _used_ltrs: list,
    _used_words: list,
    _tries: int,
) -> tuple:
    """Check word matches secret word."""
    if _usr_ans in _used_words:
        print(messages["used_word"])

    elif _usr_ans == _scrt_word:

        print(messages["guessed_word"])
        _used_words.append(_usr_ans)
        [_used_ltrs.append(ltr) for ltr in _usr_ans if ltr not in _used_ltrs]
        _closed_ltrs = get_open_ltr(_scrt_word, _used_ltrs)

    else:

        print(messages["missing_word"])
        _tries -= 1
        _used_words.append(_usr_ans)

    return _closed_ltrs, _used_ltrs, _used_words, _tries


def get_lives(_tries: int, _level: str) -> str:
    """Display the number of remaining attempts."""
    if _level in {"low", "medium"}:
        _stages = [
            ("\U0001f90D " * 3),  # 0 tries, game over
            ("\u2764\uFE0F  " * 1 + "\U0001f90D " * 2),
            ("\u2764\uFE0F  " * 2 + "\U0001f90D " * 1),
            ("\u2764\uFE0F  " * 3),  # 3 tries, game start
        ]
    else:
        _stages = [
            ("\U0001f90D " * 6),  # 0 tries, game over
            ("\u2764\uFE0F  " * 1 + "\U0001f90D " * 5),
            ("\u2764\uFE0F  " * 2 + "\U0001f90D " * 4),
            ("\u2764\uFE0F  " * 3 + "\U0001f90D " * 3),
            ("\u2764\uFE0F  " * 4 + "\U0001f90D " * 2),
            ("\u2764\uFE0F  " * 5 + "\U0001f90D " * 1),
            ("\u2764\uFE0F  " * 6),  # 6 tries, game start
        ]

    return _stages[_tries]


def get_game_stats(
    _closed_ltrs: str,
    _lives: str,
    _used_ltrs: list,
    _used_words: list,
    _promt: str,
):
    """Display the current state game."""
    _len_word = len(_closed_ltrs)

    _used_ltrs = ", ".join(_used_ltrs)
    _used_words = ", ".join(_used_words)

    print(f"+{'-' * _len_word}+")
    print(f"|{_closed_ltrs}|   ПОПЫТКИ: {_lives}")
    print(f"+{'-' * _len_word}+")

    print(messages["used_ltrs"], _used_ltrs)
    print(messages["used_words"], _used_words)

    if not isinstance(_promt, type(None)):
        print(messages["promt"], _promt, "(отгадай слово)")


def get_play() -> tuple:
    """Play the game.

    The main part of the module.
    """
    _theme = get_theme(messages["select_theme"])
    _level = get_level(messages["select_level"])
    _used_words = []
    _scrt_word, _closed_ltrs, _used_ltrs, _promt = get_word(_theme, _level)
    _tries = 3 if _level in {"low", "medium"} else 6  # total tries

    print(f"\033[0;0;96m\nУ тебя {_tries} попыток, отгадай слово!\033[0;0m")

    while True:
        _lives = get_lives(_tries, _level)
        get_game_stats(_closed_ltrs, _lives, _used_ltrs, _used_words, _promt)

        _usr_ans = is_valid_alpha(messages["user_input"]).upper()

        if len(_usr_ans) not in [1, len(_scrt_word)]:
            pass

        elif len(_usr_ans) == 1:

            _closed_ltrs, _used_ltrs, _tries = is_ltr(
                _scrt_word, _usr_ans, _closed_ltrs, _used_ltrs, _tries
            )

        else:
            _closed_ltrs, _used_ltrs, _used_words, _tries = is_word(
                _scrt_word, _usr_ans, _closed_ltrs, _used_ltrs, _used_words, _tries
            )

        if _usr_ans == _scrt_word or "".join(_closed_ltrs.split()) == _scrt_word:

            _lives = get_lives(_tries, _level)
            get_game_stats(_closed_ltrs, _lives, _used_ltrs, _used_words, _promt)
            return True, _scrt_word  # user win

        elif _tries == 0:

            _lives = get_lives(_tries, _level)
            get_game_stats(_closed_ltrs, _lives, _used_ltrs, _used_words, _promt)
            return False, _scrt_word  # user lose

        continue


def is_game():
    """Welcome in game.

    Meet the user and offer to play the game.
    """
    _usr_name = input("Как тебя зовут?\n")

    print(f"\nПривет {_usr_name.title()}, давай играть в угадайку слов!")

    while True:
        _bool, _scrt_word = get_play()  # get game result

        if _bool is True:
            print()
            print(messages["user_win"])
        else:
            print()
            print(messages["user_lose"])
            print(messages["secret_word"], _scrt_word)

        if is_valid_answer("\nСыграем ещё? (Да/нет):\n") is True:
            continue

        break

    return print("Спасибо за игру!")


if __name__ == "__main__":
    is_game()
