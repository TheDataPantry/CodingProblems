from typing import List
def xmas_counter(data:List) -> int:
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