with open("day10_input.txt") as file:
    data = [line.replace("<", " ").replace(">", " ").replace(",", "") for line in file.readlines()]
    data = [[line.split()[1], line.split()[2], line.split()[4], line.split()[5]] for line in data]
    coord = [[int(i[0]), int(i[1])] for i in data]
    v = [[int(i[2]), int(i[3])] for i in data]


def draw(points, t):
    middle = 1000
    line = "." * middle * 2
    lines = [line for _ in range(middle * 2)]
    for x, y in points:
        lines[middle + y] = lines[middle + y][:middle + x] + "X" + lines[middle + y][middle + x + 1:]

    to_print = 0
    lines_to_print = []
    for line in lines:
        if line != "." * middle * 2:
            lines_to_print.append(line[400:-400])
            to_print += 1

    if to_print < 20:
        [print(line) for line in lines_to_print]
        print(t)
        return True

    return False


t = 0
while True:
    t += 1
    for i in range(len(data)):
        coord[i][0] += v[i][0]
        coord[i][1] += v[i][1]
    if abs(coord[0][0]) < 400 and abs(coord[0][1]) < 400:
        if draw(coord, t):
            break
