from LoadData import load_data
from CleanData import clean_data
from NormalizeData import normalize_data

def main():
    customer, sales, product = load_data()
    customer, sales, product = clean_data(customer, sales, product)
    customer, sales, product = normalize_data(customer, sales, product)

if __name__ == "__main__":
    main()
