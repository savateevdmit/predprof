import csv

category = input()  # категория
while category != 'молоко':
    products = []  # список продуктов
    # считываем данные из файла
    with (open("products.csv", encoding='utf-8') as r_file):
        file_reader = csv.reader(r_file, delimiter=";")

        for row in file_reader:
            if row[0] != 'Category':
                if row[0] == category:  # Проверка на совпадение категории
                    products.append([row[4], row[1]])

    products = sorted(products, key=lambda x: x[0])  # Сортировка списка продуктов
    if len(products) == 0:
        print("Такой категории не существует в нашей БД")
    else:
        print(f"В категории: {category} товар: {products[0][1]} был куплен {products[-1][0]} раз")

    category = input()