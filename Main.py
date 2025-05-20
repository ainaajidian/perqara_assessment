from LoadData import load_data
from CleanData import clean_data

def main():
    customer, sales, product = load_data()
    customer, sales, product = clean_data(customer, sales, product)

if __name__ == "__main__":
    main()
