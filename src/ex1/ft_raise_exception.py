class GardenTempError(ValueError):
    def __init__(self, temp: int, bound: str):
        if bound == "max":
            self.args = (f"{temp}°C is too hot for plants (max 40°C)",)
        elif bound == "min":
            self.args = (f"{temp}°C is too cold for plants (min 0°C)",)
        else:
            raise ValueError("bound must be 'min' or 'max'")


def caught_error(e: Exception) -> None:
    print(f"Caught {input_temperature.__name__} error: {e}")


def input_temperature(temp_str: str) -> int:
    temp: int = int(temp_str)
    if temp < 0:
        raise GardenTempError(temp, "min")
    if temp > 40:
        raise GardenTempError(temp, "max")
    print(f"Temperature is now {temp}C")
    return temp


def test_temperature() -> None:
    def run_test(data: str) -> None:
        print(f"Input data is '{data}'")
        try:
            input_temperature(data)
        except Exception as e:
            caught_error(e)
        print("")

    print("=== Garden Temperature ===")
    print("")
    run_test("25")
    run_test("abc")
    run_test("100")
    run_test("-50")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
