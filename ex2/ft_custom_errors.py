class GardenError(Exception):
    """Base class for all garden related errors"""
    pass


class PlantError(GardenError):
    """Error related to plants"""
    pass


class WaterError(GardenError):
    """Error related to watering"""
    pass


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===")
    try:
        print("\nTesting PlantError...")
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    try:
        print("\nTesting WaterError...")
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")
