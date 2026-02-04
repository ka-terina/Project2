import pytest

from src.masks import get_mask_card_number


@pytest.fixture
def valid_card_number():
    """Возвращает список валидных номеров карт в разных форматах"""
    return [
        "1234567890123",  # 13 цифр
        "1234-5678-9012-345",  # 15 цифр, дефисы
        "4111 1111 1111 1111"  # 16 цифр, пробелы
        "1234.5678.9012.3456",  # точки как разделитель
        " 1234 5678 9012 3456 ",  # лишние пробелы
    ]


@pytest.fixture
def invalid_card_number():
    """Возвращает список некорректных номеров карт"""
    return [
        "",
        " ",
        "abcd",
        "123",
    ]


@pytest.mark.parametrize(
    "input_number, expected",
    [
        ("1234567890123", "1234 56** * 0123"),
        ("1234-5678-9012-345", "1234 56** *** 2345"),
        ("4111 1111 1111 1111", "4111 11** **** 1111"),
        ("1234.5678.9012.3456", "1234 56** **** 3456"),
        (" 1234 5678 9012 3456 ", "1234 56** **** 3456"),
    ],
)
def test_valid_masking(input_number, expected, valid_card_number):
    """Проверка корректного маскирования для валидных номеров"""
    result = get_mask_card_number(input_number)
    assert result == expected


def test_empty_string_raises_error(invalid_card_number):
    """Пустая строка или пробелы должна вызывать ошибку"""
    with pytest.raises(ValueError, match="Номер карты не может быть пустым"):
        get_mask_card_number("")
    with pytest.raises(ValueError, match="Номер карты не может быть пустым"):
        get_mask_card_number("  ")


def test_only_digits_no_formatting():
    """Проверка, что функция работает с чистой строкой цифр."""
    result = get_mask_card_number("1234567812345678")
    assert result == "1234 56** **** 5678"


def test_mixed_chars_with_digits():
    """Проверка строки с буквами и цифрами
    (остаются только цифры)."""
    result = get_mask_card_number("a1b2c3d4e5f6g7h8i9j0f1g2e3y4")
    assert result == "1234 56** ** 1234"
