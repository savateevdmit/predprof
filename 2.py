import csv

# Считывание данных из CSV файла
with (open("products.csv", encoding='utf-8') as r_file):
    file_reader = csv.reader(r_file, delimiter=";")
    price = 0  # Сумма цен закусок
    category = []  # Список категорий
    products = []  # Список продуктов самой дорогой категории

    for row in file_reader:
        if row[0] != 'Category':
            category.append(row[0])

    category.sort()  # Сортировка списка категорий
    category = category[0]

# Считывание данных из CSV файла
with (open("products.csv", encoding='utf-8') as r_file):
    file_reader = csv.reader(r_file, delimiter=";")
    for row in file_reader:
        if row[0] != 'Category':
            if row[0] == category:  # Проверка на совпадение категории
                products.append([row[3], row[1]])

products = sorted(products, key=lambda x: x[0])  # Сортировка списка продуктов
print(f"В категории: {category} самый дорогой товар: {products[-1][1]} его цена за единицу товара составляет {products[-1][0]}")
