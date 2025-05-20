def clean_data(customer, sales, product):
    print(f"\nRows before cleaning:")
    print(f"Customers: {len(customer)} | Sales: {len(sales)} | Products: {len(product)}")

    customer = customer.loc[:, ~customer.columns.str.contains('^Unnamed')].copy()
    sales = sales.loc[:, ~sales.columns.str.contains('^Unnamed')].copy()
    product = product.loc[:, ~product.columns.str.contains('^Unnamed')].copy()

    customer.dropna(how='all', inplace=True)
    sales.dropna(how='all', inplace=True)
    product.dropna(how='all', inplace=True)

    customer.drop_duplicates(inplace=True)
    sales.drop_duplicates(inplace=True)
    product.drop_duplicates(inplace=True)

    print(f"\nRows after dropping duplicates/empty:")
    print(f"Customers: {len(customer)} | Sales: {len(sales)} | Products: {len(product)}")
    return customer, sales, product
