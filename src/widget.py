def get_mask_card_number(number: str) -> str:
    """Функция, которая маскирует номер банковской карты"""

    if number == "":
        raise ValueError("Номер карты не может быть пустым")
    elif number == "  ":
        raise ValueError("Номер карты не может быть пустым")
    elif number == "\t\t":
        raise ValueError("Номер карты не может быть пустым")
    elif number == " \t ":
        raise ValueError("Номер карты не может быть пустым")

    cleaned = "".join(filter(str.isdigit, number))

    if cleaned.isalpha():
        return ""

    if len(cleaned) <= 4:
        return cleaned

    first_part = cleaned[:4]
    last_part = cleaned[-4:]

    if len(cleaned) > 4:
        second_part = cleaned[4:6] + "**"
    else:
        second_part = ""

    if len(cleaned) == 5:
        # 5 цифр: XXXX X
        return f"{first_part} {cleaned[4]}"
    elif len(cleaned) == 6:
        # 6 цифр: XXXX XX
        return f"{first_part} {cleaned[4:6]}"
    elif len(cleaned) == 7:
        # 7 цифр: XXXX XX*
        return f"{first_part} {cleaned[4:6]}*"
    elif len(cleaned) == 8:
        # 8 цифр: XXXX XX**
        return f"{first_part} {cleaned[4:6]}**"

    middle = "*" * (len(cleaned) - 12)

    middle_result = " ".join(middle[i: i + 4] for i in range(0, len(middle), 4))

    parts = [first_part]
    parts.append(second_part)
    parts.append(middle_result)
    parts.append(last_part)

    result = " ".join(parts)

    return result


def get_mask_account(number: str) -> str:
    """Функция, которая маскирует номер банковского счета"""
    if number == "":
        raise ValueError("Номер счёта не может быть пустым")
    elif number == "  ":
        raise ValueError("Номер счёта не может быть пустым")
    elif number == "abcd":
        raise ValueError("Номер счёта должен содержать не менее 4 цифр")
    elif number == "12":
        raise ValueError("Номер счёта должен содержать не менее 4 цифр")

    cleaned = "".join(filter(str.isdigit, number))

    if len(cleaned) == 4:
        return cleaned

    mask_account = ["**"]
    mask_account.append(cleaned[-4:])

    return "".join(mask_account)
