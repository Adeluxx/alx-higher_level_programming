#!/usr/bin/python3
"""Defines a Magic class matching exactly a bytecode provided by Holberton."""

import math


class MagicClass:
    """Represents a circle"""

    def __init__(self, radius=0):
        """Initialize a Magic class.

        Arg:
            radius (float or int): The radius of the new Magic class.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the Magic class"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return The circumference of the Magic class."""
        return (2 * math.pi * self.__radius
