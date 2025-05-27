import os
import json
import pytest
from main import parse_csv, generate_payout_report, create_json_report


@pytest.fixture
def test_create_test_csv(tmp_path):
    """
    Фикстура для создания файла csv
    """
    csv_data = """id,email,name,department,hours_worked,hourly_rate
1,alice@example.com,Alice Johnson,Marketing,160,50
2,bob@example.com,Bob Smith,Design,150,40"""

    file_path = tmp_path / "test.csv"
    file_path.write_text(csv_data)
    return file_path


def test_parse_csv(test_create_test_csv):
    """
    Тестирование чтения csv файла
    """
    employees = parse_csv(test_create_test_csv)
    expected = [
        {
            "id": "1",
            "email": "alice@example.com",
            "name": "Alice Johnson",
            "department": "Marketing",
            "hours_worked": 160,
            "hourly_rate": 50.0,
        },
        {
            "id": "2",
            "email": "bob@example.com",
            "name": "Bob Smith",
            "department": "Design",
            "hours_worked": 150,
            "hourly_rate": 40.0,
        },
    ]

    assert employees == expected


@pytest.fixture
def test_generate_payout_report():
    """
    Тестируем функцию генерации отчета(generate_payout_report)
    """

    employees = [
        {
            "id": "1",
            "email": "alice@example.com",
            "name": "Alice Johnson",
            "department": "Marketing",
            "hours_worked": 160,
            "hourly_rate": 50.0,
        },
        {
            "id": "2",
            "email": "bob@example.com",
            "name": "Bob Smith",
            "department": "Design",
            "hours_worked": 150,
            "hourly_rate": 40.0,
        },
    ]

    report = generate_payout_report(employees)
    expected = [
        {
            "id": "1",
            "name": "Alice Johnson",
            "email": "alice@example.com",
            "department": "Marketing",
            "payout": 8000.0,
        },
        {
            "id": "2",
            "name": "Bob Smith",
            "email": "bob@example.com",
            "department": "Design",
            "payout": 6000.0,
        },
    ]

    assert report == expected
    return report


def test_create_json_report(tmp_path, test_generate_payout_report):
    """
    Тестирование фенкции создания отчета в файл .json
    """
    report = test_generate_payout_report

    output_path = tmp_path / "test_report"
    create_json_report(report, str(output_path))

    file_name = f"{output_path}.json"
    assert os.path.exists(file_name)

    with open(file_name, "r") as file:
        saved_report = json.load(file)
    assert saved_report == report

