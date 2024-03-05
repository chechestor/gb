'''
На выбор ОДНО ИЗ ДВУХ ЗАДАНИЙ (выбрано первое):
1. Взять класс студент из дз 12-го семинара, добавить запуск из командной строки(передача в качестве аргумента название
csv-файла с предметами), логирование и написать 3-5 тестов с использованием pytest.
Написать 3-5 тестов к задаче.

Сдавать дз ссылкой на репозиторий GitHub(проверьте что он не приватный перед отправкой).
'''
import logging
import os.path
import csv
from statistics import mean
import pytest
import argparse


logging.basicConfig(level=logging.INFO)
class NameDescriptor:
    def __init__(self, name='Default'):
        self.param_value = name

    def __set_name__(self, owner, param_name):
        self.param_name = '_' + param_name
    def __get__(self, instance, owner):
        return getattr(instance, self.param_value)
    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_value, value)
    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')
    def validate(self, value:str):
        names = value.split()
        for n in names:
            if not n.istitle() or not n.isalpha():
                raise ValueError(f'ФИО должно состоять только из букв и начинаться с заглавной буквы')
                return False
        return True

class Student:
    name = NameDescriptor()
    _allowed_subjects = []

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = {}
        self.load_subjects(subjects_file)

    def load_subjects(self, subjects_file):
        '''
        Загружает предметы из файла CSV. Использует модуль csv для чтения данных из файла и добавляет предметы в атрибут subjects.
        '''
        with open(subjects_file, 'rt', newline='', encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            for line in csv_reader:
                for subj in line:
                    self._allowed_subjects.append(subj)

    def _check_subject(self, subject):
        if not subject in self._allowed_subjects:
            raise ValueError(f'Предмет {subject} не найден')
            return False
        return True

    def _create_subject_if_need(self, subject):
        if subject not in self.subjects:
            self.subjects[subject] = {'grade': [], 'test_score': []}

    def add_grade(self, subject, grade):
        '''
        Добавляет оценку по заданному предмету. Убеждается, что оценка является целым числом от 2 до 5.
        '''
        if not self._check_subject(subject):
            return False
        self._create_subject_if_need(subject)
        if not isinstance(grade, int) or not (2 <= grade <= 5):
            raise ValueError(f'Оценка должна быть целым числом от 2 до 5')
            return False
        self.subjects[subject]['grade'].append(grade)
        return True


    def add_test_score(self, subject, test_score) -> float:
        '''
        Добавляет результат теста по заданному предмету. Убеждается, что результат теста является целым числом от 0 до 100.
        '''
        if not self._check_subject(subject):
            return False
        self._create_subject_if_need(subject)
        if not isinstance(test_score, int) or not ( 0 <= test_score <= 100):
            raise ValueError(f'Результат теста должен быть целым числом от 0 до 100')
            return False
        self.subjects[subject]['test_score'].append(test_score)
        return True

    def get_average_test_score(self, subject) -> float:
        '''
        Возвращает средний балл по тестам для заданного предмета.
        '''
        if not self._check_subject(subject):
            return None
        return float(mean(self.subjects[subject]['test_score']))

    def get_average_grade(self) -> float:
        '''
        Возвращает средний балл по всем предметам.
        '''
        ave = []
        for s,v in self.subjects.items():
            ave.extend(v['grade'])
        if not ave:
            return 0
        return float(mean(ave))

    def __str__(self):
        return (f'''Студент: {self.name}\n'''
                f'''Предметы: {", ".join(self.subjects.keys())}''')



class TestClass:
    csv_file = './subjects.csv'

    @pytest.fixture
    def get_csv_file(self, tmp_path):
        f_name = tmp_path / 'test_file.txt'
        with open(f_name, 'wt', encoding='utf-8') as f:
            csv_writter = csv.writer(f, dialect='excel')
            csv_writter.writerow(['Математика','Физика','История','Литература'])
        yield f_name
        if os.path.exists(f_name):
            os.remove(f_name)


    def test_student_create(self, get_csv_file):
        student1 = Student("Иван Иванов", get_csv_file)
        assert student1.name == 'Иван Иванов', "Не удалось установить имя студента"
        assert student1.subjects == {}, "Некорректный список предметов при создании класса"


    def test_student_create(self, get_csv_file):
        student1 = Student("Иван Иванов", get_csv_file)
        assert student1.name == 'Иван Иванов', "Не удалось установить имя студента"
        assert student1.subjects == {}, "Некорректный список предметов при создании класса"

    def test_student_create_incorrect_name(self, get_csv_file):
        with pytest.raises(ValueError):
            student1 = Student("ASCI SOTONA 666", get_csv_file)

    def test_add_subject_correctly(self, get_csv_file):
        student1 = Student("Петр Петров", get_csv_file)
        student1.add_grade("Математика", 4)
        student1.add_test_score("Математика", 85)
        student1.add_grade("Математика", 3)
        student1.add_test_score("Математика", 77)
        student1.add_grade("История", 3)
        student1.add_test_score("Физика", 55)
        result_subjects_string = ("{'Математика': {'grade': [4, 3], 'test_score': [85, 77]}, "
                                  "'История': {'grade': [3], 'test_score': []}, "
                                  "'Физика': {'grade': [], 'test_score': [55]}}")
        assert str(student1.subjects) == result_subjects_string, "Ошибка добавления оценок и тестов."
        #assert student1.subjects == {}, "екорректный список предметов при создании класса"

    def test_add_subject_incorrect(self, get_csv_file):
        with pytest.raises(ValueError):
            student1 = Student("Сидр Сидоров", get_csv_file)
            student1.add_grade("Ботанохимия", 4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Тестирование работы со студентами.")
    parser.add_argument("scv_file", type=str, help="Тестовый CSV-файла для проверки классов судентов.")
    args = parser.parse_args()

    logging.info(f'Файл \"{args.scv_file}\" используется в качестве базы с разрешенными дисциплинами студентов')

    # Создаем зоопарк студентов по именам и фамилиям, производным от имен
    first_names = ['Иван', 'Петр', 'Сидор', 'Макар']
    last_names = list(map(lambda x: x+'ов', first_names))
    full_names = [' '.join((fname, lname)) for fname in first_names for lname in last_names ]
    students = [Student(funame, args.scv_file) for funame in full_names]

    for student in students:
        logging.info(student)
