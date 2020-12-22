# Dylan Andrews, dmandrew@usc.edu
# ITP 115, Fall 2020
# Lab 7

def rectangle(length, width):
    # builds rectangle based on inputted dimensions
    i = 0
    print(" " + "-" * width)
    while i < length:
        print("|" + " " * width + "|")
        i += 1
    print(" " + "-" * width)

    return


def triangle(base):
    # builds triangle based on desired base
    i = 0
    while i < base // 2:
        if i == 0:
            print(" " * (base // 2) + "/" + "\ ")
            i += 1
        else:
            print(" " * ((base // 2) - i) + "/" + " " * (2 * i) + "\ ")
            i += 1
    if base % 2 != 0:
        print(" " * ((base // 2) - i) + "/" + " " * (2 * i) + "\ ")
    print(" " + "-" * base)

    return


def main():
    # initializing so while loop runs once
    cont = "y"
    # runs while the user selects y
    while cont == "Y" or cont == "y":
        # menu option
        print("Welcome to Shape Printer!\nR) Rectangle\nT) Triangle")
        option = input("Enter the shape you want to print: ")
        while option != "R" and option != "r" and option != "t" and option != "T":
            option = input("Enter \"T\" for triangle or \"R\" for rectangle: ")
        # if rectangle selected, user enters length and width desired and sends it to rectangle function
        if option == "r" or option == "R":
            length = input("Enter the length: ")
            while length.isdigit() == False:
                length = input("Enter an integer for the length: ")
            width = input("Enter the width: ")
            while width.isdigit() == False:
                width = input("Enter an integer for the width: ")
            rectangle(int(length), int(width))
        # if triangle selected, user enters base desired and sends it to triangle function
        elif option == "t" or option == "T":
            base = input("Enter the base: ")
            while base.isdigit() == False:
                base = input("Enter an integer for the base: ")
            triangle(int(base))
        # asks if user wants to continue
        cont = input("Do you want to continue (y/n)?: ")
        while cont != "Y" and cont != "y" and cont != "n" and cont != "N":
            cont = input("Please enter \"Y\" to continue or \"n\" to quit: ")


main()