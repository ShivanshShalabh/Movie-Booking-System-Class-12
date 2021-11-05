def take_input(input_statement="Your choice: ", error_message="Invalid Input", input_type='str', input_range=None):
    """
    This function takes input from the user of specific datatype and format and returns it.
    """
    input_value = input(input_statement)
    if input_type == 'str':
        if not input_range:
            while not input_value:
                print(error_message)
                input_value = input(input_statement)
        else:
            while not input_value or len(input_value) not in range(input_range[0], input_range[1]):
                print(
                    f'The length of the input should be in the range of  {input_range[0]}, {input_range[1]}')
                input_value = input(input_statement)

    elif input_type == 'int' or input_type == 'float':
        if input_range:

            while (not (input_value.replace('.', '', 1) if input_type == 'float' else input_value).isdigit() and input_type == 'int') or int(input_value) not in input_range:
                print(error_message)
                input_value = input(input_statement)
        else:
            while not input_value.isdigit():
                print(error_message)
                input_value = input(input_statement)

    return input_value