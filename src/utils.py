import json
import logging
from pathlib import Path

logger = logging.getLogger("transformation")
file_handler = logging.FileHandler(r"E:\IT\pycharm\Project2\logs\transformation.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def transformation(file: str) -> list:
    """Принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    file_path = Path(file)

    logging.info("Проверка наличия файла")
    # проверяем наличие файла
    if not file_path.exists():
        return []
    try:
        logging.info("Читаем файл и преобразовываем в python-объект")
        # читаем файл
        with open(file, "r", encoding="utf-8-sig") as f:
            data = json.load(f)
        # проверяем что данные это список
        if isinstance(data, list):
            return data
        else:
            return []
    except (json.JSONDecodeError, UnicodeDecodeError):
        logging.error("Произошла ошибка преобразования")
        # возвращаем пустой список при ошибке
        return []
    except Exception as f:
        logging.error(f"Произошла ошибка: {f}")
        # перехватываем другие ошибки
        return []
