"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta

def print_days():
    date_now=datetime.now()
    yesterday= date_now-timedelta(days=1)
    after30_days=date_now-timedelta(days=30)
    print('Сегодняшняя дата: {}\nВчерашняя дата: {} \nДата 30 дней назад: {}'.format(date_now.strftime('%d.%m.%Y'), yesterday.strftime('%d.%m.%Y'),after30_days.strftime('%d.%m.%Y') ))


def str_2_datetime(date_string):
    date_dt = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
    return date_dt

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
