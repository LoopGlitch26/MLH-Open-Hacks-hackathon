import os

def clear():
    """
    Clears the terminal screen.
    """
    name = os.name
    if name == "nt":
        os.system('cls')
    elif name == "posix":
        os.system('clear')