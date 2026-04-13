import pytest

from src.processing import filter_by_state


@pytest.fixture
def sample_transactions() -> list:
    return [
        {"id": 1, "state": "EXECUTED", "amount": 100},
        {"id": 2, "state": "PENDING", "amount": 200},
        {"id": 3, "state": "EXECUTED", "amount": 300},
        {"id": 4, "state": "CANCELED", "amount": 400},
        {"id": 5, "state": "EXECUTED", "amount": 500},
    ]


@pytest.fixture
def all_executed() -> list:
    """Фикстура — все транзакции в состоянии EXECUTED."""
    return [{"id": 1, "state": "EXECUTED", "amount": 100}, {"id": 2, "state": "EXECUTED", "amount": 200}]


@pytest.mark.parametrize("state,expected_count", [("EXECUTED", 3), ("PENDING", 1), ("CANCELED", 1), ("UNKNOWN", 0)])
def test_filter_by_different_states(sample_transactions: list, state: str, expected_count: int) -> None:
    """Тест фильтрации по разным состояниям."""
    result = filter_by_state(sample_transactions, state)
    assert len(result) == expected_count
    if expected_count > 0:
        assert all(item["state"] == state for item in result)


@pytest.mark.parametrize(
    "input_list,state,expected_length",
    [
        ([], "EXECUTED", 0),
        ([], "PENDING", 0),
        ([{"id": 1, "state": "EXECUTED"}], "EXECUTED", 1),
        ([{"id": 1, "state": "PENDING"}], "EXECUTED", 0),
    ],
)
def test_edge_cases(input_list: list, state: str, expected_length: int) -> None:
    """Тест краевых случаев: пустые списки, одиночные элементы."""
    result = filter_by_state(input_list, state)
    assert len(result) == expected_length


def test_default_parameter(sample_transactions: list) -> None:
    """Тест с параметром по умолчанию (state='EXECUTED')."""
    result = filter_by_state(sample_transactions)  # без указания state
    assert len(result) == 3
    assert all(item["state"] == "EXECUTED" for item in result)


def test_all_executed_case(all_executed: list) -> None:
    """Тест когда все элементы уже в состоянии EXECUTED."""
    result = filter_by_state(all_executed, "EXECUTED")
    assert len(result) == 2
    assert result == all_executed  # должен вернуть тот же список


def test_no_matching_items(sample_transactions: list) -> None:
    """Тест когда нет элементов с заданным состоянием."""
    result = filter_by_state(sample_transactions, "COMPLETED")
    assert result == []
    assert len(result) == 0


@pytest.mark.parametrize(
    "data,state,expected",
    [
        ([{"state": "EXECUTED"}, {"state": "PENDING"}], "EXECUTED", [{"state": "EXECUTED"}]),
        ([{"state": "CANCELED"}, {"state": "CANCELED"}], "CANCELED", [{"state": "CANCELED"}, {"state": "CANCELED"}]),
    ],
)
def test_simple_cases(data: list, state: str, expected: list) -> None:
    """Простые тестовые случаи с минимальной структурой данных."""
    result = filter_by_state(data, state)
    assert result == expected


def test_invalid_lst() -> None:
    """Проверка пустой список."""
    result = filter_by_state([])
    assert result == []


def test_single_item_does_not_match() -> None:
    """Тест с одним элементом, который не соответствует состоянию."""
    data = [{"id": 1, "state": "PENDING"}]
    state = "EXECUTED"
    result = filter_by_state(data, state)
    assert result == []


def test_dict_without_state_key() -> None:
    """Тест с словарями, у которых отсутствует ключ "state"."""
    data = [{"id": 1, "status": "EXECUTED"}, {"id": 2, "state": "EXECUTED"}]  # нет ключа "state"
    with pytest.raises(KeyError):
        filter_by_state(data)


def test_single_item_does_match() -> None:
    """Тест с одним элементом, который соответствует состоянию."""
    data = [{"id": 1, "state": "PENDING"}]
    state = "PENDING"
    result = filter_by_state(data, state)
    assert result == [{"id": 1, "state": "PENDING"}]


def test_mixed_data_types_in_list() -> None:
    """Тест со списком, содержащим разные типы данных."""
    data = [{"id": 1, "state": "EXECUTED"}, "not a dict", 42, {"id": 2, "state": "EXECUTED"}]
    with pytest.raises(KeyError):
        filter_by_state(data)


def test_nested_dictionaries() -> None:
    """Тест со вложенными словарями."""
    data = [
        {"id": 1, "state": "EXECUTED", "details": {"amount": 100}},
        {"id": 2, "state": "PENDING", "details": {"amount": 200}},
    ]
    expected = [{"id": 1, "state": "EXECUTED", "details": {"amount": 100}}]
    result = filter_by_state(data)
    assert result == expected


def test_large_dataset() -> None:
    """Тест с большим набором данных."""
    large_data = [{"id": i, "state": "EXECUTED" if i % 2 == 0 else "PENDING"} for i in range(100)]
    expected_count = 50  # половина элементов с state="EXECUTED"
    result = filter_by_state(large_data)
    assert len(result) == expected_count
    assert all(item["state"] == "EXECUTED" for item in result)
