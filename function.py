def get_positive_value():
    """
    Prompts the user for value , and reprompys if the value is not nagative.
    """

    value = float(input("(prompt_text): "))
    while value < 0:
        print("sorry, the value can not be negative.")

        value = float(input("prompt_text): "))

        return value

    