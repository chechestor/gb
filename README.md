# Репозиторий

# Курс Flask, промежуточное тестирование, многопоточность, асинхронность

### Задание

Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск.
Каждое изображение должно сохраняться в отдельном файле, название которого соответствует названию изображения
в URL-адресе.
Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
— Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
— Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
— Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем времени
выполнения программы.

### Запуск

Перейти в папку скрипта:

    cd .\Kurs_Flask\Test_sync_async\

Запустить скрипт, указав в параметрах все URL картинок. Пример:

    python main.py https://hb.bizmrg.com/gb_ui_assets/ui_banners/6586/62db1647f8ec3f716c1123e091392b66.png https://gb.ru/_nuxt/img/ef949be.png https://gb.ru/_nuxt/img/8e1cdf0.png

### Пример вывода

    INFO:root:####################
    INFO:root:Sync download:
    INFO:root:  1.78 seconds for downloaded https://hb.bizmrg.com/gb_ui_assets/ui_banners/6586/62db1647f8ec3f716c1123e091392b66.png.
    INFO:root:  1.62 seconds for downloaded https://gb.ru/_nuxt/img/ef949be.png.
    INFO:root:  1.54 seconds for downloaded https://gb.ru/_nuxt/img/8e1cdf0.png.
    INFO:root:Total time:  4.93 seconds
    INFO:root:####################
    INFO:root:Multithread download:
    INFO:root:  1.68 seconds for downloaded https://gb.ru/_nuxt/img/8e1cdf0.png.
    INFO:root:  2.65 seconds for downloaded https://gb.ru/_nuxt/img/ef949be.png.
    INFO:root:  2.79 seconds for downloaded https://hb.bizmrg.com/gb_ui_assets/ui_banners/6586/62db1647f8ec3f716c1123e091392b66.png.
    INFO:root:Total time:  2.80 seconds
    INFO:root:####################
    INFO:root:Multithread download:
    INFO:root:  1.24 seconds for downloaded https://gb.ru/_nuxt/img/ef949be.png.
    INFO:root:  1.25 seconds for downloaded https://gb.ru/_nuxt/img/8e1cdf0.png.
    INFO:root:  1.40 seconds for downloaded https://hb.bizmrg.com/gb_ui_assets/ui_banners/6586/62db1647f8ec3f716c1123e091392b66.png.
    INFO:root:Total time:  1.40 seconds




# Курс Flask, промежуточное тестирование

### Задание

Создать форму для регистрации пользователей на сайте.
Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться".
При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован.

Зависимости:
- install Flask
- install Flask-WTF
- install Flask-SQLAlchemy

Установка:
- cd Flask_test
- flask install

Запуск:
- flask run --debug



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


