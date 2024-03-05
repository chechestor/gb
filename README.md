# Репозиторий

Ссылка на репозиторий с результатами промежуточной аттестации:
https://github.com/chechestor/gb

# Урок 15, задача 1

### Задание

На выбор ОДНО ИЗ ДВУХ ЗАДАНИЙ (выбрано первое):

1. Взять класс студент из дз 12-го семинара, добавить запуск из командной строки(передача в качестве аргумента название
csv-файла с предметами), логирование и написать 3-5 тестов с использованием pytest.
Написать 3-5 тестов к задаче.

Сдавать дз ссылкой на репозиторий GitHub(проверьте что он не приватный перед отправкой).

### Решение

В архиве:
- Urok15_task1/Urok15_task1.py
- Urok15_task1/subjects.csv

Исполняемый файл скрипта Urok15_task1/Urok15_task1.py. Скрипт при запуске заводит много студентов и выводит из через logging.info на экран. Ничего более полезного не делает. Для запуска скрипта требуется наличие файла csv с предметами.

### Запуск скрипта с параметрами из консоли

Запуск скрипта из консоли сначала переходим в директорию со скриптом, оттуда запускаем интерпретатор:

    $ cd Urok15_task1
    $ python Urok15_task1.py subjects.csv

### Тестирование через pytest

Проверка через pytest запускается так:

    $ cd Urok15_task1
    $ pytest Urok15_task1.py


