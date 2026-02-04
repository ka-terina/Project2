def get_mask_card_number(number: str) -> str:
    """Функция, которая маскирует номер банковкой карты"""
    if number == "":
        raise ValueError("Номер карты не может быть пустым")
    elif number == "  ":
        raise ValueError("Номер карты не может быть пустым")

    cleaned = "".join(filter(str.isdigit, number))

    if len(cleaned) <= 4:
        return cleaned

    first_part = cleaned[:4]

    if len(cleaned) > 4:
        second_part = cleaned[4:6] + "**"
    else:
        second_part = ""

    middle = "*" * (len(cleaned) - 12)

    middle_result = " ".join(middle[i: i + 4] for i in range(0, len(middle), 4))

    last_part = cleaned[-4:]

    parts = [first_part]
    parts.append(str(second_part))
    parts.append(str(middle_result))
    parts.append(str(last_part))

    result = " ".join(parts)

    return result


print(get_mask_card_number("1234567890123"))


def get_mask_account(number: int) -> str:
    """Функция, которая маскирует номер банковского счета"""
    new_number = list(str(number))
    mask_account = ["*", "*"]
    mask_account.append("".join(new_number[-4:]))

    return "".join(mask_account)
