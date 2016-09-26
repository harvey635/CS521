# DEFINITIONS


class OctothorpeError(Exception):
    def __init__(self):
        self.


def get_name():
    print("Please enter a name (if it contains a '#', an error message will appear: ")
    name_input = input()
    if name_input.find('#') > -1:
        raise OctothorpeError()


# EXECUTION

try:
    get_name()
except OctothorpeError:
    print("Exception raised because '#' found")
