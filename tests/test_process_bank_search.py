import pytest
from src.filter_transactions import process_bank_search


@pytest.fixture
def sample_transactions() -> list:
    return [
        {"id": 939719570, "description": "Перевод"},
        {"id": 142264268, "description": "Открытие вклада"},
        {"id": 1424564268, "description": "Перевод"},
    ]


@pytest.mark.parametrize(
    "file_path, word, expected",
    [
        (
            [{"id": 939719570, "description": "Перевод"}, {"id": 142264268, "description": "Открытие вклада"}],
            "перевод",
            [{"id": 939719570, "description": "Перевод"}],
        ),
        (
            [{"id": 939719570, "description": "Перевод"}, {"id": 142264268, "description": "Открытие вклада"}],
            "Открытие вклада",
            [{"id": 142264268, "description": "Открытие вклада"}],
        ),
    ],
)
def test_sample_transactions(file_path: list, word: str, expected: list) -> None:
    """Проверка корректности работы функции"""
    result = process_bank_search(file_path, word)
    assert result == expected


def test_empty_list() -> None:
    """Проверка краевых случаев пустые списки"""
    result = process_bank_search([], "вклад")
    assert result == []


def test_not_word(sample_transactions: list) -> None:
    """Нет нужного слова в описании"""
    result = process_bank_search(sample_transactions, "счет")
    assert result == []
