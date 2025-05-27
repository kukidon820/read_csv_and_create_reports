
Скрипт на Python для генерации отчетов о выплатах сотрудникам на основе CSV-файлов с данными.

Скрипт читает один или несколько CSV-файлов с информацией о сотрудниках, рассчитывает выплаты на основе отработанных часов и ставки, и сохраняет отчет в выбранном формате: JSON (реализован), CSV или XML (заготовки присутствуют).

##  Структура CSV-файла

CSV-файл должен содержать следующие столбцы:

- `id` — идентификатор сотрудника
- `email` — email сотрудника
- `name` — имя сотрудника
- `department` — отдел
- `hours_worked` — отработанные часы
- Один из следующих столбцов, содержащий ставку:
  - `hourly_rate`
  - `rate`
  - `salary`

## Использование

```bash
python script.py <пути_к_csv_файлам> --report payout [--output report] [--format json|csv|xml]
```

### Аргументы

- `<пути_к_csv_файлам>` — один или несколько путей к CSV-файлам
- `--report` — тип отчета (обязательно). Поддерживается только `payout`
- `--output` — базовое имя выходного файла (по умолчанию: `report`)
- `--format` — формат выходного файла: `json` (по умолчанию), `csv`, `xml`

### Примеры запуска

```bash
python script.py employees.csv --report payout --format json
python script.py employees.csv --report payout --output employees_report
python script.py file1.csv file2.csv --report payout --format json
```

##  Форматы отчета

- ✅ `JSON`: реализован, сохраняет файл с именем `report.json`, `report-1.json`, и т.д.
- ⏳ `CSV`: функция `create_csv_report()` не реализована
- ⏳ `XML`: функция `create_xml_report()` не реализована
