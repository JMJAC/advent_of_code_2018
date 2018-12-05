def load_data_int(src):
    result = []
    with open(src) as file:
        for line in file.readlines():
            result.append(int(line))
    return result


def load_data_str(src):
    result = []
    with open(src) as file:
        for line in file.readlines():

            result.append(line.strip("\n"))
    return result

