import mysql.connector
from mysql.connector import Error

def load_data(df, host='localhost', user='your_username', password='your_password', database='your_database'):
    """Load DataFrame into MySQL database."""
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if conn.is_connected():
            cursor = conn.cursor()

            # Create table if it doesn't exist
            create_table_query = """
            CREATE TABLE IF NOT EXISTS sales_data (
                OrderId INT PRIMARY KEY,
                OrderItemId INT,
                QuantityOrdered INT,
                ItemPrice DECIMAL(10, 2),
                PromotionDiscount DECIMAL(10, 2),
                total_sales DECIMAL(10, 2),
                region VARCHAR(1),
                net_sale DECIMAL(10, 2)
            );
            """
            cursor.execute(create_table_query)

            # Insert DataFrame into MySQL table
            for i, row in df.iterrows():
                insert_query = """
                INSERT INTO sales_data (OrderId, OrderItemId, QuantityOrdered, ItemPrice, PromotionDiscount, total_sales, region, net_sale)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                OrderItemId=VALUES(OrderItemId), QuantityOrdered=VALUES(QuantityOrdered), ItemPrice=VALUES(ItemPrice),
                PromotionDiscount=VALUES(PromotionDiscount), total_sales=VALUES(total_sales), region=VALUES(region), net_sale=VALUES(net_sale);
                """
                cursor.execute(insert_query, tuple(row))

            conn.commit()
            print("Data loaded successfully.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
