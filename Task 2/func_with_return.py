
def my_avg(a: int = 0, b: int = 0) -> float:
    """
    This function gets 3 int numbers from the user and returns the average of the numbers (in float)

    """
    avg: float = (a + b) / 2
    return avg


def my_headline(a: str = "") -> str:
    """
    This function gets a string from the user and returns the string in uppercase and "!" at the end

    """
    a = a.upper() + "!"
    return a


def concat_list(a: list[int] = "", b: list[int] = "", c: list[int] = "") -> list[int]:
    """
    This function gets 3 lists of int numbers from the user and returns a new list of the combined list

    """
    d: list = a + b + c
    return d


def say_bool(a: bool = True) -> str:
    """
    This function gets bool parameter from the user and returns "yes" string if True and "no" string if False.

    """
    ans: str = f"yes" if a == True else "no"
    return ans