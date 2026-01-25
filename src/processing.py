def filter_by_state(new_lst: list, state="EXECUTED": str) -> list:
    """Функция возвращает новый список словарей, содержащий только те
    словари, у которых ключ state соответствует указанному значению"""
    result = []
    for i in new_lst:
        if i["state"] == state:
            result.append(i)

    return result


def sort_by_date(new_lst: list, reverse=True: bool) -> list:
    """Функция возвращает новый список сортированный по дате"""
    if reverse == True:
        result = sorted(new_lst, key=lambda x: x["date"], reverse=True)
    else:
        result = sorted(new_lst, key=lambda x: x["date"], reverse=False)

    return result
