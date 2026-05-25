import json
from pathlib import Path


def transformation(file: str) -> list:
    """Принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    file_path= Path(file)

    # проверяем наличие файла
    if not file_path.exists():
        return []
    try:
        # читаем файл
        with open(file, "r", encoding="utf-8-sig") as f:
            data = json.load(f)
        # проверяем что данные это список
        if isinstance(data, list):
            return data
        else:
            return []
    except (json.JSONDecodeError, UnicodeDecodeError):
        # возвращаем пустой список при ошибке
        return []
    except Exception:
        # перехватываем другие ошибки
        return []

print(transformation(r"E:\IT\pycharm\Project2\data\operations.json"))