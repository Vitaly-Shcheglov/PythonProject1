# Проект "Виджет банковских операций клиента"

## Описание
IT-отдел крупного банка разрабатывает новую функцию для личного кабинета клиента. Это виджет, который показывает несколько последних успешных банковских операций клиента. Вам доверили реализовать этот проект, который на бэкенде будет готовить данные для отображения в новом виджете.

## Реализация функций
В проекте реализовано несколько функций для виджета:

- **В модуле masks** реализованы:
  - Функция маскировки номера банковской карты `get_mask_card_number` и функция маскировки номера банковского счета `get_mask_account`.

### Как работают функции
- **Функция `get_mask_card_number`** принимает на вход номер карты и возвращает её маску. Номер карты замаскирован и отображается в формате `XXXX XX** **** XXXX`, где `X` — это цифра номера. То есть видны первые 6 цифр и последние 4 цифры, остальные символы отображаются звездочками, а номер разбит по блокам по 4 цифры, разделённым пробелами.
  - **Пример работы функции**:
    - Входной аргумент: `7000792289606361`
    - Выход функции: `7000 79** **** 6361`

- **Функция `get_mask_account`** принимает на вход номер счета и возвращает его маску. Номер счета замаскирован и отображается в формате `**XXXX`, где `X` — это цифра номера. То есть видны только последние 4 цифры номера, а перед ними — две звездочки.
  - **Пример работы функции**:
    - Входной аргумент: `73654108430135874305`
    - Выход функции: `**4305`

- **В модуле widget** также доступна функция маски номера карты или счета `mask_account_card`, а также реализована функция форматирования даты и приведения её к виду "ДД.ММ.ГГГГ" — `get_date`.

### Как работают функции
- **Функция `mask_account_card`** принимает на вход строку формата `Visa Platinum 7000792289606361`, или `Maestro 7000792289606361`, или `Счет 73654108430135874305`. Для маскировки номера карты/счета используются ранее написанные функции из модуля `masks`.

- **Функция `get_date`** принимает на вход строку и отдает корректный результат в формате `ДД.ММ.ГГГГ`.
  - **Пример работы функции**:
    - Входной аргумент: `2024-03-11T02:26:18.671407`
    - Выход функции: `11.03.2024`

- **В модуле processing** реализованы:
  - Функция фильтрации операций по статусу “EXECUTED” и “CANCELED” — `filter_by_state`.
  - Функция сортировки банковских операций по дате — `sort_by_date`.

### Как работают функции
- **Функция `filter_by_state`** принимает на вход список словарей с данными о банковских операциях и параметр `state`, возвращает новый список, содержащий только те словари, у которых ключ `state` содержит переданное в функцию значение. Параметр `state` функции имеет значение по умолчанию `EXECUTED`.

- **Функция `sort_by_date`** принимает на вход список словарей и параметр порядка сортировки, возвращает новый список, в котором исходные словари отсортированы по дате. Параметр порядка сортировки функции имеет значение по умолчанию `True`.

- **В модуле generators** реализованы:
- Функция  фильтра транкзаций по выбранной пользователем валюте — `filter_by_currency`.
- Функция вывода описания произведенных ранее операций — `transaction_description`.
- Генератор номеров банковских карт в указанном диапазоне — `card_number_generator`.

### Как работают функции
- **Функция `filter_by_currency`** принимает на вход список словарей, представляющих транзакции и возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной (`USD`).

- **Функция `transaction_description`** принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.

- **Генератор `card_number_generator`** выдает номера банковских карт в формате `XXXX XXXX XXXX XXXX`, где X — цифра номера карты.

- **В модуле decorator** реализован:
  - Декоратор  логирования функции — `log`.

### Как работает декоратор
- **Декоратор `log`** автоматически логирetn начало и конец выполнения функции, а также ее результаты или возникшие ошибки Декоратор должен принимать необязательный аргумент filename, который определяет, куда будут записываться логи (в файл или в консоль).

- **В модуле utils** реализована:
  - Функция чтения JSON-файла — `get_operations_data`.

### Как работает функция
- **Функция `get_operations_data`** принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях. Если файл пустой, содержит не список или не найден, функция возвращает пустой список.

- **В модуле external_api** реализованы:
  - Функция, получающая данные о транзакции и возвращащающая сумму в рублях — `get_transaction_amount`.
  - Функция конвертации валюты из USD и EUR в рубли — `convert_amount`.

### Как работают функции
- **Функция `get_transaction_amount`** принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях.
- **Функция `convert_amount`** — если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют и конвертации суммы операции в рубли.

- **В модуле data_loader** реализованы:
- Функция  для считывания финансовых операций из CSV — `read_transactions_from_csv`.
- Функция для считывания финансовых операций из Excel — `read_transactions_from_excel`.

### Как работают функции
- **Функция `read_transactions_from_csv`** принимает путь к файлу CSV в качестве аргумента и выдает список словарей с транзакциями.
- **Функция `read_transactions_from_excel`** принимает путь к файлу Excel в качестве аргумента и выдает список словарей с транзакциями.


## Установка
1. Клонирование репозитория
```git clone https://github.com/Vitaly-Shcheglov/PythonProject1.git```

2. Запуск скрипта для демонстрации возможностей

## Использование

## Тестирование

В ходе тестирования кода был выполнен ряд проверок и отладки отдельных модулей:

### Модуль masks

#### Функция get_mask_card_number:
- **Тестирование правильности маскирования номера карты**: Проверка корректности формата возвращаемого значения для различных номеров карт.
- **Тестирование обработки некорректных номеров карт**: Проверка, что функция возвращает сообщение об ошибке для номеров карт, которые не соответствуют ожидаемому формату (например, слишком короткие номера).
- **Тестирование работы функции на различных входных форматах номеров карт**: Проверка работы функции с номерами карт разных форматов и длин.

#### Функция get_mask_account:
- **Тестирование правильности маскирования номера счета**: Проверка корректности выходного значения для различных номеров счетов.
- **Тестирование обработки некорректных номеров счетов**: Убедиться, что функция возвращает сообщение об ошибке для номеров счетов, которые не соответствуют минимальной длине или формату.
- **Тестирование работы функции с различными форматами и длинами номеров счетов**: Проверка работы функции с разными входными данными, включая граничные случаи (например, минимально допустимая длина номера).

### Модуль widget

#### Функция mask_account_card:
- **Тестирование функции на корректность распознавания и применения нужного типа маскировки в зависимости от типа входных данных (карта или счет)**: Проверка, что функция правильно определяет, является ли ввод номером карты или счета, и применяет соответствующую маскировку.
- **Тестирование с разными типами карт и счетов для проверки универсальности функции**: Проверка функции на различных типах входных данных, чтобы убедиться в корректной маскировке.
- **Тестирование функции на обработку некорректных входных данных и проверка ее устойчивости к ошибкам**: Убедиться, что функция возвращает соответствующее сообщение об ошибке для некорректных входных данных.

#### Функция get_date:
- **Тестирование правильности преобразования даты**: Проверка, что функция корректно преобразует дату из формата YYYY-MM-DDTHH:MM:SS в формат ДД.ММ.ГГГГ.
- **Тестирование работы функции на различных входных форматах даты**: Проверка функции с различными форматами ввода, включая корректные и некорректные форматы.

### Модуль processing

#### Функция filter_by_state:
- **Тестирование функции фильтрации по статусу**: Проверка корректности работы функции, которая фильтрует банковские операции по статусу, отображая только операции с заданным статусом.
- **Параметризация тестов для проверки различных возможных значений статуса state**: Убедиться, что функция корректно обрабатывает разные статусы и возвращает правильные результаты.

#### Функция sort_by_date:
- **Тестирование функции сортировки по дате**: Проверка, что функция корректно сортирует операции по дате.
- **Параметризованное тестирование функции сортировки по дате**: Проверка функции с различными входными данными, чтобы убедиться, что она правильно сортирует список операций.

### Модуль generators

#### Функция filter_by_currency:
- **Тестирование функции** на корректность фильтрации транзакций по заданной валюте.
- **Тестирование генератора** при обработке пустого списка транзакций.
- **Тестирование функции на обработку случаев, когда транзакции в заданной валюте отсутствуют.

#### Функция transaction_description:
- **Тестирование функции** на возврат корректных описаний транзакций.
- **Тестирование работы функции** с различным количеством входных транзакций, включая пустой список.

#### Генератор card_number_generator:
- **Тестирование выдачи генератором** правильных номеров карт в заданном диапазоне.
- **Тестирование корректности** форматирования номеров карт.

### Модуль decorators

#### Декоратор log:
- **Тестирование функции на возврат правильного результата**.
- **Проверяется, что вывод логов содержит правильные сообщения** о начале и окончании выполнения.
- **Проверяется, что происходит исключение `ZeroDivisionError`**, если делитель равен нулю, и что лог содержит соответствующее сообщение об ошибке.
- **Проверяется, что функция корректно записывает логи** в файл при выполнении.
- **Все тесты используют фикстуру "capsys"** для перехвата вывода в консоль, что позволяет проверять, что логирование работает корректно.

### Модуль utils

#### Функция get_operations_data:
- **Тестирование функции** на успешность получения данных операций из JSON-файла.
- **Тестирование функции** на получение пустого списка операций из пустого JSON-файла.
- **Тестирование функции** на на обработку некорректного JSON-файла.
- **Тестирование функции** на случай, когда файл не найден.

### Модуль external_api

#### Функция get_transaction_amount:
- **Тестирование функции** на получение суммы операции в рублях.

#### Функция convert_amount:
- **Тестирование функции** на получение суммы операции из USD в RUB.
- **Тестирование функции** на некорректные данные.
- **Тестирование функции** на конвертацию из USD в RUB.
- **Тестирование функции** на конвертацию с ошибкой API.

### Модуль data_loader

#### Функция read_transactions_from_csv:
- **Тестирование функции** на считывание транзакций из CSV.
- **Тестирование функции** на случай, когда файл не найден.
- **Тестирование функции** на некорректный формат CSV.
- **Тестирование функции** на CSV-файл с недостающими столбцами.

#### Функция read_transactions_from_excel:
- **Тестирование функции** на считывание транзакций из Excel.
- **Тестирование функции** на случай, когда файл не найден.
- **Тестирование функции** на некорректный формат Excel.
- **Тестирование функции** на Excel-файл с недостающими столбцами.
