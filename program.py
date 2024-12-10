def main(*args):
    """main method"""

    data = get_data("data.txt")

    data_dict_list = make_list_of_dict(data)
    good_lines = []

    list_of_values_one = data_dict_list[8].get("elements")
    possible_values = evaluate_list_of_values(list_of_values_one)

    for index, dictionary in enumerate(data_dict_list):
        list_of_values = dictionary.get("elements")
        possible_values = evaluate_list_of_values(list_of_values)
        equation_total = dictionary.get("total")
        if equation_total in possible_values:
            good_lines.append(dictionary)

    total = 0
    for line in good_lines:
        total += line.get("total")

    print(total)


def evaluate_list_of_values(list_of_values) -> list:
    length_of_list = len(list_of_values)
    possible_outcomes = []
    if length_of_list == 2:
        plus = list_of_values[0] + list_of_values[1]
        multiply = list_of_values[0] * list_of_values[1]
        possible_outcomes.append(plus)
        possible_outcomes.append(multiply)
        return possible_outcomes
    new_list_of_values = list_of_values[0 : length_of_list - 1]
    final_element = list_of_values[length_of_list - 1]
    previous_outcomes = evaluate_list_of_values(new_list_of_values)
    for element in previous_outcomes:
        plus = element + final_element
        multiply = element * final_element
        possible_outcomes.append(plus)
        possible_outcomes.append(multiply)
    return possible_outcomes


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
