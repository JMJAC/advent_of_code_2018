grid_number = 9221
grid = [[int(str(((x + 10) * y + grid_number) * (x + 10))[::-1][2]) - 5 for y in range(1, 301)] for x in range(1, 301)]

cords = {}
for x in range(300 - 3):
    for y in range(300 - 3):
        cords[f"{x + 1}:{y + 1}:{3}"] = sum([grid[i][j] for j in range(y, y + 3) for i in range(x, x + 3)])

print(max(cords, key=cords.get))  # Part 1
for size in range(4, 25):
    for x in range(300 - size):
        for y in range(300 - size):
            cords[f"{x + 1}:{y + 1}:{size}"] = sum([grid[i][j] for j in range(y, y + size) for i in range(x, x + size)])

print(max(cords, key=cords.get))  # Part 2
