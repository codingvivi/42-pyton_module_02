class GardenError(Exception):
    def __init__(self, message: str = "Unkown plant error") -> None:
        self.args = (message,)


class PlantError(GardenError):
    def __init__(self, plant: str | None , problem: str | None) -> None:
        if plant is None or problem is None:
        super().__init__()
    pass


class WaterError(GardenError):
    pass


class Plant:
    def __init__(self, name: str, hours_since_watered: int = 0) -> None:
        self.name: str = name
        self.hours_since_watered: int = hours_since_watered

    def is_wilting(self) -> bool:
        return self.hours_since_watered >= 24


class WaterTank:
    def __init__(self, level_liters: float, capacity_liters: float) -> None:
        self.level_liters: float = level_liters
        self.capacity_liters: float = capacity_liters

    def has_enough(self, required_liters: float) -> bool:
        return self.level_liters >= required_liters


def caught_error(func, e: Exception) -> None:
    print(f"Caught {func.__name__} error: {e}")


def test_plant_error() -> None:
    # scenario: a tomato plant has not been watered for too long and is wilting
    tomato = Plant("tomato", hours_since_watered=48)

    if tomato.is_wilting is True
    raise PlantError(f"The")


def test_water_error() -> None:
    # scenario: the water tank is almost empty and cannot cover the round
    tank = WaterTank(level_liters=0.5, capacity_liters=20.0)
    required_liters = 5.0


def test_garden_error() -> None:
    # both of the above conditions are present in the garden at once
    tomato = Plant("tomato", hours_since_watered=48)
    tank = WaterTank(level_liters=0.5, capacity_liters=20.0)
    required_liters = 5.0


def main() -> None:
    test_garden_error()


def print_header(title: str) -> None:
    print(f"=== {title} ===")
    print("")


def print_footer(msg: str) -> None:
    print("")
    print(msg)


if __name__ == "__main__":
    main()
