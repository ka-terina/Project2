def filter_by_state(new_lst: list, state="EXECUTED") -> list:
    """Функция возвращает новый список словарей, содержащий только те 
    словари, у которых ключ state соответствует указанному значению""" result = []
    for i in new_lst:
        if i["state"] == state:
            result.append(i)

    return result

