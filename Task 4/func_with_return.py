def return_zugi(a: list[int] = []) -> list[str]:
    """
    This function gets a list of numbers from the user and returns a new list for "even" or "odd" [depends on the index].

    """
    zugi: list =["even" if a[i] % 2 == 0 else "odd" for i in range(len(a))]
    return zugi

