def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    return (int(temp_str))


def main():
    print(f"{input_temperature("abc")}")


if __name__ == "__main__":
    main()