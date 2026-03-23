import pytest

from src.processing import sort_by_date

@pytest.fixture
def sample_transactions():
    return [
        {"id": 1, "date": "2023-01-15T10:30:00", "amount": 100},
        {"id": 2, "date": "2023-03-20T14:15:00", "amount": 200},
        {"id": 3, "date": "2023-02-10T09:45:00", "amount": 300},
        {"id": 4, "date": "2023-01-05T16:20:00", "amount": 400},
        {"id": 5, "date": "2023-04-25T11:10:00", "amount": 500}
    ]

@pytest.fixture
def empty_list():
    """Пустой список."""
    return []

@pytest.fixture
def single_item():
    """Список с одним элементом."""
    return [{"id": 1, "date": "2023-05-10T12:00:00", "amount": 150}]

@pytest.fixture
def same_dates():
    """Все элементы с одинаковой датой."""
    return [
        {"id": 1, "date": "2023-01-15T10:00:00", "amount": 100},
        {"id": 2, "date": "2023-01-15T10:00:00", "amount": 200},
        {"id": 3, "date": "2023-01-15T10:00:00", "amount": 300}
    ]

@pytest.mark.parametrize("reverse,expected_order", [
    (True, [5, 2, 3, 1, 4]),
    (False, [4, 1, 3, 2, 5])
])
def test_sort_by_date_with_reverse(sample_transactions, reverse, expected_order):
    """Тест сортировки с разными значениями параметра reverse."""
    result = sort_by_date(sample_transactions, reverse=reverse)
    result_ids = [item["id"] for item in result]
    assert result_ids == expected_order

@pytest.mark.parametrize("input_list,reverse,expected_length", [
    ([], True, 0),
    ([], False, 0),
    ([{"id": 1, "date": "2023-01-01T00:00:00"}], True, 1),
    ([{"id": 1, "date": "2023-01-01T00:00:00"}, {"id": 2, "date": "2023-01-02T00:00:00"}], False, 2)
])
def test_edge_cases(input_list, reverse, expected_length):
    """Тест краевых случаев: пустые списки, одиночные элементы."""
    result = sort_by_date(input_list, reverse=reverse)
    assert len(result) == expected_length

def test_default_parameter(sample_transactions):
    """Тест с параметром по умолчанию (reverse=True)."""
    result = sort_by_date(sample_transactions)  # без указания reverse
    result_ids = [item["id"] for item in result]
    assert result_ids == [5, 2, 3, 1, 4]  # ожидаемый порядок по убыванию даты

def test_empty_list_input(empty_list):
    """Тест на обработку пустого списка."""
    result = sort_by_date(empty_list, reverse=True)
    assert result == []

def test_single_item_list(single_item):
    """Тест для списка с одним элементом."""
    result = sort_by_date(single_item, reverse=True)
    assert result == single_item

def test_same_dates_case(same_dates):
    """Тест когда все элементы имеют одинаковую дату."""
    result = sort_by_date(same_dates, reverse=True)
    # При одинаковых датах порядок должен сохраняться
    assert result == same_dates

def test_original_list_unchanged(sample_transactions):
    """Тест что исходная коллекция не изменяется."""
    original_copy = sample_transactions.copy()
    result = sort_by_date(sample_transactions, reverse=True)
    # Проверяем, что исходный список не изменился
    assert sample_transactions == original_copy
    # И что результат — это новый список
    assert result is not sample_transactions

@pytest.mark.parametrize("data,reverse,expected_first_date", [
    (
        [
            {"date": "2023-01-01T00:00:00"},
            {"date": "2023-12-31T23:59:59"}
        ],
        True,
        "2023-12-31T23:59:59"
    ),
    (
        [
            {"date": "2023-01-01T00:00:00"},
            {"date": "2023-12-31T23:59:59"}
        ],
        False,
        "2023-01-01T00:00:00"
    )
])
def test_simple_cases(data, reverse, expected_first_date):
    """Простые тестовые случаи с минимальной структурой данных."""
    result = sort_by_date(data, reverse=reverse)
    assert result[0]["date"] == expected_first_date