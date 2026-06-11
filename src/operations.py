import pandas as pd


def read_csv_operations(file_path: str) -> list:
    """Считывание финансовых операций из CSV-файла"""
    df = pd.read_csv(file_path)

    return df.to_dict('records')


def read_xlsx_operations(file_path: str) -> list:
    """Считывание финансовых операций из XLSX-файла"""
    df = pd.read_excel(file_path)

    return df.to_dict('records')
