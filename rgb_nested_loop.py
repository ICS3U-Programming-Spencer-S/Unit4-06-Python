#!/usr/bin/env python3

# Created by: Spencer.S
# Created on: November 20, 2022
# A program which displays all RGB values from 0-256


def main():

    # For all red values
    for red in range(256):

        # For all green values
        for green in range(256):

            # For all blue values
            for blue in range(256):
                # Displays all RGB values from 0-256 in order
                # With colours to match the number
                print(
                    "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(
                        red,
                        green,
                        blue,
                        "RGB(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                    )
                )


if __name__ == "__main__":
    main()
