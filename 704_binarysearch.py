def search(nums, target):

    low = 0
    high = len(nums) - 1
    while low <= high:

        middle = (high + low) // 2

        if target == nums[middle]:
            return middle
        elif target > nums[middle]:
            low += 1
        elif target < nums[middle]:
            high -= 1
    return -1


class Solution:
    pass


_obj = Solution()
valuefound = search([-1, 0, 3, 5, 9, 12], 2)
valuefound
