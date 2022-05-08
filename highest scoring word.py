# Given a string of words, you need to find the highest scoring word.
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
# You need to return the highest scoring word as a string.
# If two words score the same, return the word that appears earliest in the original string.
# All letters will be lowercase and all inputs will be valid.
import string


def high(sent):
    count = []
    score = {letter: value for letter, value in zip(list(string.ascii_lowercase), [x for x in range(1, 27)])}
    for word in sent.split():
        count.append(sum([score[letter] for letter in word]))
    return sent.split()[count.index(max(count))]


if __name__ == "__main__":
    high('man i need a taxi up to ubud')
