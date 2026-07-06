# mutable for no reason,
# should be an enum
# but enum isn't a builtin
# only a stdlib one
# and i am scared of norminette
class GardenOpTest:
    VAL_ERR: int = 0
    ZERO_DIV: int = 1
    FILE_NOT_FOUND: int = 2
    TYPE_ERR: int = 3
    NO_ERR: int = 4


def garden_operations(operation_number: int) -> None:
    def caught_error(e: Exception) -> None:
        print(f"Caught {e.__class__.__name__}: {e}")

    try:
        match operation_number:
            case GardenOpTest.VAL_ERR:
                int("abc")
            case GardenOpTest.ZERO_DIV:
                print(1 / 0)
            case GardenOpTest.FILE_NOT_FOUND:
                open("asfasdfasdf")  # noqa: SIM115
            case GardenOpTest.TYPE_ERR:
                string: str = "a"
                num: int = 1
                result: str = num + string
                print(result)
            case _:
                print("Operation completed successfully")

    except Exception as e:
        caught_error(e)


def test_error_types() -> None:
    print_header("Garden Error Types Demo")

    garden_operations(GardenOpTest.VAL_ERR)
    garden_operations(GardenOpTest.ZERO_DIV)
    garden_operations(GardenOpTest.FILE_NOT_FOUND)
    garden_operations(GardenOpTest.TYPE_ERR)
    garden_operations(GardenOpTest.NO_ERR)

    print_footer("All error types tested successfully!")


def print_header(title: str) -> None:
    print(f"=== {title} ===")
    print("")


def print_footer(msg: str) -> None:
    print("")
    print(msg)


if __name__ == "__main__":
    test_error_types()
