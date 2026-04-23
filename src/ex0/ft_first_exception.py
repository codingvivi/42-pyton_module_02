def input_temperature(temp_str: str) -> int:
    temp: int = int(temp_str)
    print(f"Temperature is now {temp}C")
    return temp


def test_temperature() -> None:
    def run_test(data: str) -> None:
        print(f"Input data is '{data}'")
        try:
            input_temperature(data)
        except Exception as e:
            print(f"Caught {input_temperature.__name__} error: {e}")
        print("")

    print("=== Garden Temperature ===")
    run_test("25")
    run_test("abc")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
