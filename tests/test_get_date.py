import pytest

from src.widget import get_date


@pytest.fixture
def valid_date() -> list:
    return [
        "2024-03-11T02:26:18.671407",
        "2026-10-10T02:26:18.671407",
        "2023-09-03T02:26:18.671407",
    ]


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
