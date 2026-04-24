import pytest
from src.decorators import log


def test_no_errors(capsys: pytest.CaptureFixture[str]) -> None:
    @log()
    def my_function(x: float, y: float) -> float:
        return x / y

    my_function(2, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function 1.0\n"


def test_error_zero(capsys: pytest.CaptureFixture[str]) -> None:
    @log()
    def my_function(x: float, y: float) -> float:
        return x / y

    my_function(2, 0)
    captured = capsys.readouterr()
    assert captured.out == "my_function error: ZeroDivisionError. Input: (2, 0), {}\n"


def test_no_error_output_to_file(capsys: pytest.CaptureFixture[str]) -> None:
    @log(filename="mylog.txt")
    def my_function(x: float, y: float) -> float:
        return x / y

    my_function(2, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function 1.0\n"
