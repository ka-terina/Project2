def mask_account_card(account_card: str) -> str:
    """Функция, которая маскирует номер карты или номер счета"""
    if account_card == "":
        raise ValueError("Номер карты не может быть пустым")
    elif account_card == "  ":
        raise ValueError("Номер карты не может быть пустым")
    elif account_card == "\t\t":
        raise ValueError("Номер карты не может быть пустым")
    elif account_card == " \t ":
        raise ValueError("Номер карты не может быть пустым")

    if account_card.isalpha():
        return ""

    # Шаг 1. Извлекаем все цифры и запоминаем их позиции
    digits = []
    digit_positions = []

    for i, char in enumerate(account_card):
        if char.isdigit():
            digits.append(char)
            digit_positions.append(i)

    if not digits:
        # Если цифр нет, возвращаем исходную строку
        return account_card

    digits_str = "".join(digits)
    num_digits = len(digits_str)

    # Шаг 2. Определяем тип: счёт или карта
    is_account = num_digits >= 20

    # Шаг 3. Создаём замаскированную версию цифр
    if is_account:
        # Для счёта: ** + последние 4 цифры
        masked_digits = f"**{digits_str[-4:]}"
    else:

        if num_digits <= 20:
            start_part = digits_str[:6]
            end_part = digits_str[-4:]
            masked_count = num_digits - 10
            masked_part = start_part + ("*" * masked_count) + end_part

        # Для карты: первые 6 + маскированные + последние 4
        if num_digits == 5:
            # 5 цифр: XXXX X
            return account_card[: digit_positions[0]] + " " + digits_str[:4] + " " + digits_str[4]
        elif num_digits == 6:
            # 6 цифр: XXXX XX
            return account_card[: digit_positions[0]] + " " + digits_str[:4] + " " + digits_str[4:6]
        elif num_digits == 7:
            # 7 цифр: XXXX XX*
            return account_card[: digit_positions[0]] + " " + digits_str[:4] + " " + digits_str[4:6] + "*"
        elif num_digits == 8:
            # 8 цифр: XXXX XX**
            return account_card[: digit_positions[0]] + " " + digits_str[:4] + " " + digits_str[4:6] + "**"

        # Группируем по 4 символа
        groups = []
        for i in range(0, len(masked_part), 4):
            groups.append(masked_part[i: i + 4])
        masked_digits = " ".join(groups)

    # Шаг 4. Заменяем цифры в исходной строке на замаскированные
    # Берём часть строки до первой цифры
    before_digits = account_card[: digit_positions[0]]
    # Берём часть строки после последней цифры
    after_digits = account_card[digit_positions[-1] + 1:]

    # Формируем итоговую строку
    result = before_digits + masked_digits + after_digits

    return result


def get_date(date: str) -> str:
    """Функция, которая выводит дату из полученной строки"""
    if date == "":
        raise ValueError("Строка не может быть пустой")
    elif date == "  ":
        raise ValueError("Строка не может быть пустой")

    if len(date) <= 4:
        raise IndexError("Строка слишком короткая")

    lst_date = list(str(date))
    day = lst_date[8:10]
    month = lst_date[5:7]
    year = lst_date[:4]
    result_date = day + ["."] + month + ["."] + year

    result = "".join(str(item) for sublist in result_date for item in sublist)

    return result
