# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits
# that occur more than once in the input string. The input string can be assumed to contain only alphabets
# (both uppercase and lowercase) and numeric digits.

def duplicate_count(text):
    return len(set([letter for letter in text.lower() if text.lower().count(letter) > 1]))



print(duplicate_count("abcdeaB"))
print(duplicate_count("Indivisibilities"))

