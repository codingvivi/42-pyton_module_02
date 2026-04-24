class Plant:
    def __init__(self, name: str, height_cm: int, age_days: int) -> None:
        self.name: str = name
        self.height_cm: int = height_cm
        self.age_days: int = age_days

    def show(self) -> None:
        age_unit_name: str = "day" if self.age_days == 1 else "days"
        print(f"{self.name.capitalize()}: {self.height_cm}cm, {self.age_days} {age_unit_name} old")


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
                open("asfasdfasdf")
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

    print_footer("All error types tested sucessfully")


def print_header(title: str) -> None:
    print(f"=== {title} ===")
    print("")


def print_footer(msg: str) -> None:
    print("")
    print(msg)


if __name__ == "__main__":
    test_error_types()
