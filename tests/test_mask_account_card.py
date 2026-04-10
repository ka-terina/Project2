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


@pytest.fixture
def invalid_number() -> list:
    """Возвращает список некорректных номеров карт"""
    return [
        "",
        " ",
        "\t\t",
        "abcd",
        "123",
    ]

@pytest.fixture
def short_card_number() -> list:
    """Короткие номера карт"""
    return [
        "12345",
        "123456",
        "1234567",
        "12345678",
    ]

@pytest.mark.parametrize(
    "input_number, expected",
    [
        ("Visa12345","Visa 1234 5"),
        ("Visa123456", "Visa 1234 56"),
        ("Visa1234567", "Visa 1234 56*"),
        ("Visa12345678", "Visa 1234 56**"),
    ],
)
def test_5_8_digit_card(input_number: str, expected: str, short_card_number: list) -> None:
    """Проверка корректного маскирования для коротких номеров"""
    result = mask_account_card(input_number)
    assert result == expected

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

def test_empty_string_raises_error(invalid_number: list) -> None:
    """Пустая строка или пробелы должна вызывать ошибку"""
    with pytest.raises(ValueError, match="Номер карты не может быть пустым"):
        mask_account_card("")
    with pytest.raises(ValueError, match="Номер карты не может быть пустым"):
        mask_account_card("  ")

def test_tab_only(invalid_number: list) -> None:
    """Тест: строка из табуляций вызывает ValueError"""
    with pytest.raises(ValueError, match="Номер карты не может быть пустым"):
        mask_account_card("\t\t")

def test_mixed_whitespace(invalid_number: list) -> None:
    """Тест: смешанные пробелы и табуляции вызывают ValueError"""
    with pytest.raises(ValueError, match="Номер карты не может быть пустым"):
        mask_account_card(" \t ")

def test_non_digit_input() -> None:
    """Тест: ввод без цифр вызывает ошибку или возвращает пустую строку"""
    assert mask_account_card("abcd") == ""

def test_short_card_12_digits() -> None:
    """Тест: 12‑значный номер карты маскируется"""
    result = mask_account_card("123456789012")
    assert result == "1234 56** 9012"

def test_25_digit_account() -> None:
    """Тест: 25‑значный счёт маскируется"""
    result = mask_account_card("Счет 1234567890123456789012345")
    assert result == "Счет **2345"

