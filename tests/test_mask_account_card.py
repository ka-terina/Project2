import pytest

from src.widget import mask_account_card


@pytest.fixture
def card_examples() -> list:
    """Фикстура с примерами номеров карт разной длины и форматов."""
    return [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("MasterCard 1234-5678-9012-3456", "MasterCard 1234 56** **** 3456"),
        ("Card: 1234.5678.9012.3456", "Card: 1234 56** **** 3456"),
        ("Discover 6011111111111117", "Discover 6011 11** **** 1117"),
    ]


@pytest.fixture
def account_examples() -> list:
    """Фикстура с примерами номеров счетов."""
    return [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Bank Account 12345678901234567890", "Bank Account **7890"),
        ("Account 12345678901234564305", "Account **4305"),
        ("Счёт 00001111222233334444", "Счёт **4444"),
    ]


@pytest.mark.parametrize(
    "input_text,expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("MasterCard 1234567890123456", "MasterCard 1234 56** **** 3456"),
        ("Card 1234-5678-9012-3456", "Card 1234 56** **** 3456"),
    ],
)
def test_card_masking_parametrized(input_text: str, expected: str) -> None:
    """Параметризованный тест для маскировки карт."""
    result = mask_account_card(input_text)
    assert result == expected


@pytest.mark.parametrize(
    "input_text,expected",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Bank Account 12345678901234567890", "Bank Account **7890"),
        ("Account 98765432109876543210", "Account **3210"),
    ],
)
def test_account_masking_parametrized(input_text: str, expected: str) -> None:
    """Параметризованный тест для маскировки счетов."""
    result = mask_account_card(input_text)
    assert result == expected


def test_card_examples(card_examples: list) -> None:
    """Тест примеров карт с использованием фикстуры."""
    for input_text, expected in card_examples:
        result = mask_account_card(input_text)
        assert result == expected


def test_account_examples(account_examples: list) -> None:
    """Тест примеров счетов с использованием фикстуры."""
    for input_text, expected in account_examples:
        result = mask_account_card(input_text)
        assert result == expected
