import pytest
from src.filter_transactions import process_bank_operations


@pytest.fixture
def sample_transactions() -> list:
    return [
        {"id": 939719570, "description": "Перевод", "category": "Продукты"},
        {"id": 142264268, "description": "Открытие вклада", "category": "Сбережения"},
        {"id": 1424564268, "description": "Перевод", "category": "Такси"},
    ]


@pytest.mark.parametrize(
    "file_path, category, expected",
    [
        (
            [
                {"id": 939719570, "description": "Перевод", "category": "Продукты"},
                {"id": 142264268, "description": "Открытие вклада", "category": "Сбережения"},
            ],
            ["Продукты", "Сбережения"],
            {"Продукты": 1, "Сбережения": 1},
        ),
        (
            [
                {"id": 142264268, "description": "Открытие вклада", "category": "Сбережения"},
                {"id": 1424564268, "description": "Перевод", "category": "Такси"},
            ],
            ["Такси", "Сбережения"],
            {"Такси": 1, "Сбережения": 1},
        ),
    ],
)
def test_sample_filter(file_path: list, category: list, expected: dict) -> None:
    """Корректная работа функции"""
    result = process_bank_operations(file_path, category)
    assert result == expected


def test_empty_list() -> None:
    """Проверка краевых случаев пустые списки"""
    result = process_bank_operations([], ["Такси", "Сбережения"])
    assert result == {"Такси": 0, "Сбережения": 0}


def test_not_category(sample_transactions: list) -> None:
    """Нет нужной категории"""
    result = process_bank_operations(sample_transactions, ["Вклады"])
    assert result == {"Вклады": 0}
