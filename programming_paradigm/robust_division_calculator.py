#!/usr/bin/env python3
"""
This module provides a function for robustly dividing two numbers.
"""

def safe_divide(numerator, denominator):
    """
    Performs division and handles non-numeric inputs and division by zero.

    Args:
        numerator (str): The number to be divided.
        denominator (str): The number to divide by.

    Returns:
        str: A string containing the result of the division or an
             error message.
    """
    try:
        num = float(numerator)
        den = float(denominator)
        result = num / den
        return f"The result of the division is {result}"
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
