from connect_to_db import open_sql_database_connection_and_cursor
from extract_data_lamda import extract_csv
from transform_data_lamda import transform_raw_data
from generate_sql_db import create_db_tables
from load_clean_data_into_db import load_data_into_database

def lambda_handler(event, handler):

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    print(f'lambda_handler starting key = {key}, bucket = {bucket}')

    # extract
    raw_data = extract_csv(bucket, key)
    print(f'lambda_handler successfully extracted data, key = {key} number of rows = {len(raw_data)}')

    # transform
    trans_data = transform_raw_data(raw_data, key)
    print(f'lambda_handler successfully transformed data, key = {key} number of rows = {len(trans_data)}')

    # load
    conn, cur = open_sql_database_connection_and_cursor()
    create_db_tables(conn, cur)
    boole_2, line_count = load_data_into_database(trans_data, conn, cur, key)
    print(f'lambda_handler successfully processed data, key = {key}, number of rows = {line_count}')
    
    cur.close()
    conn.close()
    print('lambda_handler cursor and connection successfully closed.')
    
    return {
        'statusCode': 200,
        'body': 'successful'
    }

if __name__ == "__main__":
    lambda_handler(None, None)