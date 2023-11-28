#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevents the user from creating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
