# sales_manager.py
import csv
import os

FILE = "sales.csv"

def setupFile():
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Product", "Quantity", "Price", "Date", "Total"])

def addSale(product, qty, price, date):
    total = qty * price
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([product, qty, price, date, total])
    print("Sale added!")

def viewSales():
    with open(FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
def updateSale(date, product, newQty, newPrice):
    updated = False
    with open(FILE, "r") as f:
        rows = list(csv.reader(f))
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        for row in rows:
            if row[0] == product and row[3] == date:
                total = newQty * newPrice
                writer.writerow([product, newQty, newPrice, date, total])
                updated = True
            else:
                writer.writerow(row)
    if updated:
        print("Sale updated!")
    else:
        print("Sale not found.")

def deleteSale(date, product):
    deleted = False
    with open(FILE, "r") as f:
        rows = list(csv.reader(f))
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        for row in rows:
            if row[0] == product and row[3] == date:
                deleted = True
                continue
            writer.writerow(row)
    if deleted:
        print("Sale deleted!")
    else:
        print("Sale not found.")



def sortByDate():
    with open(FILE, "r") as f:
        reader = list(csv.reader(f))
        header = reader[0]
        data = reader[1:]
        data.sort(key=lambda x: x[3])
        print(header)
        for row in data:
            print(row)

def showSummary():
    total = 0
    count = {}
    with open(FILE, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row:
                product = row[0]
                qty = int(row[1])
                sale = float(row[4])
                total += sale
                count[product] = count.get(product, 0) + qty
    print("Total Sales:", total)
    if count:
        best = max(count, key=count.get)
        print("Best Seller:", best)