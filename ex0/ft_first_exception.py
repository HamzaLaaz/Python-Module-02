def check_temperature(temp_str):
    """
    Check if temperature is suitable for plants (0-40°C).

    Args:
        temp_str: Temperature as string

    Prints error for invalid/out-of-range values.
    """
    try:
        temp_int = int(temp_str)
        if temp_int > 40:
            print(f"Error: {temp_int}°C is too hot for plants (max 40°C)\n")
        elif temp_int < 0:
            print(f"Error: {temp_int}°C is too cold for plants (min 0°C)\n")
        else:
            print(f"Temperature {temp_int}°C is perfect for plants!\n")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")


def test_temperature_input():
    """Run automated tests for check_temperature function."""
    print("=== Garden Temperature Checker ===\n")
    temp_test = ["25", "abc", "100", "-50"]
    for temp in temp_test:
        print(f"Testing temperature: {temp}")
        check_temperature(temp)
    print("All tests completed - program didn't crash!")
