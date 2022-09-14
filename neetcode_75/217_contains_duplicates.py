import collections


class Solution:

    # todo: naive solution using collections.Counter, and then looping over the count_list to check if the count of each
    # recorded element is greater than 1 or not.
    # def containsDuplicate(self, nums):
    #     count_list = list(collections.Counter(nums).values())
    #
    #     for count_val in count_list:
    #         if count_val > 1:
    #             return True
    #     return False

    # todo: similar solution using a dictionary instead of a list, but performance is still bad
    # def containsDuplicate(self, nums):
    #     # count_dict = collections.OrderedDict(dict)
    #     count_dict = dict()
    #
    #     for number in nums:
    #         if number in count_dict:
    #             return True
    #         count_dict[number] = 1
    #
    #     return False

    # todo: the same could be done using a set as a hashmap instead of a dictionary
    def containsDuplicate(self,nums):
        count_list = set()
        for number in nums:
            if number in count_list:
                return True
            count_list.add(number)
        return False


_obj = Solution()
print(_obj.containsDuplicate([2, 14, 18, 22, 22]))
