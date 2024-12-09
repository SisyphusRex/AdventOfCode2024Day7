def main(*args):
    """main method"""

    data = get_data("test_data.txt")
    print(data)


def get_data(filename):
    """Reads a maze from a text file and returns it as a list of lists."""
    data = []
    with open(filename, "r") as f:
        for line in f:
            strip_line = line.strip()
            split_line = strip_line.split(" ")
            total = split_line[0]
            split_line[0] = total.strip(":")
            inted_list = []
            for element in split_line:
                inted_list.append(int(element))

            data.append(inted_list)
    return data
