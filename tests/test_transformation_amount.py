import os
from unittest.mock import Mock, patch

import pytest
from typing import Any

from src.external_api import transaction_amount


@patch("requests.request")
@patch("os.getenv", return_value=os.getenv("API_KEY"))
def test_usd_conversion(self: Any, mock_request: Any) -> None:
    """Проверка работы - успешная конвертация USD -> RUB"""
    mock_response = Mock()
    mock_response.json.return_value = {"result": 583723.699111}
    mock_request.return_value = mock_response

    transaction = {"operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}}}

    result = transaction_amount(transaction)

    expected_url = "https://api.apilayer.com/fixer/convert?to=RUB&from=USD&amount=8221.37"
    expected_headers = {"apikey": os.getenv("API_KEY")}
    mock_request.assert_called_once_with("GET", expected_url, headers=expected_headers)

    assert result == 583723.699111


@patch("requests.request")
@patch("os.getenv", return_value=os.getenv("API_KEY"))
def test_eur_conversion(self: Any, mock_request: Any) -> None:
    """Проверка работы - успешная конвертация EUR -> RUB"""
    mock_response = Mock()
    mock_response.json.return_value = {"result": 684120.085194}
    mock_request.return_value = mock_response

    transaction = {"operationAmount": {"amount": "8221.37", "currency": {"name": "EUR", "code": "EUR"}}}

    result = transaction_amount(transaction)

    expected_url = "https://api.apilayer.com/fixer/convert?to=RUB&from=EUR&amount=8221.37"
    expected_headers = {"apikey": os.getenv("API_KEY")}
    mock_request.assert_called_once_with("GET", expected_url, headers=expected_headers)

    assert result == 684120.085194


def test_rub_conversion() -> None:
    """Рубли - конвертация не нужна"""
    transaction = {"operationAmount": {"amount": "8221.37", "currency": {"name": "RUB", "code": "RUB"}}}

    result = transaction_amount(transaction)
    assert result == 8221.37


@patch("requests.request")
@patch("os.getenv", return_value=None)
def test_error(self: Any, mock_request: Any) -> None:
    """Отсутствие ключа вызывает ошибку"""
    mock_response = Mock()
    mock_response.json.side_effect = ValueError("result")
    mock_request.return_value = mock_response

    transaction = {"operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}}}
    with pytest.raises(ValueError):
        transaction_amount(transaction)


@patch("requests.request")
@patch("os.getenv", return_value="test_key")
def test_api_error(self: Any, mock_request: Any) -> None:
    """Проверка ошибок"""
    mock_response = Mock()
    mock_response.json.side_effect = KeyError("result")
    mock_request.return_value = mock_response

    transaction = {"operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}}}

    with pytest.raises(KeyError):
        transaction_amount(transaction)


def test_invalid_transaction() -> None:
    """Некорректная структура транзакции"""
    transaction = {"invalid": "data"}
    with pytest.raises(KeyError):
        transaction_amount(transaction)
