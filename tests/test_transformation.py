from unittest.mock import mock_open, patch

from mypy.types_utils import AnyType

from src.utils import transformation


@patch("builtins.open", return_value=False)
def test_file_not_found(self: AnyType) -> None:
    """Проверка случая когда файл не найден"""
    result = transformation("missing.json")
    assert result == []


@patch("builtins.open", mock_open(read_data="[]"))
def test_empty_list() -> None:
    """Проверка если файл пустой"""
    result = transformation("text.json")
    assert result == []


@patch("builtins.open", mock_open(read_data='{"key": "value"}'))
def test_not_a_list() -> None:
    """Проверка если в файле данные не список"""
    result = transformation("text.json")
    assert result == []


@patch("pathlib.Path.exists", return_value=True)
@patch("builtins.open", side_effect=FileNotFoundError("File not found"))
@patch("builtins.open", side_effect=PermissionError("Permission denied"))
def test_error(self: AnyType, mock_file: AnyType, mock_exists: AnyType) -> None:
    """Проверка отработки различных ошибок"""
    result = transformation("text.json")
    assert result == []
