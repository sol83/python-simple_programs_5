"""
Is even

Fill out the is_even(num) function which returns whether or not the inputted integer num is even. Your function should return a boolean. We've written a main() function which asks a user for input and then prints whether or not the number is by calling your is_even(num) function to verify.

Here's a sample run of the program:

$ python is_even.py
Enter a number: 20
That number is even!
"""

def is_even(num):
    # write your code below!
    if num % 2 == 0:
        return True
    return False    

def main():
    num = int(input("Enter a number: "))
    if is_even(num):
        print("That number is even!")
    else:
        print("That number is not even!")

if __name__ == "__main__":
    main()

