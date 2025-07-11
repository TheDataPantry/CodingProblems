from typing import List

## Part 1

def quick_sort(arr: List[int]) -> List[int]:
    """
    Recursively evaluate each value in an array to see if its greater or less than the previous value assessed starting with the first value.
    """

    if len(arr) <= 1:
        return arr 
    first_value = arr[0]
    values_less = [x for x in arr[1:] if x <= first_value]
    values_greater = [x for x in arr[1:] if x > first_value]
    return quick_sort(values_less) + [first_value] + quick_sort(values_greater)

#Part 1 solution
def compare_lists(L1: List[int], L2: List[int]) -> int:
    return sum(abs(a-b) for a, b in zip(L1, L2))

## Part 2

def occurrence_count(L1: List[int], L2: List[int]) -> int:
    """
    Go through 2nd list to count occurrence of values in 1st list and then multiply the values for end result
    """
    result = []
    for i in range(len(L1)):
        value = L1[i]
        count = 0
        for j in range(len(L2)):
            if L2[j] == value:
                count += 1
        result.append((value, count))

    return sum(a*b for a, b in result)