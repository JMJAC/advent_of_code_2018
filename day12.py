orders = []
with open("day12_input.txt") as file:
    state = file.readline().split()[2]
    file.readline()
    for line in file.read().split("\n"):
        orders.append(line.split(" => "))


def ans1(state, orders, generations):
    middle = len(state)
    state = "." * len(state) + state + "." * len(state)
    for _ in range(generations):
        plants = []
        for order in orders:
            for i in range(len(state) - 4):
                if (state[i:i + 5]) == order[0]:
                    if order[1] == "#":
                        plants.append(i + 2)
        state = "".join(["#" if i in plants else "." for i in range(len(state))])

    return sum([i - middle for i in range(len(state)) if state[i] == "#"])


def ans2(state, orders, generations):
    middle = len(state)
    state = "." * len(state) + state + "." * len(state)*5
    past_palts = []
    for k in range(generations):
        plants = []
        for order in orders:
            for i in range(len(state) - 4):
                if (state[i:i + 5]) == order[0]:
                    if order[1] == "#":
                        plants.append(i + 2)
        state = "".join(["#" if i in plants else "." for i in range(len(state))])
        if [p-4 for p in plants] in past_palts:
            return sum([i - middle for i in range(len(state)) if state[i] == "#"])+87*(generations-k-1)
        past_palts.append(plants)

    return sum([i - middle for i in range(len(state)) if state[i] == "#"])


print(ans1(state, orders, 20))
print(ans2(state, orders, 50000000000))
