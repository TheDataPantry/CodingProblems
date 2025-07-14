from typing import List

with open('data.txt', 'r') as f:
    lines = f.read().strip().split('\n')

def list_of_lists(data: List) -> List:
    updated_data = []
    for line in data:
        row = []
        for num in line.split():
            row.append(int(num))
        updated_data.append(row)
    return updated_data

## Part 1 Solution
"""
Create filters per report to assess if the entire report is increasing/decreasing (monontic) and then evaluate if differences are within 1 and 3.
"""

def monotonic_window(data: List) -> int:
    valid_count = 0

    for report in data:
        diffs = [abs(report[i+1] - report[i]) for i in range(len(report) - 1)]
        is_monotonic = all(report[i] < report[i+1] for i in range(len(report) - 1)) or all(report[i] > report[i+1] for i in range(len(report) - 1))
        valid_diffs = all(1 <= d <= 3 for d in diffs)

        if is_monotonic and valid_diffs:
            valid_count += 1
    return valid_count

## Part 2 Solution
"""
Need to adjust function from part 1 to assess on an individual row level rather than aggregate data set. 
This in turn is used to evaluate the almost safe cases by running the evaluation iteratively by removing one level from the report. 
"""

def is_safe(levels):
    diffs = [b - a for a, b in zip(levels, levels[1:])]
    # Check monotonicity & range constraints
    return (all(d > 0 for d in diffs) or all(d < 0 for d in diffs)) and all(1 <= abs(d) <= 3 for d in diffs)

def almost_safe(data):
    valid_count = 0

    for report in data:
        if is_safe(report):
            valid_count += 1
        else:
            # Try removing one level anywhere
            for i in range(len(report)):
                if is_safe(report[:i] + report[i+1:]):
                    valid_count += 1
                    break
    return valid_count