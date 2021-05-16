"""
Get name

Fill out the get_name() function to return your name as a string! We've written a main() function for you which calls your function to retrieve your name and then prints it in a greeting.

Here's a sample run of the program where the name we've decided to return is Karel:

$ python get_name.py
Howdy Karel ! 🤠
"""


def get_name():
    # delete the pass statement below and write your code here!
    return "Solon"

def main():
    name = get_name() # get_name() will return a string which we store to the 'name' variable here
    print("Howdy", name, "! 🤠")

if __name__ == "__main__":
    main()
