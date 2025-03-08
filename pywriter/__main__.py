"""
Pywriter.
Developed by Jesse Amarquaye.
Copyright(C) 2025 Jesse Amarquaye.
"""

from argparse import ArgumentParser, Namespace
from importlib.metadata import version
import sys
import time
from typing import Union


def write(text, rate: Union[float, None] = 0.01):
    """Function to print output with typewriter effect

    >>>
        write(text="Hello world!", rate=1)

        This will print all the elements of the string **Hello world!** one by one at the rate of 1 element per second.
    """

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(rate)
    print()


def reverse(text, rate: Union[float, None] = 0.01):
    """Function to print output with typewriter effect in reverse.

    >>>
        writer(text="Hello world!", rate=1)

        This will print all the elements of the string **Hello world!** one by one
        at the rate of 1 element per second in the reverse order.
        This time it will print **!dlrow olleH** instead.
    """

    reversed_text = text[::-1]
    for char in reversed_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(rate)
    print()


def typewriter(text, new, rate: Union[float, None] = 0.01, idx=None):
    """Function to print output with typewriter effect.
       Deletes some part of the text to some index and prints another text to replace the previous text.

    >>>
        typewriter(text="Hello world!", new="Pythonista", idx=6, rate=1)

        This will print all the elements of the string **Hello world!** one by one
        at the rate of 1 element per second.
        Delete parts of **Hello world** till it reaches the index 6 then prints
        the value of new in the same typewriter effect.
    """

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(rate)
    if idx is not None:
        for i in range(len(text) - 1, idx - 1, -1):
            sys.stdout.write("\b \b")
            sys.stdout.flush()
            time.sleep(rate)
        for char in new:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(rate)
    print()


########################### Miscellaneous functions ###########################


def display_info():
    write(
        """
    pywriter - A command-line writing tool.

    Written by Jesse Amarquaye.

    Copyright (C) 2025 Jesse Amarquaye. This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it under certain conditions.
    See the LICENSE file for more details.

    Project Links:
    - GitHub: https://github.com/amarquaye/pywriter
    - PyPI: https://pypi.org/project/pywriter

    Connect with the Author:
    - LinkedIn: https://www.linkedin.com/in/amarquaye
    - Reddit: https://www.reddit.com/user/amarquaye/
""",
        rate=0.005,
    )


def get_version():
    """Display the version of pywriter"""
    parser = ArgumentParser(
        prog="pywriter",
        description="A command-line writing tool.",
        epilog="Created by Jesse Amarquaye.",
    )

    parser.add_argument(
        "-v", "--version", help="Display the version of pywriter.", action="store_true"
    )
    parser.add_argument(
        "-i", "--info", help="Display information about pywriter.", action="store_true"
    )

    args: Namespace = parser.parse_args()

    if args.version:
        write(version("pywriter"))

    elif args.info:
        display_info()

    else:
        display_info()
