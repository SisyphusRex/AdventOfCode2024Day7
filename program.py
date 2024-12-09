def main(*args):
    """main method"""

    data = get_data("test_data.txt")

    data_dict_list = make_list_of_dict(data)

    list_of_values_one = data_dict_list[1].get("elements")
    value_dict = evaluate_list_of_values(list_of_values_one)


def evaluate_list_of_values(list_of_values) -> {}:
    length_of_list = len(list_of_values)
    if length_of_list == 2:
        plus_plus = list_of_values[0] + list_of_values[1]
        plus_multiply = list_of_values[0] * list_of_values[1]
        multiply_multiply = list_of_values[0] * list_of_values[1]
        multiply_plus = list_of_values[0] + list_of_values[1]

        return {
            "plus_plus": plus_plus,
            "plus_multiply": plus_multiply,
            "multiply_multiply": multiply_multiply,
            "multiply_plus": multiply_plus,
        }
    new_list = list_of_values[0 : length_of_list - 1]
    my_dict = evaluate_list_of_values(new_list)
    my_dict["plus_plus"] = my_dict["plus_plus"] + new_list[length_of_list - 2]
    multiply = multiply * new_list[length_of_list - 2]
    return plus_plus, plus_multiply, multiply_multiply, multiply_plus


def make_list_of_dict(data):
    data_dict_list = []

    for element in data:
        data_dict = {"total": None, "elements": [], "spaces": None}
        for index, number in enumerate(element):
            if index == 0:
                data_dict["total"] = number
            else:
                data_dict["elements"].append(number)
        data_dict["spaces"] = len(data_dict["elements"]) - 1
        data_dict_list.append(data_dict)
    return data_dict_list


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
