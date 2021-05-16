"""
Chaotic counting

Fill out the chaotic_counting() function, which prints the numbers from 1 to 10, but with a catch. We've written a done() function which returns True with likelihood DONE_LIKELIHOOD -- at each number, before printing the number, you should call done() and check if it returns True or not. If done() returns True, we're done counting, and you should use a return statement to end the chaotic_counting() function execution and resume execution of main(), which will print "I'm done.". We've written main() for you -- check it out! Notice that we'll only print "I'm done" from main() once chaotic_counting() is done with its execution.

Here's a sample run of this sassy program:

$ python chaotic_counting.py
I'm going to count until 10 or until I feel like stopping, whichever comes first.
1
2
3
I'm done.
"""

import random

DONE_LIKELIHOOD = 0.3

def chaotic_counting():
    # write your code below!
    for i in range(10):
        num = i + 1
        if done():
            return # this ends the function execution, so we'll get back to the main() function!
        print(num)

def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done")

if __name__ == "__main__":
    main()
