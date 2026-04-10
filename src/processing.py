def filter_by_state(new_lst: list, state: str = "EXECUTED") -> list:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    """
    if new_lst == []:
        return []


    result = []
    for i in new_lst:
        if not isinstance(i, dict):
            raise KeyError
        if i["state"] == state:
            result.append(i)

    return result


def sort_by_date(new_lst: list, reverse: bool = True) -> list:
    """Функция возвращает новый список сортированный по дате"""
    result = sorted(new_lst, key=lambda x: x["date"], reverse=reverse)

    return result
