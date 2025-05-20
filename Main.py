from LoadData import load_data
from CleanData import clean_data
from NormalizeData import normalize_data
from LoadToDuckDB import load_to_duckdb
from ShowData import show_data

def main():
    customer, sales, product = load_data()
    customer, sales, product = clean_data(customer, sales, product)
    customer, sales, product = normalize_data(customer, sales, product)
    load_to_duckdb(customer, sales, product)
    show_data()

if __name__ == "__main__":
    main()
