#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Nov. 17, 2023
# This program displays all possible colour combinations for RGB using nested loops.


def main():
    # introduce program to user
    print(
        "This program displays all possible colour combinations for RGB using nested loops."
    )

    # initialize counter/variables
    red = 0
    green = 0
    blue = 0

    # for loop for all colours
    for red in range(256):
        for green in range(256):
            for blue in range(256):
                print("RGB ({}), ({}), ({})".format(red, green, blue))


if __name__ == "__main__":
    main()
