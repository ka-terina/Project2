import pytest

from src.widget import get_date


@pytest.fixture
def valid_date():
    return[
        "2024-03-11T02:26:18.671407",
        "2026-10-10T02:26:18.671407",
        "2023-09-03T02:26:18.671407",
    ]

@pytest.fixture
def invalid_inputs():
    return [
        "",  # пустая строка
        "123",  # слишком короткая
        "abc def ghi",  # буквы и пробелы
        "!@#$%^&*()",  # спецсимволы
    ]

@pytest.mark.parametrize(
    "date","expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2026-10-10T02:26:18.671407", "10.10.2026"),
        ("2023-09-03T02:26:18.671407", "03.09.2023")
    ]
)

def test_get_date(date, expected, valid_date):
    """Проверяем маскировку даты"""
    result = get_date(date)
    assert result == expected

def test_error(invalid_inputs):
    """Проверка ошибок"""
    with pytest.raises(ValueError, match="Некорректный ввод"):
        get_date(invalid_inputs)

