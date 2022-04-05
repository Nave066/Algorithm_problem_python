def check_anagram(inp, check):
    """
    :param inp: input string
    :param check: Input string to be checked for anagram
    :return: Whether both inputs are anagram or not
    """
    if len(inp) == len(check):
        if sorted(inp) == sorted(check):
            return "Both are anagrams"
        else:
            return "Both are not anagrams"
    else:
        return "Not anagram"


if __name__ == "__main__":
    input_text = input("Please enter the string: ")
    checking_text = input("Please Enter checking string: ")
    print(check_anagram(input_text, checking_text))
