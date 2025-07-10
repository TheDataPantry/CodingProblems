"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""

# Brute Force Method (O-squared time complexity)
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    #Combine lists
    idx = 0
    for i in range(m, m+n):
        # Add value to nums1:
        nums1[i] = nums2[idx]
        idx += 1
    #Starting from end, evaluate adjacent values
    idx = -1
    counter = 0
    while counter < len(nums1):
        for i, num in enumerate(nums1):
            if num > nums1[idx]:
                nums1[idx], nums1[i] = num, nums1[idx]
        idx -= 1
        counter += 1
    nums1.append(nums1.pop(0))
    return nums1

# Optimal Method (O(m+n) time complexity)
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Create identifiers of index values and lengths of given values. Then go through the second list and check index of first list to ensure you are within bounds. 
    As you go through the list, evaluate values from list 1 against list 2 and continue moving backwards from there. Key point is you are starting at the back of the list and moving to the beginning.
    Evaluate values at each index first and then go back a level.
    """
    a, b, write_index = m-1, n-1, m + n - 1

    while b >= 0:
        if a >= 0 and nums1[a] > nums2[b]:
            nums1[write_index] = nums1[a]
            a -= 1
        else:
            nums1[write_index] = nums2[b]
            b -= 1

        write_index -= 1
    return nums1

