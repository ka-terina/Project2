import pytest

from src.widget import mask_account_card


@pytest.fixture
def valid_card_numbers():
    return [
        "Visa 4276 1234 5678 9012",
        "MasterCard 5105 1051 0510 5100",
        "Visa4111111111111111",
        "MasterCard5555555555554444",
    ]

@pytest.fixture
def valid_account_numbers():
    return [
        "Счет40817810099910004312",
        "Счет 40702810700000000012",
    ]

@pytest.fixture
def invalid_inputs():
    return [
        "",                     # пустая строка
        "123",                  # слишком короткая
        "abc def ghi",          # буквы и пробелы
        "!@#$%^&*()",          # спецсимволы
    ]

@pytest.mark.parametrize("card_number,expected_mask", [
    ("Visa Platinum 4276 1234 5678 9012", "Visa Platinum 4276 12** **** 9012"),
    ("Visa 5105 1051 0510 5100", "Visa 5105 10** **** 5100"),
    ("MasterCard 6011 1111 1111 1117", "MasterCard 6011 11** **** 1117"),
    ("Visa4111111111111111", "Visa 4111 11** **** 1111"),
    ("Visa5555555555554444", "Visa 5555 55** **** 4444"),
])
def test_mask_card(card, expected, valid_card_number):
    """Проверяет маскировку номеров карт."""
    result = mask_account_card(card)
    assert result == expected

@pytest.mark.parametrize("account,expected", [
    ("Cчет 12345678901234567890", "Счет **7890"),
    ("Счет00000000000000000001", "Счет **0001"),
    ("Счет 9999 9999 9999 9999 9999", "Счет **9999"),
])
def test_mask_account(account, expected, valid_account_numbers):
    """Проверяет маскировку номеров счетов."""
    result = mask_account_card(account)
    assert result == expected

def test_error(invalid_inputs):
    """Проверка ошибок"""
    with pytest.raises(ValueError, match="Некорректный ввод"):
        mask_account_card(invalid_inputs)

