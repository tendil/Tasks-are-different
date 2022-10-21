"""
Given: Sequence of numbers
Task:
    Sum numbers from the sequence
"""
from typing import Iterable

def sum_numbers(numbers: Iterable[int]) -> int:
    sum_of_numbers = 0

    for number in numbers:
        sum_of_numbers += number

    return sum_of_numbers

def sum_numbers_rec(numbers: Iterable[int]) -> int:
    if len(numbers) == 0:
        return 0

    # if not numbers:
    #     return 0

    last_number_sum = numbers[0]
    rest_numbers = numbers[:]
    rest_numbers_sum = sum_numbers_rec(rest_numbers)
    return last_number_sum + rest_numbers_sum

# print(sum_numbers_rec([]))
"""
1 1 2 2 3 3

1 1 2 2 3 + 3 = (1 1 2 2 + 3) + 3 = ((1 1 2 + 2) + 3) + 3 = (((1 1 + 2) + 2) + 3) + 3 = (((((1 + 1) + 2) + 2) + 3) + 3

(((((1 + 1) + 2) + 2) + 3) + 3 = (((((2) +2) +2) +3) +3) = (((4) +2) +3) +3 = ((6) +3) +3 = (9) +3 = 12
"""
print(sum_numbers_rec([1, 1, 2, 2, 3, 3, 4]))
print(sum_numbers_rec((4, 6, 10)))
print(sum_numbers_rec([]))
