class GardenError(Exception):
    _default_message = "Unknown plant error"

    def __init__(self, message: str | None = None) -> None:
        super().__init__(
            message if message is not None else self._default_message
        )


class PlantError(GardenError):
    def __init__(
        self, plant: str | None = None, problem: str | None = None
    ) -> None:
        # XOR
        if (plant is None) != (problem is None):
            raise TypeError(
                "Plant error requires both plant and problem "
                "(or neither default msg)"
            )
        # plant and problem must both be true or false at this point,
        # so only checking plant is fine
        if plant is None:
            super().__init__(self._default_message)
        else:
            super().__init__(f"The {plant} plant {problem}!")


class WaterError(GardenError):
    _default_message = "Not enough water in the tank!"

    def __init__(self, message: str | None = None) -> None:
        super().__init__(
            message if message is not None else self._default_message
        )


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


def caught_error(e: Exception) -> None:
    print(f"Caught {e.__class__.__name__}: {e}")


def test_plant_error() -> None:
    tomato = Plant("tomato", hours_since_watered=48)
    if tomato.is_wilting() is True:
        raise PlantError("tomato", "is wilting")
    print("")


def test_water_error() -> None:
    tank = WaterTank(level_liters=0.5, capacity_liters=20.0)
    required_liters = 5.0
    if tank.has_enough(required_liters) is False:
        raise (WaterError)
    print("")


def test_garden_error() -> None:
    try:
        test_plant_error()
    except GardenError as ge:
        caught_error(ge)
    try:
        test_water_error()
    except GardenError as ge:
        caught_error(ge)


def main() -> None:
    print_header("Custom Garden Errors Demo")

    print_test_header(PlantError.__name__)
    try:
        test_plant_error()
    except PlantError as pe:
        caught_error(pe)
    print("")

    print_test_header(WaterError.__name__)
    try:
        test_water_error()
    except WaterError as we:
        caught_error(we)
    print("")

    print_test_header("all garden errors")
    test_garden_error()

    print_footer("All custom error types work correctly")


def print_test_header(error: str) -> None:
    print(f"Testing {error}...")


def print_header(title: str) -> None:
    print(f"=== {title} ===")
    print("")


def print_footer(msg: str) -> None:
    print("")
    print(msg)


if __name__ == "__main__":
    main()
