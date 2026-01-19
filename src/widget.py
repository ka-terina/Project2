from mypy.modulefinder import load_stdlib_py_versions


def mask_account_card(account_card: str) -> str:
    """Функция, которая маскирует номер карты или номер счета """
    lst_account_card = list(str(account_card))
    mask_number = [] #список для маскировки номера счета
    mask_number_card = []  # список для маскировки номера карты
    if lst_account_card[0] == "С":
        mask_number.append(lst_account_card[:5])
        mask_number.append("**")
        mask_number.append(lst_account_card[-4:])
        result = ' '.join(str(item) for sublist in mask_number for item in sublist)
    else:
        index = -10
        for i in range(6):
            lst_account_card[index] = "*"
            index += 1
        mask_number_card.append(lst_account_card[:-16])
        index_1 = -16
        index_2 = -12
        for i in range(3):
            mask_number_card .append(lst_account_card[index_1:index_2])
            mask_number_card.append(" ")
            index_1 += 4
            index_2 += 4
        mask_number_card.append(lst_account_card[-4:])
        result = ' '.join(str(item) for sublist in mask_number_card for item in sublist)

    return result



