# https://www.codewars.com/kata/5977ef1f945d45158d00011f
# Create a function that takes a string and separates it into a sequence of letters.
# The function should separate each word into individual letters,
# with the first word in the sentence having its letters in the 0th index of each 2nd dimension array, and so on.
# Shorter words will have an empty string in the place once the word has already been mapped out.
# (See the last element in the last part of the array.)


def sep_str(st):
    words = st.split()
    result = []
    for index, letter in enumerate(max(words, key=len)):
        tier = []
        for word in words:
            if index + 1 <= len(word):
                tier.append(word[index])
            else:
                tier.append("")
        result.append(tier)
    return result


if __name__ == "__main__":
    sep_str("Just Live Life Man")
