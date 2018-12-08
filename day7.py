from collections import defaultdict
from copy import deepcopy

with open("day7_input.txt") as file:
    reqs = defaultdict(list)
    for line in file.readlines():
        reqs[line.split()[7]].append(line.split()[1])


def ans1(reqs):
    order = ""
    while len(order) != ord(max(reqs.keys())) - ord("A")+1:
        for i in range(ord("A"), ord(max(reqs.keys())) + 1):
            letter = chr(i)
            if not reqs[letter] and letter not in order:
                order += letter
                break
        for i in reqs.keys():
            if letter in reqs[i]:
                reqs[i].remove(letter)
    return order


def ans2(reqs, number_workers, setp_time):
    order = ""
    time = 0
    workers = ["FREE" for _ in range(number_workers)]
    worker_letters = {}
    while True:

        for worker in range(number_workers):
            if workers[worker] == "FREE":
                continue
            workers[worker] -= 1
            if workers[worker] < 0:
                workers[worker] = "FREE"
                for i in reqs.keys():
                    if worker_letters[worker] in reqs[i]:
                        reqs[i].remove(worker_letters[worker])

        for i in range(ord("A"), ord(max(reqs.keys())) + 1):
            letter = chr(i)
            if not reqs[letter] and letter not in order:
                if "FREE" in workers:
                    for worker in range(number_workers):
                        if workers[worker] == "FREE":
                            workers[worker] = ord(letter) - ord("A") + setp_time
                            order += letter
                            worker_letters[worker] = letter
                            break
        if all(workers[i] == "FREE" for i in range(number_workers)):
            break
        time += 1
    return time


print(ans1(deepcopy(reqs)))
print(ans2(deepcopy(reqs), 5, 60))
