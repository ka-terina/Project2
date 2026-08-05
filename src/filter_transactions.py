import re


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Ищет в списке банковских операций те, у которых в описании (поле 'description')
    содержится заданная строка"""
    pattern = re.compile(search, re.IGNORECASE)

    result = []
    for operation in data:
        # проверяем есть ли поле discription и содержит ли оно искомую строку
        description = operation.get("description", "")
        if description and pattern.search(description):
            result.append(operation)

    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Подсчитывает количество операций в каждой категории и возвращает словарь"""
    # делаем словарь с нулями для всех категорий
    result = {category: 0 for category in categories}
    # подсчитываем операции
    for operation in data:
        category = operation.get("category")
        if category in result:
            result[category] += 1

    return result
