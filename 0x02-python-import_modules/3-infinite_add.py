#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

number = 0
for i in range(len(sys.argv) - 1):
    number += int(sys.argv[i + 1])

print("{}".format(number))
