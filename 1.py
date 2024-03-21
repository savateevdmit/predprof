import csv

# Считывание данных из CSV файла
with (open("products.csv", encoding='utf-8') as r_file):
    file_reader = csv.reader(r_file, delimiter=";")
    price = 0  # Сумма цен закусок
    total = []  # Список сумм всех продуктов

    for row in file_reader:
        if row[0] != 'Category':
            x = float(row[3]) * float(row[4])
            if row[0] == 'Закуски':
                price += x
            total.append(x)

print('Итоговая сумма по категории "Закуски" =', price)

# Сохранение данных в новый файл
with open("products_new.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
    file_writer.writerow(["total"])
    for row in total:
        file_writer.writerow([row])