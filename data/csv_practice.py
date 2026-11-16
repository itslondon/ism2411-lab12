import csv
# Exercise 1
with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# Exercise 2
with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

# Exercise 3

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)

#Exercise 4
total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        revenue = price * quantity
        total_revenue += revenue

        print(f"{product}: {quantity} units × ${price:.2f} = ${revenue:.2f}")

print(f"Total revenue: ${total_revenue:.2f}")

#Exercise 5
original_count = 0
cleaned_count = 0

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)

    with open("cleaned.csv", "w", newline="") as output_file:
        writer = csv.writer(output_file)

        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            original_count += 1

            product = row[0]
            price = float(row[1])
            quantity = int(row[2])

            total = price * quantity

            if total > 100:
                writer.writerow([product, price, quantity, total])
                cleaned_count += 1

print("Original rows:", original_count)
print("Rows written:", cleaned_count)

# Exercise 6
total_revenue_dict = 0

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        revenue = price * quantity
        total_revenue_dict += revenue

        print(f"{product}: {quantity} units × ${price:.2f} = ${revenue:.2f}")

print(f"Total revenue using DictReader: ${total_revenue_dict:.2f}")
# csv.reader uses column positions, while DictReader uses column names.
# I prefer DictReader when I want code that is easier to read.

# Exercise 7

summary = {}

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        revenue = price * quantity

        if product in summary:
            summary[product] += revenue
        else:
            summary[product] = revenue

for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")


# Exercise 8

import csv
from datetime import datetime

total_revenue = 0
with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)

    for row in reader:
        price = float(row[1])
        quantity = int(row[2])

        revenue = price * quantity
        total_revenue += revenue

        current_time = datetime.now()

        with open("run_log.txt", "a") as log_file:
            log_file.write(f"{current_time} - Total Revenue ${total_revenue:.2f}\n")

        print("Run log updated!")


