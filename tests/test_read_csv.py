from typing import Any

import pandas as pd
import pytest

from src.operations import read_csv_operations


def test_read_csv_successfully(mocker: Any) -> None:
    """Тестируем корректность работы функции"""
    mock_read_csv = mocker.patch("pandas.read_csv")

    mock_df = pd.DataFrame(
        {
            "date": ["2023-01-15", "2023-01-16"],
            "amount": [1000, 50],
        }
    )

    mock_read_csv.return_value = mock_df
    result = read_csv_operations("test.csv")

    expected = [{"date": "2023-01-15", "amount": 1000}, {"date": "2023-01-16", "amount": 50}]
    assert result == expected
    mock_read_csv.assert_called_once_with("test.csv")


def test_read_csv_empty(mocker: Any) -> None:
    """Тестируем если на входе будет пустой файл"""
    mock_read_csv = mocker.patch("pandas.read_csv")
    mock_df = pd.DataFrame()

    mock_read_csv.return_value = mock_df

    result = read_csv_operations("test.csv")

    expected: list = []
    assert result == expected
    mock_read_csv.assert_called_once_with("test.csv")


def test_file_not_found(mocker: Any) -> None:
    """Тест ошибки файл не найден"""
    mock_read_csv = mocker.patch("pandas.read_csv")
    mock_read_csv.side_effect = FileNotFoundError("File not found")

    with pytest.raises(FileNotFoundError):
        read_csv_operations("test.csv")
        mock_read_csv.assert_called_once_with("test.csv")
