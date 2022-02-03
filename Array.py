# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def array():
    try:
        # Use a breakpoint in the code line below to debug your script.
        a=[1.00, 2, 3, 4] # Can store all types of variables in python
        a[1]=6
        print(a[:])  # Fetch all elements of an array
        print(a[:-1])  # Fetch all elements expect the last element of an array
        print(f'Hi, {"Arya"}')  # Press Ctrl+F8 to toggle the breakpoint.

        # Linear Search O(N)

        max  = a[0]
        for i in a:
            if i > max :
                max  = i

        print(max )
    except TypeError as e:
        print(f"Caught exception", {e}, {type(e)})


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    array()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/