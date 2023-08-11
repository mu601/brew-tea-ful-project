from connect_to_db import *
from generate_sql_db import *
from load_clean_data_into_db import *
from transform_data_lambda import *
from extract_data_lambda import *

if __name__ == "__main__":
   
# print a message to confirm program has been run




    # from extract_data_lamda import read_brew_csv
    # from transform_data_lamda import transformed_data
    # from dummy_data import generate_dummy_csv

    # data = read_brew_csv('brew.csv')
    # transformed_data = transformed_data_lamda(data)
    # generate_dummy_csv('brew.csv', 'our_dummy_data.csv')
    #print(transformed_data)

    # extract_function()
    list_of_dicts = read_brew_csv('brew.csv')
    print(list_of_dicts)

    # transform
    transformed_data = transformed_data(list_of_dicts)

    # load
    conn, cur = open_sql_database_connection_and_cursor
    create_db_tables(conn, cur)
    load_data_into_database() #(list_of_dicts, cur, conn)


