# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Простое решение - просто переводим из одной системы счисления в другую и потом обратно.


def hex_to_dec(seq):
    values = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
              "8": 8, "9": 9, "a": 10, "b": 11, "c": 12, "d": 13, "e": 14,
              "f": 15}

    value = 0

    for i, x in enumerate(reversed(seq)):
        value += values[x] * (16 ** i)

    return value


def dec_to_hex(x):
    values = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7",
              8: "8", 9: "9", 10: "a", 11: "b", 12: "c", 13: "d", 14: "e",
              15: "f"}

    if x <= 1:
        return [values[x]]

    result = []
    quotient = x

    while True:
        remainder = quotient % 16

        if quotient == 0:
            return result

        quotient = quotient // 16
        result = [values[remainder]] + result


a, b = input("Введите 2 числа в шестнадцеричном виде (через запятую): ").lower().split(",")

a = hex_to_dec(a)
b = hex_to_dec(b)

print(dec_to_hex(a + b))
print(dec_to_hex(a * b))
