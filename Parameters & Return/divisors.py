"""
Print divisors

Fill out the function print_divisors(num), which takes in a number and prints all of its divisors (all the numbers from 1 to num inclusive that num can be cleanly divided by (there is no remainder to the division). We've given you a main() which prompts the user to input a number and then calls your code for print_divisors(num).

Here's a sample run:

$ python divisors.py
Enter a number: 12
Here are the divisors of 12
1
2
3
4
6
12
"""

def print_divisors(num):
    # write your code below!
    print("Here are the divisors of", num)
    for i in range(num):
        divisor = i + 1
        if num % divisor == 0:
            print(divisor)
def main():
    num = int(input("Enter a number: "))
    print_divisors(num)

if __name__ == "__main__":
    main()
