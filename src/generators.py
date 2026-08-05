from collections.abc import Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    """Фильтрует транзакции по заданной валюте"""

    for transaction in transactions:
        transaction_currency = transaction.get("currency_code", {})
        if transaction_currency == currency:
            yield transaction


def transaction_descriptions(transactions: list) -> Iterator[str]:
    """Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Выдает номера банковских карт в формате ХХХХ ХХХХ ХХХХ ХХХХ"""
    if start == 0:
        start += 1
    for num in range(start, stop + 1):
        num_str = str(num)
        num_str = "0" * (16 - len(num_str)) + num_str
        parts = [num_str[i: i + 4] for i in range(0, 16, 4)]
        formatted_card = " ".join(parts)
        yield formatted_card
