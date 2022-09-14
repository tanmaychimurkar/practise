class Solution:
    def twoSum(self, nums, target):

        # todo: brute force is straightforward, iterate over the array once and check which of the numbers make a pair
        #  but we need to keep track of indexes

        # doesn't work for duplicate elements at different indexes
        # for number in nums:
        #     for second_number in nums:
        #         if number != second_number and (number + second_number) == target:
        #             return nums.index(number), nums.index(second_number)

        # timeout limit reached, time complexity o(n^2)
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if (nums[i] + nums[j]) == target and i != j:
        #             return i, j

        # todo: use a dictionary to maintain indexes of all the elements as we pass through the array once, if looping
        #  through the array only once, maintain a hashmap to keep track of indexes of visited elements

        element_indexes = {}

        for index, number in enumerate(nums):
            if (target - number) in element_indexes:
                return [index, element_indexes[target - number]]
            element_indexes[number] = index





