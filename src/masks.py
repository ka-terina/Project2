def get_mask_card_number(number: int) -> str:
    """Функция, которая маскирует номер банковкой карты"""
    lst_number = list(str(number))
    mask_number = []
    a = 0
    b = 4
    for i in range(4):
        mask_number.append(lst_number[a:b])
        mask_number.append([" "])
        a += 4
        b += 4
    mask_number[2][2:] = ["**"]
    mask_number[4] = ["****"]

    for i in range(len(mask_number)):
        mask_number[i] = "".join(mask_number[i])

    return "".join(mask_number)


def get_mask_account(number: int) -> str:
    """Функция, которая маскирует номер банковского счета"""
    new_number = list(str(number))
    mask_account = ["*", "*"]
    mask_account.append("".join(new_number[-4:]))

    return "".join(mask_account)
