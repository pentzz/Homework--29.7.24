import statistics


def get_int(a: str = "") -> int:
    """
    This function gets a string from the user and put the string in the input function.
    the user enters non-stop inputs until he enters an int number. the function returns the int number.

    """
    while True:
        try:
            ans: int = int(input(f"{a}"))
            return ans
        except Exception as e:
            print(f"You need to type int number only! {e}")


def my_statistics(a: list[int] = []) -> None:
    """
    This function gets a list of grades from the user and prints :
    the max grade, the min grade, the number of grades in the list, the number of grades above 90,
    and the number of grades below 55, and the standard deviation of the grades

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