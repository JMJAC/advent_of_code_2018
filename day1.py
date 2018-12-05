from helpers import load_data_int


def ans1(changes):
    return sum(changes)


def ans2(changes):
    frequency = 0
    memory = set()

    while True:
        for i in changes:
            memory.add(frequency)
            frequency += i
            if frequency in memory:
                return frequency


data = load_data_int("da1_input.txt")
print(ans1(data))
print(ans2(data))