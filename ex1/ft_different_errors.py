"""Demonstration of Python exception handling with common error types."""


def garden_operations():
    """
    Test and catch four common Python exceptions individually.

    Tests: ValueError, ZeroDivisionError, FileNotFoundError, KeyError
    Each error is caught and displayed without crashing the program.
    """
    print("=== Garden Error Types Demo ===")

    try:
        print("\nTesting ValueError...")
        int('abc')
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    try:
        print("Testing ZeroDivisionError...")
        10 / 0
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}\n")
    try:
        print("Testing FileNotFoundError...")
        open("missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError:  No such file 'missing.txt'\n")
    try:
        print("Testing KeyError...")
        garden = {"tomato": 5}
        print(garden["missing_plant"])
    except KeyError as error:
        print(f"Caught KeyError: {error}\n")


def test_error_types():
    """
    Run all error handling tests.

    Demonstrates individual error handling and catching multiple
    exception types in a single except block.
    """
    garden_operations()
    try:
        print("\nTesting multiple errors together...")
        int("abc")
        10 / 0
    except (ValueError, ZeroDivisionError, KeyError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")
