## takes data from extract function then for the items ordered it separates order in a list
def transformed_data(data):
    try:
        transformed_list = []
        for row in data:
            orders = []
            order_name = row['Order'].split(',')
            for order in order_name:
                orders.append(order.strip())
            # print(f"Date Time: {row['Date Time']}\nLocation: {row['Location']}\nName: {row['Name']}\nOrder: {orders}\nTotal: {row['Total']}\nPayment Method: {row['Payment Method']}\n")
            transformed_list.append({'Date Time': row['Date Time'], 'Location': row['Location'], 'Name': row['Name'], 'Order': orders , 'Total': row['Total'],'Payment Method': row['Payment Method']})
            # print(transformed_data)
        return transformed_list
    except Exception as e:
        print(f'Not able to transform file: {e}')












