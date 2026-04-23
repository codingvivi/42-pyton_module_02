class GardenError(Exception):
    def __str__(self) -> str:
        return "Unknown plant error"


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def caught_error(func, e: Exception) -> None:
    print(f"Caught {func.__name__} error: {e}")


def test_plant_error() -> None:
    pass


def test_water_error() -> None:
    pass


def test_garden_error() -> None:
    pass


if __name__ == "__main__":
    test_garden_error()
