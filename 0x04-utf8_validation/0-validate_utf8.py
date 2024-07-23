#!/usr/bin/python3
"""
Module for UTF-8 validation.
"""

def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): List of integers representing bytes.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    number_of_bytes = 0
    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        mask = 1 << 7
        if number_of_bytes == 0:
            while mask & num:
                number_of_bytes += 1
                mask = mask >> 1

            if number_of_bytes == 0:
                continue

            if number_of_bytes == 1 or number_of_bytes > 4:
                return False
        else:
            if not (num & mask1 and not (num & mask2)):
                return False

        number_of_bytes -= 1

    return number_of_bytes == 0
