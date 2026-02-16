def water_plants(plant_list):
    """Water all plants in the list and close the watering system."""
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise Exception(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except Exception as error:
        print("Error:", error)
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """Test watering system with valid and invalid plant lists."""
    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    good_plant = ["tomato", "lettuce", "carrots"]
    water_plants(good_plant)
    print("Watering completed successfully!\n")

    print("Testing with error...")
    bad_plant = ["tomato", None]
    water_plants(bad_plant)
    print("\nCleanup always happens, even with errors!")
