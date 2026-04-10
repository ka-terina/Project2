import pytest

from src.widget import get_date


@pytest.fixture
def valid_date() -> list:
    return [
        "2024-03-11T02:26:18.671407",
        "2026-10-10T02:26:18.671407",
        "2023-09-03T02:26:18.671407",
    ]


@pytest.fixture
def invalid_date() -> list:
    """Возвращает список некорректных номеров карт"""
    return [
        "",
        " ",
        "\t\t",
        "abcd",
        "123",
    ]

@pytest.fixture
def short_dates():
    """Фикстура с короткими строками (недостаточная длина)."""
    return ["2023", "202", "20", "2", ""]

@pytest.mark.parametrize(
    "date,expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2026-10-10T02:26:18.671407", "10.10.2026"),
        ("2023-09-03T02:26:18.671407", "03.09.2023"),
    ],
)
def test_get_date(date: str, expected: str, valid_date: bool) -> None:
    """Проверяем маскировку даты"""
    result = get_date(date)
    assert result == expected

def test_date_with_single_digit_day() -> None:
    """Тест: дата с однозначным днём (с ведущим нулём)"""
    result = get_date("2023-03-07")
    assert result == "07.03.2023"

def test_date_with_single_digit_month() -> None:
    """Тест: дата с однозначным месяцем (с ведущим нулём)"""
    result = get_date("2023-04-18")
    assert result == "18.04.2023"

def test_leap_year_date() -> None:
    """Тест: дата в високосном году"""
    result = get_date("2024-02-29")
    assert result == "29.02.2024"

def test_century_boundary_date() -> None:
    """Тест: дата на границе веков"""
    result = get_date("2000-12-31")
    assert result == "31.12.2000"

def test_early_year_date() -> None:
    """Тест: дата с ранним годом"""
    result = get_date("0001-01-01")
    assert result == "01.01.0001"

def test_string_with_date_like_pattern() -> None:
    """Тест: строка с похожим на дату шаблоном (но не дата)"""
    result = get_date("XXXX-XX-XX")
    assert result == "XX.XX.XXXX"

def test_empty_string_raises_error(invalid_date: list) -> None:
    """Пустая строка или пробелы должна вызывать ошибку"""
    with pytest.raises(ValueError, match="Строка не может быть пустой"):
        get_date("")
    with pytest.raises(ValueError, match="Строка не может быть пустой"):
        get_date("  ")

@pytest.mark.parametrize("short_date", [
    "2023",
    "202",
    "20",
    "2"
])
def test_short_strings_index_error(short_date) -> None:
    """Параметризованный тест для коротких строк (вызывают IndexError)."""
    with pytest.raises(IndexError):
        get_date(short_date)