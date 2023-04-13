import math
import sys
from functions import add_numbers, multiply_numbers

def main():
    print("Hello World")
    ret1 = add_numbers(1, 2)
    ret2 = multiply_numbers(3, 4)
    print(ret1)
    print(ret2)
    # inはリストに含まれているかどうか
    # in
    if 1 in [1, 2, 3]:
        print("1 is in the list")
    # not in
    if 1 not in [2, 3, 4]:
        print("1 is not in the list")
    # isはオブジェクトが同じかどうか
    # is
    if 1 is 1:
        print("1 is 1")
    # is not
    if 1 is not 2:
        print("1 is not 2")
    # and
    if 1 == 1 and 2 == 2:
        print("1 is 1 and 2 is 2")
    # or
    if 1 == 1 or 2 == 3:
        print("1 is 1 or 2 is 3")
    else:
        print("1 is not 1 or 2 is not 3")

    
    

if __name__ == "__main__":
	main()