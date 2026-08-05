from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency
from src.operations import read_csv_operations, read_xlsx_operations
from src.utils import transformation
from src.widget import get_date
from src.filter_transactions import process_bank_search


def load_transactions_from_json(file_path: str) -> list:
    """Загрузка транзакции из json-файла"""
    print(f"Загрузка транзакций из файла: {file_path}")
    file_transactions = transformation(file_path)
    return file_transactions


def load_transactions_from_csv(file_path: str) -> list:
    """Загрузка транзакций из csv-файла"""
    print(f"Загрузка транзакций из файла: {file_path}")
    file_transactions = read_csv_operations(file_path)
    return file_transactions


def load_transactions_from_xlsx(file_path: str) -> list:
    """Загрузка транзакций из xlsx-файла"""
    print(f"Загрузка транзакций из файла: {file_path}")
    file_transactions = read_xlsx_operations(file_path)
    return file_transactions


def main() -> None:
    """Основная логика программы"""
    # выбираем формат файла
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input().strip()

    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        file_path = input("Введите путь к JSON-файлу: ").strip()
        transactions = load_transactions_from_json(file_path)

    elif choice == "2":
        print("Для обработки выбран CSV-файл")
        file_path = input("Введите путь к CSV-файлу: ").strip()
        transactions = load_transactions_from_csv(file_path)

    elif choice == "3":
        print("Для обработки выбран XLSX-файл")
        file_path = input("Введите путь к XLSX-файлу: ").strip()
        transactions = load_transactions_from_xlsx(file_path)

    else:
        print("Неверный выбор. Пожалуйста, выберите пункт от 1 до 3.")

    # выбираем по какому статусу отфильтровать список и фильтруем
    print("Введите статус, по которому необходимо выполнить фильтрацию.")
    print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")

    status = input().strip().upper()

    valid_statuses = {"EXECUTED", "CANCELED", "PENDING"}
    while True:
        if status in valid_statuses:
            filter_file = filter_by_state(transactions, status)
            print(f"Операции отфильтрованы по статусу '{status}'")
            break
        else:
            print(f"Статус операции '{status}' недоступен.")
            print("Введите статус, по которому необходимо выполнить фильтрацию.")
            print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
            status = input().strip().upper()

    while True:  # выбираем сортировать по дате или нет
        print("Отсортировать операции по дате? Да/Нет")
        data = input().strip().lower()

        if data == "да":
            print("Отсортировать по:")
            print("1. возрастанию")
            print("2. убыванию")

            while True:  # цикл для выбора направления сортировки
                reverse = input().strip()
                if reverse == "1":
                    data_reverse_file = sort_by_date(filter_file, reverse=False)
                    print("Операции отсортированы по дате в порядке по возрастанию")
                    break  # выходим из внутреннего цикла
                elif reverse == "2":
                    data_reverse_file = sort_by_date(filter_file, reverse=True)
                    print("Операции отсортированы по дате в порядке по убыванию")
                    break  # выходим из внутреннего цикла
                else:
                    print("Некорректный ввод. Введите 1 или 2.")
            break  # выходим из внешнего цикла, т.к. "да" обработано

        elif data == "нет":
            data_reverse_file = filter_file
            break  # выходим из внешнего цикла, т.к. "нет" обработано
        else:
            print("Некорректный ввод. Пожалуйста, введите 'Да' или 'Нет'.")
            # цикл продолжается, снова задается вопрос

    while True:  # определяем нужно ли фильтровать по валюте
        print("Выводить только рублевые транзакции? Да/Нет")
        currency_rub = input().strip().lower()

        if currency_rub == "да":
            currency_file = list(filter_by_currency(data_reverse_file, currency="RUB"))
            print("Выведены только рублевые транзакции")
            break  # выходим из цикла, т.к. "да" обработано
        elif currency_rub == "нет":
            currency_file = data_reverse_file
            break  # выходим из цикла, т.к. "нет" обработано
        else:
            print("Некорректный ввод. Пожалуйста, введите 'Да' или 'Нет'.")
            # цикл продолжается, снова задается вопрос

    while True:  # нужно ли фильтровать по слову в описании
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        answer = input().strip().lower()

        if answer == "да":
            word = input("Введите слово для фильтрации: ").strip()
            result_file = process_bank_search(currency_file, word)
            break  # выходим из цикла, т.к. "да" обработано
        elif answer == "нет":
            result_file = currency_file
            break  # выходим из цикла, т.к. "нет" обработано
        else:
            print("Некорректный ввод. Пожалуйста, введите 'Да' или 'Нет'.")
            # цикл продолжается, снова задается вопрос

    print("Распечатываю итоговый список транзакций...")

    # выводим количество операций в выборке
    print(f"Всего банковских операций в выборке: {len(result_file)}")
    # Если выборка оказалась пустой, программа выводит сообщение:
    if len(result_file) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

    # выводим список операций в нужном виде
    for element in result_file:
        data = get_date(element["date"])

        print(data, element["description"])  # дата и описание
        print(f"{element['from']} -> {element['to']}")  # если перевод то откуда и куда
        print(f"Сумма: {element['amount']} {element['currency_code']}")  # сумма и валюта
        print()
