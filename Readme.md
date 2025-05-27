
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


Для проверки кода необходимо клонировать репозиторий на ваш дистрибутив командой -

```bash
git clone https://github.com/kukidon820/read_csv_and_create_reports.git
```

Далее необходимо перейти в папку проекта -

```bash
cd read_csv_and_create_reports
```

Установить python и пакетный менеджер pip - 

```bash
sudo apt install python3 python3-pip
```

Далее нужно скачать зависимотсти - 

```bash
pip3 install -r requirements.txt 
```

Запустить тесты - 

```bash
pytest tests/test_main.py 
```

И наконец запустить скрипт - 

```bash
python main.py files/data1.csv --report payout --output new_report --format json  
```


## Отчет 

![image](https://github.com/user-attachments/assets/8c61c3d3-dd67-4047-af76-813e51e4fc80)
