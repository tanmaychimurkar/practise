class Solution:
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


_object = Solution()
total = _object

_object.runningSum([3, 1, 2, 10, 1])
