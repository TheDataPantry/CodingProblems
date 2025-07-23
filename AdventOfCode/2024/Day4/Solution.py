from typing import List
def xmas_counter(data:List) -> int:
    """
    Go through each line to identify if xmas is formed in every direction
    """
    match = 'XMAS'
    counter = 0
    for line in range(len(data)):
        for char in range(len(data[line])):
            #forward
            if data[line][char:char+4] == match:
                counter += 1
            #backward
            if data[line][::-1][char: char+4] == match:
                counter += 1
            #downward
            if line <= len(data) - 4:
                if data[line][char] + data[line+1][char] + data[line+2][char] + data[line+3][char] == match:
                    counter += 1
            #upward
            if line >= 3:
                if data[line][char] + data[line-1][char] + data[line-2][char] + data[line-3][char] == match:
                    counter += 1
            #leftdown diagonal
            if line <= len(data) - 4 and char >= 3:
                if data[line][char] + data[line+1][char-1] + data[line+2][char-2] + data[line+3][char-3] == match:
                        counter += 1
            #leftup diagonal
            if line >= 3 and char >= 3:
                if data[line][char] + data[line-1][char-1] + data[line-2][char-2] + data[line-3][char-3] == match:
                    counter += 1
            #rightup diagonal
            if line >= 3 and char <= len(data[line]) - 4:
                if data[line][char] + data[line-1][char+1] + data[line-2][char+2] + data[line-3][char+3] == match:
                    counter += 1
            #rightdown diagonal
            if line <= len(data) - 4 and char <= len(data[line]) - 4:
                if data[line][char] + data[line+1][char+1] + data[line+2][char+2] + data[line+3][char+3] == match:
                    counter += 1
    return counter

def count_xmas_crosses(data):
    """
    Look for an A and then check to see if the diagonals form one of the combinations that forms mas
    """
    valid = {"MMSS", "MSSM", "SSMM", "SMMS"}
    H, W = len(data), len(data[0])
    count = 0

    for line in range(1, H-1):
      for char in range(1, W-1):
        if data[line][char] == 'A':
          # corners in leftup, rightup, rightdown, leftdown order
          corners = (
            data[line-1][char-1] +
            data[line-1][char+1] +
            data[line+1][char+1] +
            data[line+1][char-1]
          )
          if corners in valid:
            count += 1

    return count