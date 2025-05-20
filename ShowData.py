import duckdb

def show_data():
    con = duckdb.connect("perqara.duckdb")
    print("\nTop 5 from customers:")
    print(con.execute("SELECT * FROM customers LIMIT 5").fetchdf())

    print("\nTop 5 from products:")
    print(con.execute("SELECT * FROM products LIMIT 5").fetchdf())

    print("\nTop 5 from sales:")
    print(con.execute("SELECT * FROM sales").fetchdf())
    con.close()
