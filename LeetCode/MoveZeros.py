from typing import List

def brute_force(nums: List) -> List:
    for i in range(0, len(nums)):
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.extend([0])

def moveZeroes(self, nums: List[int]) -> None:
        """
        create a running index to compare to length of number list. For all values not 0 move to the front and increase index. For however shorter index value is compared to length of list, insert 0s.
        """
        insert_pos = 0

        # Move all non-zero elements to the front
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1

        # Fill the rest with zeros
        for i in range(insert_pos, len(nums)):
            nums[i] = 0