import string

with open("day5_input.txt") as file:
    polymer_original = file.read()


def get_reaction(polymer):
    last_len = 0
    polymer = list(i for i in polymer)
    while len(polymer) != last_len:

        last_len = len(polymer)
        new_polymer = polymer
        reaction = False
        reactions = []

        for i in range(1, last_len):
            if abs(ord(new_polymer[i]) - ord(new_polymer[i - 1])) == 32 and not reaction:
                reactions.append(i)
                reactions.append(i - 1)
                reaction = True
            else:
                reaction = False
        for i in sorted(reactions)[::-1]:
            del polymer[i]
        polymer = new_polymer
    return polymer


def ans1(polymer):
    return len(get_reaction(polymer))


def ans2(polymer):
    polymer = "".join(get_reaction(polymer))
    lens = []
    for letter in string.ascii_lowercase:
        lens.append(len(get_reaction(polymer.replace(letter, "").replace(letter.upper(), ""))))
    return min(lens)


print(ans1(polymer_original))
print(ans2(polymer_original))
