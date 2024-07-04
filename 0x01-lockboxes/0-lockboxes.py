#!/usr/bin/python3
"""
This module provides a function to determine if all boxes can be unlocked.
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.
    
    Args:
        boxes (list of lists): A list where each element is a list of keys for other boxes.
    
    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    if not boxes:
        return False
    
    n = len(boxes)
    opened = [False] * n
    opened[0] = True  # The first box is always open
    
    queue = [0]  # Start with the first box

    while queue:
        current_box = queue.pop(0)  # Get the next box to check
        for key in boxes[current_box]:
            if key < n and not opened[key]:  # If the key opens a new box
                opened[key] = True
                queue.append(key)

    return all(opened)  # Check if all boxes are opened
