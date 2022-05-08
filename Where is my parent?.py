# https://www.codewars.com/kata/58539230879867a8cd00011c
# Legend:
# -Uppercase letters stands for mothers, lowercase stand for their children, i.e. "A" mother's children are "aaaa".
# -Function input: String contains only letters, uppercase letters are unique.
# Task:
# Place all people in alphabetical order where Mothers are followed by their children, i.e. "aAbaBb" => "AaaBbb".
import string


def find_children(dancing_brigade):
    result = ""
    alpha_upper = sorted([x for x in dancing_brigade if x in string.ascii_uppercase])
    alpha_low = sorted([x for x in dancing_brigade if x in string.ascii_lowercase])
    for upper in alpha_upper:
        result += upper
        for lower in alpha_low:
            if lower.upper() == upper:
                result += lower
    return result


if __name__ == "__main__":
    find_children("AaaaaZazzz")
