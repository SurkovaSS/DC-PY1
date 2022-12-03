import json

INPUT_FILE = "input.csv"
INPUT_FILE_1 = "input_1.csv"

def csv_to_list_dict(filename, delimiter=",", new_line="\n") -> list[dict]:
    with open(filename, "rt", encoding='utf-8') as file:
        data = [line.rstrip() for line in list(file)]
        data = [value.rsplit(delimiter) for value in data]
        headers = data.pop(0)
        list_of_dicts = []
        for line in data:
            temp_dict = {}
            for i in range(len(line)):
                temp_dict[headers[i]] = line[i]
            list_of_dicts.append(temp_dict)
        return list_of_dicts


# TODO реализовать конвертер из csv в json


print(json.dumps(csv_to_list_dict(INPUT_FILE_1), indent=4))
