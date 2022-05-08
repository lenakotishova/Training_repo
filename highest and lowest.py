# In this little assignment you are given a string of space separated numbers,
# and have to return the highest and lowest number.
# high_and_low("1 2 -3 4 5") # return "5 -3"


def high_and_low(numbers):
    numbers = sorted([int(x) for x in numbers.split(' ')])
    return str(numbers[-1]) + ' ' + str(numbers[::-1][-1])


if __name__ == "__main__":
    high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")
