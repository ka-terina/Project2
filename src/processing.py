def filter_by_state(new_lst: list, state="EXECUTED") -> list:
    """Функция возвращает новый список словарей, содержащий только те
    словари, у которых ключ state соответствует указанному значению"""
    result = []
    for i in new_lst:
        if i["state"] == state:
            result.append(i)

    return result


def sort_by_date(new_lst: list, reverse=True) -> list:
    """Функция возвращает новый список сортированный по дате"""
    result = sorted(new_lst, key=lambda x: x["date"], reverse=True)

    return result


new_lst = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
print(sort_by_date(new_lst))
