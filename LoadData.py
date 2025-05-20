import pandas as pd

def load_data():
    customer = pd.read_csv("Source/customer_details.csv")
    sales = pd.read_csv("Source/E-commerece sales data 2024.csv")
    product = pd.read_csv("Source/product_details.csv")

    print("Loaded data.")

    print("\nCustomer preview:")
    print(customer.head())

    print("\nSales preview:")
    print(sales.head())

    print("\nProduct preview:")
    print(product.head())
