import pytest

from src.masks import get_mask_card_number


@pytest.fixture
def valid_card_number() -> list:
    """Возвращает список валидных номеров карт в разных форматах"""
    return [
        "1234567890123",  # 13 цифр
        "1234-5678-9012-345",  # 15 цифр, дефисы
        "4111 1111 1111 1111"  # 16 цифр, пробелы
        "1234.5678.9012.3456",  # точки как разделитель
        " 1234 5678 9012 3456 ",  # лишние пробелы
    ]


@pytest.fixture
def invalid_card_number() -> list:
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
        ("1234567890123", "1234 56** * 0123"),
        ("1234-5678-9012-345", "1234 56** *** 2345"),
        ("4111 1111 1111 1111", "4111 11** **** 1111"),
        ("1234.5678.9012.3456", "1234 56** **** 3456"),
        (" 1234 5678 9012 3456 ", "1234 56** **** 3456"),
    ],
)
def test_valid_masking(input_number: str, expected: str, valid_card_number: list) -> None:
    """Проверка корректного маскирования для валидных номеров"""
    result = get_mask_card_number(input_number)
    assert result == expected


@pytest.mark.parametrize(
    "input_number, expected",
    [
        ("12345", "1234 5"),
        ("123456", "1234 56"),
        ("1234567", "1234 56*"),
        ("12345678", "1234 56**"),
    ],
)
def test_5_8_digit_card(input_number: str, expected: str, short_card_number: list) -> None:
    """Проверка корректного маскирования для коротких номеров"""
    result = get_mask_card_number(input_number)
    assert result == expected


def test_empty_string_raises_error(invalid_card_number: list) -> None:
    """Пустая строка или пробелы должна вызывать ошибку"""
    with pytest.raises(ValueError, match="Номер карты не может быть пустым"):
        get_mask_card_number("")
    with pytest.raises(ValueError, match="Номер карты не может быть пустым"):
        get_mask_card_number("  ")


def test_only_digits_no_formatting() -> None:
    """Проверка, что функция работает с чистой строкой цифр."""
    result = get_mask_card_number("1234567812345678")
    assert result == "1234 56** **** 5678"


def test_mixed_chars_with_digits() -> None:
    """Проверка строки с буквами и цифрами
    (остаются только цифры)."""
    result = get_mask_card_number("a1b2c3d4e5f6g7h8i9j0f1g2e3y4")
    assert result == "1234 56** ** 1234"


def test_tab_only(invalid_card_number: list) -> None:
    """Тест: строка из табуляций вызывает ValueError"""
    with pytest.raises(ValueError, match="Номер карты не может быть пустым"):
        get_mask_card_number("\t\t")


def test_mixed_whitespace(invalid_card_number: list) -> None:
    """Тест: смешанные пробелы и табуляции вызывают ValueError"""
    with pytest.raises(ValueError, match="Номер карты не может быть пустым"):
        get_mask_card_number(" \t ")


def test_short_number_1_digit() -> None:
    """Тест: номер из 1 цифры возвращается как есть"""
    assert get_mask_card_number("1") == "1"


def test_short_number_4_digits() -> None:
    """Тест: номер из 4 цифр возвращается как есть"""
    assert get_mask_card_number("1234") == "1234"


def test_non_digit_input(invalid_card_number: list) -> None:
    """Тест: ввод без цифр вызывает ошибку или возвращает пустую строку"""
    assert get_mask_card_number("abc def") == ""


def test_12_digit_card() -> None:
    """Тест: 12‑значный номер"""
    result = get_mask_card_number("123456789012")
    assert result == "1234 56**  9012"
