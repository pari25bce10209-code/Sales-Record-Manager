# main.py
from sales_manager import setupFile, addSale, viewSales, sortByDate, showSummary,updateSale,deleteSale
from pandas_helper import showChart          #importing different functions from the modules we created before

def menu(): #showing menu to the user
    print("\n--- Sales Manager ---")
    print("1. Add Sale")
    print("2. View Sales")
    print("3. Sort by Date")
    print("4. Update Sales")
    print("5. Delete Sales")
    print("6. Summary Report")
    print("7. Show Chart")
    print("8. Exit")

def main():
    setupFile()
    while True:
        menu()
        choice = input("Enter choice: ") #entering the choice of the user
        if choice == "1": #matching the choice entered by user to know which function is to be used
            product = input("Product: ")
            qty = int(input("Quantity: "))
            price = float(input("Price: "))
            date = input("Date (YYYY-MM-DD): ")
            addSale(product, qty, price, date) #calling the function
        elif choice == "2":
            viewSales()
        elif choice == "3":
            sortByDate()
        elif choice =="4":
            product = input("Product: ")
            qty = int(input("Quantity: "))
            price = float(input("Price: "))
            date = input("Date (YYYY-MM-DD): ")

            updateSale(date,product,qty,price)
        elif choice=="5":
          product = input("Product: ")
          date = input("Date (YYYY-MM-DD): ")
          deleteSale(date,product)
        elif choice == "6":
            showSummary()
        elif choice == "7":
            showChart()
        elif choice=="8": #to enter correct choice
            print ("TRY AGAIN")
            break
        

if __name__ == "__main__":

    main()
