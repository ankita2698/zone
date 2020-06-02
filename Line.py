"""
Project for Week 2 of "Python Data Visualization".
Read World Bank GDP data and create some basic XY plots.
Be sure to read the project description page for further information
about the expected behavior of the program.
@author: salimt
"""

import csv
import pygal


def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - Name of CSV file
      keyfield  - Field to use as key for rows
      separator - Character that separates fields
      quote     - Character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    

    with open(filename, 'r') as csvfile:
        fields = {}
        reader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        for line in reader:
            temp = dict(line)
            fields[temp.get(keyfield)] = temp
            
    return fields

### TEST
#result = {'1': {'Field4': '4', 'Field3': '3', 'Field1': '1', 'Field2': '2'}, 
#          '5': {'Field4': '8', 'Field3': '7', 'Field1': '5', 'Field2': '6'}, 
#          '9': {'Field4': '12', 'Field3': '11', 'Field1': '9', 'Field2': '10'}}
#
#if read_csv_as_nested_dict('table1.csv', 'Field1', ',', '"') == result:
#    print("True")
#else:
#    print("False")
    
 
