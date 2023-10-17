file_name = input("Enter a file name: ")
try:
    with open(file_name, 'r') as file:
        line_number = 1
        for line in file:
            print(line.upper(), end='')
            line_number += 1
except FileNotFoundError:
    print("Error!!! This file does not exist.")
