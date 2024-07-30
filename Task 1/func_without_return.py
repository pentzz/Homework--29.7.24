import statistics


def my_ascending(a: int = 0, b: int = 0) -> None:
    """
    This function gets 2 int numbers from the user and print it from low to high.

    """
    print(f"{a}, {b}" if a < b else f"{b}, {a}")


def my_details(a: str = "") -> None:
    """
    This function gets a string from the user and prints the first letter, the middle letter, and the last letter.

    """
    print(f"{a[0]}{a[len(a) // 2]}{a[-1]}")


def say_bool(a: bool = True) -> None:
    """
    This function gets bool parameter from the user and prints "yes" if True and "no" if False.

    """
    print(f"yes" if a == True else "no")


def print_zugi(a: list[int] = []) -> None:
    """
    This function gets a list of numbers from the user and prints a new list for "even" or "odd" [depends on the index].

    """
    zugi: list =["even" if a[i] % 2 == 0 else "odd" for i in range(len(a))]
    print(zugi)


def my_statistics(a: list[int] = []) -> None:
    """
    This function gets a list of grades from the user and prints :
    the max grade, the min grade, the number of grades in the list, the number of grades above 90,
    and the number of grades below 55 and the standard deviation of the grades.

    """
    excellent: list[int] = [a[i] for i in range(len(a)) if a[i] > 90]
    fails: list[int] = [a[i] for i in range(len(a)) if a[i] < 55]
    sd: list[int] = [(a[i]-statistics.mean(a)) * (a[i]-statistics.mean(a)) for i in range(len(a))]
    sd2: int = pow(statistics.mean(sd), 0.5)

    print(f"The highest grade is: {max(a)}\n"
          f"The lowest grade is: {min(a)}\n"
          f"The number of grades inserted is: {len(a)}\n"
          f"The average is: {statistics.mean(a)}\n"
          f"The number of excellent grades is {len(excellent)}\n"
          f"The number of fails grades is {len(fails)}\n"
          f"The standard deviation of the grades is: {sd2:.2f}")
