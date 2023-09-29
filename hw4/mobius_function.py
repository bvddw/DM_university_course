import math


def is_simple(p: int) -> bool:
    if p == 1:
        return False
    for i in range(2, int(math.sqrt(p)) + 1):
        if not p % i:
            return False
    return True


def simple_number_generator(n: int):
    start = 1
    while start <= n:
        if is_simple(start):
            yield start
        start += 1


def mobius_func(n: int) -> int:
    if n == 1:
        return 1
    count = 0
    for i in simple_number_generator(n):
        if not n % (i * i):
            return 0
        if not n % i:
            count += 1
    return (-1) ** count


expected_result = [
    (1, 1), (2, -1), (3, -1), (4, 0), (5, -1), (6, 1), (7, -1), (8, 0), (9, 0), (10, 1),
    (11, -1), (12, 0), (13, -1), (14, 1), (15, 1), (16, 0), (17, -1), (18, 0), (19, -1), (20, 0),
    (21, 1), (22, 1), (23, -1), (24, 0), (25, 0), (26, 1), (27, 0), (28, 0), (29, -1), (30, -1),
    (31, -1), (32, 0), (33, 1), (34, 1), (35, 1), (36, 0), (37, -1), (38, 1), (39, 1), (40, 0),
    (41, -1), (42, -1), (43, -1), (44, 0), (45, 0), (46, 1), (47, -1), (48, 0), (49, 0), (50, 0)
]
mobius_func_result = [(number, mobius_func(number)) for number in range(1, 51)]
assert expected_result == mobius_func_result
