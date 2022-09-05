# # class Solution:
# def twoSum(nums, target):
#     # base case
#     first_number = nums[0]
#     current_minimum_index = 0
#     other_number = target - first_number
#     # nums.remove(current_minimum)
#     i = 1
#     j = 0
#     while other_number not in nums:
#         # nums.remove(current_minimum)
#         current_minimum = min(nums)
#         current_minimum_index = nums.index(current_minimum)

#         other_number = target - current_minimum
#         nums.remove(current_minimum)
#         j += 1
#     index_other_num = nums.index(other_number) + j
#     # if current_minimum == current_minimum_index:
#     #     nums.remove(current_minimum)
#     #     index_other_num = nums.index(other_number) + 1
#     return current_minimum_index + i, index_other_num + i

#
def twoSum(nums, target):
    nums_index_value = {}
    for i, value in enumerate(nums):
        if target - value in nums_index_value.keys():
            return i, nums_index_value[target - value]
        else:
            nums_index_value[value] = i


# def twoSum(self, nums: List[int], target: int) -> List[int]:
#     hashmap = {}
#     for i in range(len(nums)):
#         hashmap[nums[i]] = i
#     for i in range(len(nums)):
#         complement = target - nums[i]
#         if complement in hashmap and hashmap[complement] != i:
#             return [i, hashmap[complement]]

print(twoSum([3, 2, 3], 6))
