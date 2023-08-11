from extract_data_lambda import read_brew_csv
from transform_data_lambda import transformed_data

def test_read_brew_csv_correct_output(tmpdir):
    # Arrange
    # Create a temporary CSV file for testing
    file_path = tmpdir.join("test.csv")
    with open(file_path, 'w') as file:
        file.write("25/08/2021 09:00,Chesterfield,LBOwNxrHEd,\"Regular Flavoured iced latte - Hazelnut - 2.75, Large Latte - 2.45\",5.2,CARD,2978328181139200\n")
        
    # Call the function and check the output
    data = read_brew_csv(file_path)
    print(data)
  # Assert
    assert data == [
        {'Date Time': '25/08/2021 09:00', 'Location': 'Chesterfield', 'Name': 'LBOwNxrHEd', 'Order': "Regular Flavoured iced latte - Hazelnut - 2.75, Large Latte - 2.45", 'Total': '5.2', 'Payment Method': 'CARD', 'Card No':'2978328181139200'},
        
       ]



















    
def test_transformed_data():
        # Arrange
    data = [{'Date Time': '25/08/2021 09:00', 'Location': 'Chesterfield', 'Name': 'LBOwNxrHEd', 'Order': 'Regular Flavoured iced latte - Hazelnut - 2.75, Large Latte - 2.45', 'Total': 5.2, 'Payment Method': 'CARD'},]
            
    expected_output = [{'Date Time': '25/08/2021 09:00', 'Location': 'Chesterfield', 'Name': 'LBOwNxrHEd', 'Order': ['Regular Flavoured iced latte - Hazelnut - 2.75', 'Large Latte - 2.45'], 'Total': 5.2, 'Payment Method': 'CARD'},]
                       

    # Act
    result = transformed_data(data)

    # Assert
    assert result == expected_output