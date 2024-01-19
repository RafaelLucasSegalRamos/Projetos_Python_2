def xor(*args):
    """
    This function returns True if only one of the arguments is True.
    :param args: This only enter values True or False.
    :return: Will return True if only one of the arguments is True. Otherwise, it will return False.
    """
    for pos, i in enumerate(args):
        for j in range(0, len(args)):
            if pos != j and i != False:
                if i == args[j]:
                    return False
    return True


def get_string(text="Put a value for a String: "):
    """
    This function returns a string value.
    :param text: This is the text that will be displayed.
    :return: Will return a string value.
    """
    return str(input(text))


def get_int(text="Put a value for a Integer: "):
    """
    This function returns a integer value.
    :param text: This is the text that will be displayed.
    :return: Will return a integer value.
    """

    while True:
        texto = input(text)
        if texto.isnumeric():
            return int(texto)
        else:
            print("\033[91mThe value is not a integer.")
            print("Try again.\033[0m", end=" ")


def get_float(text="Put a value for a Float: "):
    """
    This function returns a float value.
    :param text: This is the text that will be displayed.
    :return: Will return a float value.
    """
    while True:
        texto = input(text).replace(",", ".")
        if texto.replace(".", "", 1).isnumeric():
            return float(texto)
        else:
            print("\033[91mThe value is not a float.")
            print("Try again.\033[0m", end=" ")


def get_bool(text="Put a value for BOOL variable [True or False]"):
    texto = input(text).capitalize()
    if texto == "True":
        return True
    elif texto == "False":
        return False
    else:
        print("\033[91mThe value is not a bool.")
        print("Try again.\033[0m", end=" ")


def sum_Dict(*dicts):
    """
    This function returns the sum of two or more dictionaries.
    :param dicts: This is the dictionaries that will be summed.
    :return: Will return the sum of two or more dictionaries.
    """
    d3 = {}
    for i in dicts:
        d3 = {**d3, **i}
    return d3

if __name__ == '__main__':
    pass
