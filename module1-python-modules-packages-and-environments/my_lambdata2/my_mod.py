def enlarge(n):
    """
    Param n is a number

     Function will enlarge the number
    """

    return n * 100

# this code breaks our ability to import enlarge from other files, if left.
#
if __name__ == "__main__":
    #only run the code below if this script in invoked from the command-line
    # not if it is imported from another script
    print("Hello")
    y = int(input("Please choose a number"))
    print(y, enlarge(y))