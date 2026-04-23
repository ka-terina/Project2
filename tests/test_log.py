import pytest
from src.decorators import log


def test_no_errors(capsys: pytest.CaptureFixture[str]) -> None:
    @log()
    def my_function(x: float, y: float) -> float:
        return x / y

    my_function(2, 2)
    captured = capsys.readouterr()
    assert captured.out == "Start work\nmy_function 1.0\nEnd work\n"


def test_error_zero(capsys: pytest.CaptureFixture[str]) -> None:
    @log()
    def my_function(x: float, y: float) -> float:
        return x / y

    my_function(2, 0)
    captured = capsys.readouterr()
    assert captured.out == "Start work\nmy_function error: ZeroDivisionError. Input: (2, 0), {}\nEnd work\n"


def test_no_error_output_to_file(capsys: pytest.CaptureFixture[str]) -> None:
    @log(filename="mylog.txt")
    def my_function(x: float, y: float) -> float:
        return x / y

    my_function(2, 2)
    captured = capsys.readouterr()
    assert captured.out == "Start work\nmy_function 1.0\nEnd work\n"
