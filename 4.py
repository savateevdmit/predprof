import csv

# Считывание данных из CSV файла
with (open("products.csv", encoding='utf-8') as r_file):
    file_reader = csv.reader(r_file, delimiter=";")

    categories = []  # Список категорий продуктов
    products = []  # Список продуктов
    date = []  # Список дат
    price_for_unit = []  # Список цен
    count = []  # Список количества покупок
    promokods = []  # Список промокодов

    for row in file_reader:
        if row[0] != 'Category':
            d = row[2].split('.')
            promokod = row[1][:2].upper() + d[0] + row[1][:-3:-1].upper() + d[1][::-1]  # Промокод
            promokods.append(promokod)
            categories.append(row[0])
            products.append(row[1])
            date.append(row[2])
            price_for_unit.append(row[3])
            count.append(row[4])

# Сохранение данных в файл
with open("product_promo.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
    file_writer.writerow(["Category", "Product", "Date", "Price per unit", "Count", "Promocode"])
    for i in range(len(categories)):
        file_writer.writerow([categories[i], products[i], date[i], price_for_unit[i], count[i], promokods[i]])