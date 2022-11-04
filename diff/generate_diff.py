import json


def generate_diff(path1, path2):
    with open(path1) as f:
        file1 = json.load(f)
    with open(path2) as f:
        file2 = json.load(f)

    string = "{\n"

    for key in sorted(file1):

        if key not in file2:
            not_in = f"  - {key}: {file1[key]}"
            string += not_in + "\n"

        elif key in file2 and file1[key] == file2[key]:
            equal = f"    {key}: {file1[key]}"
            file2.pop(key)
            string += equal + "\n"

        elif key in file2 and file1[key] != file2[key]:
            not_equal1 = f"  - {key}: {file1[key]}"
            not_equal2 = f"  + {key}: {file2[key]}"
            file2.pop(key)
            string += not_equal1 + "\n"
            string += not_equal2 + "\n"

    for key in sorted(file2):
        end = f"  + {key}: {file2[key]}"
        string += end + "\n"
    string += "}"
    return string
