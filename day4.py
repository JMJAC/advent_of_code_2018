from collections import namedtuple, defaultdict, Counter


with open("day4_input.txt") as file:
    Log = namedtuple("Log", "date event")
    logs = [Log(" ".join(x.split()[0:2]), " ".join(x.split()[2:])) for x in
            file.read().replace("[", "").replace("]", " ").replace("#", " ").split("\n")]
    logs.sort(key=lambda x: x.date)


def get_times(logs):
    guards_times = defaultdict(list)

    for i in range(len(logs)):
        event = logs[i].event.split()

        if event[0] == "Guard":
            guard_id = event[1]

        if event[0] == "falls":
            falls = int(logs[i].date[14:])

            if logs[i + 1].event.split()[0] == 'wakes':
                wakes = int(logs[i + 1].date[14:])
            else:
                wakes = 59
            guards_times[guard_id].extend(list(range(falls, wakes)))

    return guards_times


def ans1(logs):
    guards_times = get_times(logs)
    guard_id = max(guards_times.keys(), key=lambda x: len(guards_times[x]))
    return Counter(guards_times[guard_id]).most_common()[0][0] * int(guard_id)


def ans2(logs):
    guards_times = get_times(logs)
    guard_id = max(guards_times.keys(), key=lambda x: Counter(guards_times[x]).most_common()[0][1])
    return int(guard_id) * Counter(guards_times[guard_id]).most_common()[0][0]


print(ans1(logs))
print(ans2(logs))
