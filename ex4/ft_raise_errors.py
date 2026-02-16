def check_plant_health(plant_name, water_level, sunlight_hours):
    """Check plant health. Raises ValueError if parameters invalid."""
    if plant_name == "":
        raise ValueError("Plant name cannot be empty!")
    elif water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    elif water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    elif sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is "
                         f"too low (min 2)")
    elif sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} is "
                         f"too high (max 12)")
    else:
        return f"Plant '{plant_name}' is healthy!\n"


def test_plant_checks():
    """
    Test plant health validation with various inputs.
    Demonstrates error raising and handling for invalid plant parameters.
        """
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    try:
        print(check_plant_health("tomato", 1, 2))
    except ValueError as error:
        print(f"Error: {error}\n")
    print("Testing empty plant name...")
    try:
        print(check_plant_health("", 1, 2))
    except ValueError as error:
        print(f"Error: {error}\n")
    print("Testing bad water level...")
    try:
        print(check_plant_health("tomato", 15, 2))
    except ValueError as error:
        print(f"Error: {error}\n")
    print("Testing bad sunlight hours...")
    try:
        print(check_plant_health("tomato", 1, 0))
    except ValueError as error:
        print(f"Error: {error}\n")

    print("All error raising tests completed!")
