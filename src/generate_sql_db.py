'''
As a developer 
I want to automate the creation of a database schema
So that I don't have to set it up manually.
'''
from connect_to_db import *

def create_db_tables(connection, cursor) -> True or False:
    try: 
        # print('...creating drinks')
        # cursor.execute("""
        # CREATE TABLE IF NOT EXISTS drinks (
        #     drink_id SERIAL PRIMARY KEY,
        #     drink_name VARCHAR(250) NOT NULL,
        #     drink_price DECIMAL(6,2) NOT NULL
        # );
        # """)


        # print('...creating drink_flavors')
        # cursor.execute("""
        # CREATE TABLE IF NOT EXISTS drink_flavors (
        #     drink_flavor_id SERIAL PRIMARY KEY,
        #     drink_flavor_name VARCHAR(250) NOT NULL
        # );
        # """)

        print('...creating location')
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS location (
            location_id SERIAL PRIMARY KEY,
            location_name VARCHAR(250) NOT NULL UNIQUE
        );
        """)
        
        print('...creating customers')
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id SERIAL PRIMARY KEY,
            customer_name VARCHAR(250) NOT NULL
        );
        """)
        
        print('...creating customer_transactions')
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS customer_transactions (
            transaction_id SERIAL PRIMARY KEY,
            order_date TIMESTAMP NOT NULL,
            customer_id INT NOT NULL,
            payment_method VARCHAR(10) NOT NULL,
            total_amount DECIMAL(6,2) NOT NULL,
            location_id INT NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
            FOREIGN KEY (location_id) REFERENCES location(location_id)
        );
        """)
        
        print('...creating transaction_items')
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS transaction_items (
            transaction_items_id SERIAL PRIMARY KEY,
            transaction_id INT NOT NULL,
            order_items VARCHAR(250)
        );
        """)
            # drink_id INT, 
            # drink_flavor_id INT,
            # FOREIGN KEY (transaction_id) REFERENCES customer_transactions(transaction_id),
            # FOREIGN KEY (drink_id) REFERENCES drinks(drink_id),
            # FOREIGN KEY (drink_flavor_id) REFERENCES drink_flavors(drink_flavor_id)
    
        connection.commit()
        print('...committed')
        cursor.close()
        print('Database tables successfully created.')
        return True
    except Exception as ex:
        print(f'Failed to generate table/s:\n{ex}')
        return False
        
if __name__ == "__main__":
    con, cur = open_sql_database_connection_and_cursor()
    create_db_tables(con, cur)