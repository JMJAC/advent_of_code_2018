from helpers import load_data_str
import time


def get_data_from_line(line):
    data = line.split()
    id = data[0].strip("#")
    col, row = data[2].split(",")
    size_x, size_y = data[3].split("x")
    return id, int(col), int(row[:-1]), int(size_x), int(size_y)


def ans1(data):
    fabric = [[0 for i in range(1005)] for i in range(1005)]
    for line in data:
        id, col, row, size_x, size_y = get_data_from_line(line)
        for x in range(size_x):
            for y in range(size_y):
                if fabric[col + x][row + y] == "X":
                    continue
                if fabric[col + x][row + y] != 0:
                    fabric[col + x][row + y] = "X"
                else:
                    fabric[col + x][row + y] = id
    total = 0
    for i in fabric:
        for j in i:
            if j == "X":
                total+=1
    return total


def ans2(data):
    memory = [i for i in range(0,1228)]
    fabric = [[0 for i in range(1005)] for i in range(1005)]
    for line in data:
        id, col, row, size_x, size_y = get_data_from_line(line)
        for x in range(size_x):
            for y in range(size_y):
                if fabric[col + x][row + y] == "X":
                    memory[int(id)] = 0
                    continue
                if fabric[col + x][row + y] != 0:
                    memory[int(fabric[col + x][row + y])] = 0
                    memory[int(id)] = 0
                    fabric[col + x][row + y] = "X"
                else:
                    fabric[col + x][row + y] = id

    return sum(memory)


data = load_data_str("day3_input.txt")
print(ans1(data))
print(ans2(data))
