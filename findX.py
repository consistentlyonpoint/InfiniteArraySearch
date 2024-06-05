# -*- coding: utf-8 -*-

"""

findX.py - Intro to Graduate Algorithms

Solve the findX in an Infinite array problem using a Divide & Conquer method
Your runtime must be O(log n)

The array of values is indexed A[1..n] inclusive

Your code MUST NOT directly reference any variables in findX.  The following methods are available:

    findX.start(seed) -- returns the value (x) to search for within the array
    findX.lookup(i) -- returns A[i] or None if i>n
    findX.lookups() -- returns the number of calls to lookup

"""
# argparse allows the parsing of command line arguments
import argparse
# utility functions for cs 6515 projects
import GA_ProjectUtils as util


def findXinA(x, findX):

    # def binary_search(i, j, x, look_up_var, cnt):
    def binary_search(i, j, x):
        # print("what is the count: ", cnt)
        # print("what is x? ", x)
        # print("what is i? ", i)
        # print("what is j? ", j)
        if j >= i:
            i_mid_j = i + (j - i) // 2
            new_look_up_var = findX.lookup(i_mid_j)
            # print("what is x? ", x, "\n& the old lookup? ", look_up_var, "\n& the new lookup? ", new_look_up_var)
            if new_look_up_var == x:
                # print("you made it here?")
                theIndex = i_mid_j
                return theIndex
            ###
            # elif x < new_look_up_var:
            if x < new_look_up_var:
                # cnt += 1
                # return binary_search(i, i_mid_j - 1, x, look_up_var, cnt)
                return binary_search(i, i_mid_j - 1, x)
            ####
            else:
                #     # return binary_search(i_mid_j + 1, j, x, look_up_var, cnt + 1)
                return binary_search(i_mid_j + 1, j, x)
        else:
            # return binary_search(j, i, x, look_up_var, cnt + 1)
            # return binary_search(j, i, x)
            return -1

    ###
    i = 0  # current index in the list
    j = 1  # initialize upper bound.
    look_up_var = findX.lookup(j)
    # print("what is x ? (lookup index) \n",findX.lookup(10759))
    # print("what is x ? (literal): ", x)
    # print("x type is : ", type(x))
    # print("look_up_var type is : ", type(look_up_var))
    # ###
    # print("[b4 while] how we doin? \ni: ", i, "\nj: ", j, "\nlook_up_var: ", look_up_var)
    ###
    # cnt = 0
    # if look_up_var is not None:
    #     while look_up_var < x:
    while look_up_var is not None and look_up_var < x:
            # if look_up_var == x:
            #     theIndex = j
            # elif look_up_var < x:
                # j = int(2*j)
                # i = int(j//2)
        i = int(j)
        j = int(2 * j)
        look_up_var = findX.lookup(j)
                # print("[while] how we doin? \ni: ", i, "\nj: ", j, "\nlook_up_var: ", look_up_var)
            # cnt += 1
            ####
    # print("did we get here?")
    # theIndex = binary_search(i, j, x, look_up_var, cnt)
    theIndex = binary_search(i, j, x)
    # print("This is the value in the array at index ", theIndex, ": ", findX.lookup(theIndex))

    # TODOne Your code Ends here, DO NOT MOIDFY ANYTHING BELOW THIS LINE

    numLookups = findX.lookups()

    return theIndex, numLookups


def main():
    """
    main - DO NOT CHANGE ANYTHING BELOW THIS LINE
    """
    # DO NOT REMOVE ANY ARGUMENTS FROM THE ARGPARSER BELOW
    parser = argparse.ArgumentParser(description='Find X Coding Quiz')

    # args for autograder, DO NOT MODIFY ANY OF THESE
    parser.add_argument('-n', '--sName', help='Student name, used for autograder', default='GT', dest='studentName')
    parser.add_argument('-a', '--autograde', help='Autograder-called (2) or not (1=default)', type=int, choices=[1, 2],
                        default=1, dest='autograde')
    parser.add_argument('-s', '--seed', help='seed value for random function', type=int, default=123456, dest='seed')
    parser.add_argument('-l', '--nLower', help='lower bound for N', type=int, default=10, dest='nLower')
    parser.add_argument('-u', '--nUpper', help='upper bound for N', type=int, default=100000, dest='nUpper')

    args = parser.parse_args()

    # DO NOT MODIFY ANY OF THE FOLLOWING CODE

    findX = util.findX()
    x = findX.start(args.seed, args.nLower, args.nUpper)
    index, calls = findXinA(x, findX)
    print('findX result: x found at index {} in {} calls'.format(index, calls))

    return


if __name__ == '__main__':
    main()
