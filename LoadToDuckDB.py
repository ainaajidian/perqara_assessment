import duckdb

def load_to_duckdb(customer_df, sales_df, product_df):
    con = duckdb.connect("perqara.duckdb")

    con.execute("DROP TABLE IF EXISTS customers;")
    con.execute("DROP TABLE IF EXISTS products;")
    con.execute("DROP TABLE IF EXISTS sales;")

    con.register("customer_df_view", customer_df)
    con.execute("CREATE TABLE customers AS SELECT * FROM customer_df_view")

    con.register("product_df_view", product_df)
    con.execute("CREATE TABLE products AS SELECT * FROM product_df_view")

    con.register("sales_df_view", sales_df)
    con.execute("CREATE TABLE sales AS SELECT * FROM sales_df_view")

    print("Data successfully loaded into DuckDB.")
    return con
