# https://www.codewars.com/kata/590148d79097384be600001e/train/python
# You're given an array of positive integers arr, and an array guide of the same length.
# Sort array arr using array guide by the following rules:
# if guide[i] = -1, arr[i] shouldn't be sorted;
# if guide[i] ≠ -1, arr[i] should be sorted,
# and among all elements that should be sorted,
# arr[i] should be the guide[i]th one (1-based).

def sort_by_guide(arr, guide):
    result = []
    res = sorted([(a, b)  for a, b in zip(arr, guide) if b != -1], key=lambda x: x[1])
    for a, b in zip(arr, guide):
        if b != -1:
            result.append(res.pop(0)[0])
        else:
            result.append(a)
    return result


if __name__ == "__main__":
    sort_by_guide([56, 78, 3, 45, 4, 66, 2, 2, 4], [3, 1, -1, -1, 2, -1, 4, -1, 5])
