GREEN = "\033[32m"
RESET = "\033[0m"


def water_plant(plant_name: str) -> None:
    if ("A" <= plant_name[0] <= "Z") is False:
        raise ValueError(f"Invalid plant name to water {plant_name}")
    print(f"Watering {plant_name}: {GREEN}[OK]{RESET}")


def test_watering_system(*args) -> None:
    print("Opening watering system")
    try:
        for a in args:
            water_plant(a)
    except Exception as e:
        caught_error(e)
        print("..ending tests and returning to main")
    finally:
        print("Closing watering system")
        print("")


def main() -> None:
    print_header("Garden Watering System")

    print_test_header("valid plants")
    test_watering_system("Tomato", "Lettuce", "Carrots")

    print_test_header("invalid plants")
    test_watering_system("tomato", "lettuce", "carrots")

    print("Cleanup always happens, even with errors!")


def caught_error(e: Exception) -> None:
    print(f"Caught {e.__class__.__name__}: {e}")


def print_test_header(error: str) -> None:
    print(f"Testing {error}...")


def print_header(title: str) -> None:
    print(f"=== {title} ===")
    print("")


if __name__ == "__main__":
    main()
