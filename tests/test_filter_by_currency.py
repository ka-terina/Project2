import pytest

from src.generators import filter_by_currency


@pytest.fixture
def sample_transactions() -> list:
    return [
        {"id": 939719570, "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}}},
        {"id": 142264268, "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}}},
        {"id": 1424564268, "operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}}},
        {"id": 4587984268, "operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}}},
    ]


@pytest.fixture
def not_currency() -> list:
    return [
        {"id": 1424564268, "operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}}},
        {"id": 4587984268, "operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}}},
    ]


@pytest.mark.parametrize(
    "input_list, currency, expected",
    [
        ([], "RUB", []),
        ([], "USD", []),
        (
            [
                {
                    "id": 1424564268,
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}},
                }
            ],
            "RUB",
            [
                {
                    "id": 1424564268,
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}},
                }
            ],
        ),
        (
            [{"id": 939719570, "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}}}],
            "RUB",
            [],
        ),
    ],
)
def test_edge_cases(input_list: list, currency: str, expected: list) -> None:
    """Тест краевых случаев: пустые списки, одиночные элементы."""
    result = list(filter_by_currency(input_list, currency))
    assert result == expected


def test_empty_list() -> None:
    """Тест краевых случаев пустые списки"""
    result = list(filter_by_currency([], "RUB"))
    assert result == []


def test_sample_transactions(sample_transactions: list) -> None:
    """Тест корректной фильтрации"""
    result = list(filter_by_currency(sample_transactions, "RUB"))
    assert result == [
        {"id": 1424564268, "operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}}},
        {"id": 4587984268, "operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}}},
    ]


def test_not_currency(not_currency: list) -> None:
    """Тест когда в списке нет нужной валюты"""
    result = list(filter_by_currency(not_currency, "USD"))
    assert result == []
