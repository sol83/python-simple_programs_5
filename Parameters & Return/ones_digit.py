"""
Ones digit

Fill out the function print_ones_digit(num) , which takes as input an integer num and prints its ones digit. The modulo (remainder) operator, %, should be helpful to you here. We've written a main() function which asks for user input and then calls print_ones_digit(num).

Here's a sample run:

$ python ones_digit.py
Enter a number: 42
The ones digit is 2
"""

def print_ones_digit(num):
    # delete the pass statement below and write your code!
    print("The ones digit is", num % 10)

def main():
    num = int(input("Enter a number: "))
    print_ones_digit(num)

if __name__ == "__main__":
    main()
