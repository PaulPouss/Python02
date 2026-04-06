def garden_operations(operation_number: int) -> None:
    if (operation_number == 0):
        raise (ValueError)
    elif (operation_number == 1):
        raise (ZeroDivisionError)
    elif (operation_number == 2):
        raise (FileNotFoundError)
    elif (operation_number == 3):
        raise (TypeError)
    return