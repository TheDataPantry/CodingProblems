"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
"""

def removeElement(nums: List[int], val: int) -> int:
    x = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[x] = nums[i]
            x += 1
    print(x, nums[:x])
    return x 