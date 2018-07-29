def hex_to_number(x):
    values = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
              "8": 8, "9": 9, "a": 10, "b": 11, "c": 12, "d": 13, "e": 14,
              "f": 15}

    return values[x]


def number_to_hex(x):
    values = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7",
              8: "8", 9: "9", 10: "a", 11: "b", 12: "c", 13: "d", 14: "e",
              15: "f"}

    return values[x]


def trim_hex(x):
    """
    Удаление ненужных нулей слева.
    """
    h = x[0]
    i = 0

    while h == "0" and i < len(x):
        i += 1
        h = x[i]

    return x[i:]


def shift_left(x, n):
    return [0] * n + x[:-n]


def resize(arr, new_length):
    if len(arr) < new_length:
        return arr + [0] * (new_length - len(arr))
    else:
        return arr
