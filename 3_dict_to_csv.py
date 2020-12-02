"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv


diction= [
        {'name': 'Jack', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
        {'name': 'Эдуард12', 'age': 28, 'job': 'Big boss'}
    ]

def main():
    with open('export.csv', 'w', newline='') as f:
        fields = ['first_name', 'last_name', 'email', 'gender', 'balance']
        writer = csv.DictWriter(f, diction[0].keys(), delimiter=';')
        writer.writeheader()
        for user in diction:
            writer.writerow(user)
      
        

if __name__ == "__main__":
    main()
