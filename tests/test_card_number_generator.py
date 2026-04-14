import pytest
from mypy.find_sources import create_source_list

from src.generators import card_number_generator

def test_card_number() ->None:
    """Тест на корректную работу функции"""
    result = list(card_number_generator(1, 5))
    assert result == ["0000 0000 0000 0001",
                      "0000 0000 0000 0002",
                      "0000 0000 0000 0003",
                      "0000 0000 0000 0004",
                      "0000 0000 0000 0005"]

def test_invalid_number() -> None:
    """Не корректный диапазон"""
    result = list(card_number_generator(0,2))
    assert result == ["0000 0000 0000 0001", "0000 0000 0000 0002"]


