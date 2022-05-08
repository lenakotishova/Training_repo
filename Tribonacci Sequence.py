# https://www.codewars.com/kata/556deca17c58da83c00002db
# Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function that given
# a signature array/list, returns the first n elements - signature included of the so seeded sequence.
# Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, then return
# an empty array (except in C return NULL) and be ready for anything else which is not clearly specified ;)


def tribonacci(signature, n):
    while len(signature) < n:
        for x in range(n):
            signature.append(sum(signature[-3:]))
    return signature[:n]


if __name__ == "__main__":
    tribonacci([0.5, 0.5, 0.5], 30)
