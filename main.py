# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    """Return a greeting for the given name and print it."""
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    # Use a breakpoint in the code line below to debug your script.
    message = f"Hi, {name}"
    print(message)  # Press ⌘F8 to toggle the breakpoint.
    return message


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    foo = 5
    print(foo)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
