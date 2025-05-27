import argparse
import json
import os
import pprint


def parse_csv(filename: str):
    """
    Читает CSV-файл и преобразует его в список словарей с данными сотрудников.
    """
    with open(filename, "r") as file:
        lines = file.readlines()

    header = lines[0].strip().split(",")
    data = [line.strip().split(",") for line in lines[1:]]

    possible_rate_columns = {"hourly_rate", "rate", "salary"}
    rate_column_index = None
    for i, column_name in enumerate(header):
        if column_name.lower() in possible_rate_columns:
            rate_column_index = i
            break

    employees = []
    for row in data:
        employee = {
            "id": row[header.index("id")],
            "email": row[header.index("email")],
            "name": row[header.index("name")],
            "department": row[header.index("department")],
            "hours_worked": int(row[header.index("hours_worked")]),
            "hourly_rate": (
                float(row[rate_column_index]) if rate_column_index is not None else None
            ),
        }
        employees.append(employee)

    return employees


def generate_payout_report(employees: list):
    """
    Генерирует отчет о зарплатах сотрудников на основе их данных.
    """
    report = []
    for employee in employees:
        payout = employee["hours_worked"] * employee["hourly_rate"]
        report.append(
            {
                "id": employee["id"],
                "name": employee["name"],
                "email": employee["email"],
                "department": employee["department"],
                "payout": payout,
            }
        )
    return report


def create_json_report(report, output_file="report"):
    """
    Создает JSON-файл с отчетом.
    """
    base_name = output_file
    extension = ".json"
    index = 0
    file_name = f"{base_name}{extension}"

    while os.path.exists(file_name):
        index += 1
        file_name = f"{base_name}-{index}{extension}"

    try:
        with open(file_name, "w") as file:
            json.dump(report, file, indent=4)
        print(f"Отчет успешно сохранен в файл: {file_name}")
    except Exception as e:
        print(f"Ошибка при сохранении отчета: {e}")


def create_csv_report(report, output_file="report"):
    """
    Создает CSV-файл с отчетом.
    """
    pass


def create_xml_report(report, output_file="report"):
    """
    Создает XML-файл с отчетом.
    """
    pass


def main():
    """
    Основная функция скрипта.
    """
    parser = argparse.ArgumentParser(description="Generate reports from CSV files.")
    parser.add_argument("files", nargs="+", help="Paths to CSV files")
    parser.add_argument(
        "--report", choices=["payout"], required=True, help="Type of report to generate"
    )
    parser.add_argument(
        "--output", default="report", help="Base name for the output file"
    )
    parser.add_argument(
        "--format",
        choices=["json", "csv", "xml"],
        default="json",
        help="Format of the output report",
    )
    args = parser.parse_args()

    all_employees = []
    for file_path in args.files:
        employees = parse_csv(file_path)
        all_employees.extend(employees)

    if args.report == "payout":
        report = generate_payout_report(all_employees)
        pprint.pprint(report, indent=4, width=4)
    else:
        raise ValueError("Unsupported report type")

    if args.format == "json":
        create_json_report(report, args.output)
    elif args.format == "csv":
        create_csv_report(report, args.output)
    elif args.format == "xml":
        create_xml_report(report, args.output)
    else:
        raise ValueError("Unsupported format")


if __name__ == "__main__":
    main()

