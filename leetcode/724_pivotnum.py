class Solution:
    def pivotIndex(self, nums):
        lsum = 0

        ####################################################
        # this version is correct, but has way too high runtime because we are calculating sum of array in every loop

        # for i in range(0, len(nums)):
        #     if lsum == sum(nums[i+1:]):
        #         return i
        #     lsum += nums[i]
        # return -1

        ####################################################

        # better to calculate it only once and remove numbers from it, since the commented code has high runtime
        rsum = sum(nums)

        for index, number in enumerate(nums):
            if lsum == (rsum - nums[index] - lsum):
                return index
            lsum += nums[index]
        return -1


_object = Solution()
_object.pivotIndex([1, 7, 3, 6, 5, 6])
