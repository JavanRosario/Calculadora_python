import re

# regex to match a single digit or a dot
NUM_REGEX = re.compile(r'^[0-9.]$')

def is_num_or_dot(string: str) -> bool:
    """
    Check if the input string is a single digit or a dot.

    Args:
        string (str): Input string to check.

    Returns:
        bool: True if the string is a single digit or '.', False otherwise.
    """
    return bool(NUM_REGEX.search(string))

def valid_num(string):

    # if string is empty, consider it valid
    if string == '':
        return True
    # if string has more than one dot, it's invalid
    if string.count('.') > 1:
        return False
    # if removing the dot results in only digits, it's valid
    if string.replace('.', '').isdigit():
        return True
    # try to convert to float, if possible it's valid
    try:
        float(string)
        return True
    except ValueError:
        return False
    

def is_empty(string:str):
    """
    Check if the input string is empty.

    Args:
        string (str): Input string to check.

    Returns:
        bool: True if the string is empty, False otherwise.
    """
    return len(string) == 0



def convert_to_int(string:str):
    number = float(string)

    if number.is_integer():
        number = int(number)
    
    return number