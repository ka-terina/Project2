def filter_by_currency(transactions: list, currency: str) -> dict:
    """Фильтрует транзакции по заданной валюте"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["name"] == currency:
            yield transaction


def transaction_descriptions(transactions: list) -> str:
    """Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction["description"]

