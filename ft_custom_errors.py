class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error"):
        self.message = message
    pass


class PlantError(GardenError):
    def __init__(self, name: str, message: str = 
                 "Caught PlantError: the tomato plant is wilting!"):
        self.name = name
        self.message = message


def test_errors() -> None:
    for i in range(6):
        if (i % 2 == 0):
            print("prout")
        else:
            print("ok")


def main() -> None:
    test_errors()


if __name__ == "__main__":
    main()
