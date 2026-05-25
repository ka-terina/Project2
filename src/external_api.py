import os

import requests
from dotenv import load_dotenv

load_dotenv(r"E:\IT\pycharm\Project2\.env")
api_key = os.getenv("API_KEY")


def transaction_amount(tran: dict) -> float:
    """Принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях"""
    amount = float(tran["operationAmount"]["amount"])
    name = tran["operationAmount"]["currency"]["name"]
    # если рубли конвертация не нужна возвращаем как есть
    if name == "RUB":
        return amount
    # если USD делаем конвертацию
    if name == "USD":
        if api_key is not None:
            headers = {"apikey": api_key}
        else:
            raise ValueError("API key is missing")

        url = f"https://api.apilayer.com/fixer/convert?to=RUB&from=USD&amount={amount}"

        response = requests.request("GET", url, headers=headers)
    # если валюта EUR делаем конвертацию
    elif name == "EUR":
        if api_key is not None:
            headers = {"apikey": api_key}
        else:
            raise ValueError("API key is missing")
        url = f"https://api.apilayer.com/fixer/convert?to=RUB&from=EUR&amount={amount}"

        response = requests.request("GET", url, headers=headers)

    return float(response.json()["result"])

print(transaction_amount({"operationAmount":{
          "amount":"8221.37",
        "currency":{
            "name":"EUR",
            "code":"EUR"
        }
        }}))