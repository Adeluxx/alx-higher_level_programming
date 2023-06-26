#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Print an integer with "{:d}".format()

    If a ValueError message is caught, corresponding
    message is printed to standard error

    Args:
        value (int): print the integer

    Returns:
        If a TypeError or ValueError occur - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
