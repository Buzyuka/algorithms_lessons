# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Решение усложненное - повторяет шаги как бы решал человек в столбик.

from collections import namedtuple, defaultdict, deque
from hex_helpers import *


a, b = input("Введите 2 числа в шестнадцеричном виде (через запятую): ").lower().split(",")

a = list(a)
b = list(b)

Register = namedtuple("Register", "value, accumulator")
Value = namedtuple("Value", "name, number")
zero = Value("0", 0)


def create_register(x):
    return Register(Value(x[1], hex_to_number(x[1])), 0)


row1 = list(map(lambda x: (len(a)-x[0]-1, create_register(x)), enumerate(a)))
row2 = list(map(lambda x: (len(b)-x[0]-1, create_register(x)), enumerate(b)))


def sum_(a, b):
    registers_len = max(len(a), len(b))

    accumulators = [0] * (registers_len + 1)
    values = [0] * (registers_len + 1)

    r1 = defaultdict(lambda: Register(zero, 0), a)
    r2 = defaultdict(lambda: Register(zero, 0), b)

    for i in range(registers_len):
        a = r1[i]
        b = r2[i]

        values[i] = a.value.number + b.value.number + accumulators[i]

        if values[i] > 15:
            accumulators[i+1] += 1
            values[i] -= 16

    values[-1] = accumulators[-1]

    hex_ = list(map(number_to_hex, reversed(values)))
    return trim_hex(hex_)


def _mul_hex_with_register(hex_, register):
    registers_len = max(len(a), len(b))

    accumulators = [0] * (registers_len * 3 + 1)
    values = [0] * (registers_len * 3 + 1)

    def accumulate(idx):
        while values[idx] > 15:
            accumulators[idx + 1] += 1
            values[idx] -= 16

    for j in range(len(hex_)):
        a_ = register
        b_ = hex_[j]

        values[j] = (a_.value.number * b_.value.number) + values[j] + accumulators[j]
        accumulators[j] = 0
        accumulate(j)

    for j in [3, 4, 5]:
        values[j] += accumulators[j]
        accumulators[j] = 0

    return values


def _sum_values(r1, r2):
    registers_len = len(r1)

    r1 = resize(r1, registers_len)
    r2 = resize(r2, registers_len)

    accumulators = [0] * (registers_len + 1)
    values = [0] * (registers_len + 1)

    for i in range(registers_len - 1):
        a = r1[i]
        b = r2[i]

        values[i] = a + b + accumulators[i]

        if values[i] > 15:
            accumulators[i + 1] += 1
            values[i] -= 16

    values[-1] = accumulators[-1]
    return values


def mul(a, b):
    if len(a) > len(b):
        a, b = b, a

    r1 = defaultdict(lambda: Register(zero, 0), a)
    r2 = defaultdict(lambda: Register(zero, 0), b)

    hexes = deque()

    for i in range(len(a)):
        h = _mul_hex_with_register(r2, r1[i])
        hexes.append(h)

    last = hexes.popleft()
    shifts = 1

    while len(hexes) > 0:
        a = last
        b = shift_left(hexes.popleft(), shifts)
        last = _sum_values(a, b)
        shifts += 1

    hex_ = list(map(number_to_hex, reversed(last)))
    return trim_hex(hex_)


print(sum_(row1, row2))
print(mul(row1, row2))
