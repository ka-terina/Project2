import pytest

from src.masks import get_mask_account


@pytest.fixture
def valid_account_numbers():
    """Валидные номера счетов в разных форматах."""
    return [
        "123456789012",  # 12 цифр
        "RU12 3456 7890 1234",  # 16 цифр, буквы + пробелы
        "DE43-2109-8765-4321",  # 16 цифр, дефисы
        "GB82TESC12345698765432",  # 22 цифры, буквы
        " 7777 8888 9999 ",  # 12 цифр, пробелы
        "0000111122223333",  # 16 цифр, нули
    ]


@pytest.fixture
def invalid_account_numbers():
    """Некорректные номера счетов."""
    return [
        "",  # пустая строка
        "   ",  # пробелы
        "abcd",  # нет цифр
        "12",  # < 4 цифр
    ]


@pytest.mark.parametrize(
    "input_number,expected",
    [
        ("123456789012", "**9012"),
        ("RU12 3456 7890 1234", "**1234"),
        ("DE43-2109-8765-4321", "**4321"),
        ("GB82TESC12345698765432", "**5432"),
        (" 7777 8888 9999 ", "**9999"),
        ("0000111122223333", "**3333"),
    ],
)
def test_valid_masking(input_number, expected, valid_account_numbers):
    """Проверка корректного маскирования валидных номеров."""
    result = get_mask_account(input_number)
    assert result == expected


def test_empty_string_raises_error(invalid_account_numbers):
    """Пустая строка или пробелы → ошибка."""
    with pytest.raises(ValueError, match="Номер счёта не может быть пустым"):
        get_mask_account("")


def test_non_digit_string_raises_error(invalid_account_numbers):
    """Строка без цифр → ошибка."""
    with pytest.raises(ValueError, match="Номер счёта должен содержать не менее 4 цифр"):
        get_mask_account("abcd")


def test_too_short_number_raises_error(invalid_account_numbers):
    """Номера короче 4 цифр → ошибка."""
    with pytest.raises(ValueError, match="Номер счёта должен содержать не менее 4 цифр"):
        get_mask_account("12")
