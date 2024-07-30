def say_bool(a: bool = True) -> str:
    """
    This function gets bool parameter from the user and returns "yes" string if True and "no" string if False.

    """
    ans: str = f"yes" if a else "no"
    return ans
