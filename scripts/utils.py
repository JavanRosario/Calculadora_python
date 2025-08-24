import re

NUM_REGEX = re.compile(r'^[0-9.]$')


def valid_num(string):
    checked = False
    try:
        float(string)
        checked = True
    except ValueError:
        checked = False

    return checked
