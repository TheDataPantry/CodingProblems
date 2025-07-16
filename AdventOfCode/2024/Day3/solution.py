import re 


def mul_search(data):
    """
    Goes through entire string to identify the string mul(xxx, xxx) where xxx is a number. 
    It then converts the values within the parenthesis to integers and adds the products of these values to a running total
    """
    match = "(mul\\(\\d+,\\d+\\))"
    total = 0
    for seq in re.findall(match, data):
        nums = seq[seq.index("(")+1:seq.index(")")].split(',')
        total += int(nums[0]) * int(nums[1])
    return total

def do_dont_flag(data):
    """
    Goes through entire string to find one of three matches. do(), don't(), and mul(). 
    Set a flag as boolean to determine whether to add to running total based on what it has seen before: do or don't
    if boolean is True, add to running total
    """
    total = 0
    do_sum = True
    for x in re.finditer(r'do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\)', data):
        match x[0]:
            case 'do()':
                do_sum = True
            case 'don\'t()':
                do_sum = False
            case _:
                if do_sum:
                    total += int(x[1]) * int(x[2])