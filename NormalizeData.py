import pandas as pd

def normalize_data(customer, sales, product):
    sales = sales.rename(columns={
        'user id': 'Customer ID',
        'product id': 'Product ID',
        'Time stamp': 'Order Date'
    })

    sales.dropna(subset=['Customer ID', 'Product ID'], inplace=True)
    sales['Customer ID'] = pd.to_numeric(sales['Customer ID'], errors='coerce')
    sales['Order Date'] = pd.to_datetime(sales['Order Date'], errors='coerce')
    sales.loc[:, 'Order Date'] = sales['Order Date'].fillna(pd.Timestamp("2000-01-01"))
    sales['Product ID'] = sales['Product ID'].astype(str)
    customer['Age'] = pd.to_numeric(customer['Age'], errors='coerce')
    customer['Purchase Amount (USD)'] = pd.to_numeric(customer['Purchase Amount (USD)'], errors='coerce')
    customer['Previous Purchases'] = pd.to_numeric(customer['Previous Purchases'], errors='coerce')
    import pandas as pd

def normalize_data(customer, sales, product):
    sales = sales.rename(columns={
        'user id': 'Customer ID',
        'product id': 'Product ID',
        'Time stamp': 'Order Date'
    })

    sales.dropna(subset=['Customer ID', 'Product ID'], inplace=True)
    sales['Customer ID'] = pd.to_numeric(sales['Customer ID'], errors='coerce')
    sales['Order Date'] = pd.to_datetime(sales['Order Date'], errors='coerce')
    sales.loc[:, 'Order Date'] = sales['Order Date'].fillna(pd.Timestamp("2000-01-01"))
    sales['Product ID'] = sales['Product ID'].astype(str)
    customer['Age'] = pd.to_numeric(customer['Age'], errors='coerce')
    customer['Purchase Amount (USD)'] = pd.to_numeric(customer['Purchase Amount (USD)'], errors='coerce')
    customer['Previous Purchases'] = pd.to_numeric(customer['Previous Purchases'], errors='coerce')
    
    print("\nData normalized.\n")

    return customer, sales, product