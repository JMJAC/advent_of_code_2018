from helpers import load_data_str
from collections import Counter


def ans1(data):
    twos = 0
    threes = 0
    for i in data:
        counter = Counter(i).values()
        if 2 in counter:
            twos += 1
        if 3 in counter:
            threes += 1
    return twos * threes


def compare(first_word, second_word):
    different_letters = 0

    for i, j in zip(first_word, second_word):
        if ord(i) != ord(j):
            different_letters += 1

        if different_letters > 1:
            return 2

    return different_letters


def ans2(data):
    for i in range(len(data)):
        for word in data[i:]:
            if (compare(data[i], word)) == 1:
                return "".join([i for i, j in zip(data[i], word) if j == i])


data = load_data_str("day2_input.txt")
print(ans1(data))
print(ans2(data))

