from datetime import datetime
from math import ceil


def take_input(input_statement="Your choice: ", error_message="Invalid Input", input_type='str', input_range=None):

    input_value = input(input_statement)
    if input_type == 'str':
        if not input_range:
            while not input_value:
                print(error_message)
                input_value = input(input_statement)
        else:
            while not input_value or len(input_value) not in range(input_range[0], input_range[1]):
                print(
                    f'The length of the input should be in the range of  {input_range[0]}, {int(input_range[1])-1}')
                input_value = input(input_statement)
        return input_value

    elif input_type == 'int' or input_type == 'float':
        if input_range:
            while(not ((input_value.replace('.', '', 1) if input_type == 'float' else input_value).isdigit() and ceil(float(input_value)) in range(input_range[0], input_range[1]))):
                print(error_message)
                input_value = input(input_statement)
        else:
            while (not (input_value.replace('.', '', 1) if input_type == 'float' else input_value).isdigit()):
                print(error_message)
                input_value = input(input_statement)

        return int(input_value) if input_type == 'int' else float(input_value)
    elif input_type == 'date':
        while True:
            try:
                input_value = str(datetime.strptime(
                    input_value, '%d/%m/%Y').date())
                break
            except ValueError:
                print(error_message, "enter the date in DD/MM/YYYY format")
                input_value = input(input_statement)
        return input_value
    elif input_type == 'email':
        while True:
            if '@' in input_value and '.' in input_value:
                break
            else:
                print(error_message)
                input_value = input(input_statement)
        return input_value
