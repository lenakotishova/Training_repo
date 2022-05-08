# https://www.codewars.com/kata/541c8630095125aba6000c00
# Digital root is the recursive sum of all the digits in a number.
#
# Given n, take the sum of the digits of n.
# If that value has more than one digit,
# continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.


def digital_root(n):
    first_digit = [int(x) for x in str(n)]
    while len(first_digit) != 1:
        first_digit = str((sum([int(x) for x in first_digit])))
    return int(''.join(map(str, first_digit)))


if __name__ == "__main__":
    digital_root(493193)
