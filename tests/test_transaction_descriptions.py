import pytest

from src.generators import transaction_descriptions


@pytest.fixture
def sample_transaction() -> list:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "description": "Перевод с карты на карту",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]


@pytest.mark.parametrize(
    "transactions, expected",
    [
        (
            [
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "description": "Перевод с карты на карту",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                }
            ],
            ["Перевод с карты на карту"],
        ),
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                }
            ],
            ["Перевод организации"],
        ),
    ],
)
def test_transaction(transactions: list, expected: str) -> None:
    """Тест корректной работы функции"""
    result = list(transaction_descriptions(transactions))
    assert result == expected


def test_empty_list() -> None:
    """Тест когда список пустой"""
    result = list(transaction_descriptions([]))
    assert result == []


def test_sample_transaction(sample_transaction: list) -> None:
    result = list(transaction_descriptions(sample_transaction))
    assert result == ["Перевод организации", "Перевод со счета на счет", "Перевод с карты на карту"]


def test_one_list() -> None:
    """Тест когда один список"""
    result = list(
        transaction_descriptions(
            [
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "description": "Перевод с карты на карту",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                }
            ]
        )
    )
    assert result == ["Перевод с карты на карту"]
