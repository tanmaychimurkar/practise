from collections import defaultdict


class Solution:
    def longestPalindrome(self, s):

        letter_count = defaultdict(int)

        for character in s:
            letter_count[character] += 1

        longest_palindrome = 0
        odd_counts = 0
        odd_sum = 0
        for key, count in letter_count.items():
            if count % 2 == 0:
                longest_palindrome += count
            else:
                odd_sum += count
                odd_counts += 1

        if odd_counts > 0:
            return (
                longest_palindrome + odd_sum - (odd_counts - 1)
            )  # remove all odd occurences except one

        return longest_palindrome


_obj = Solution()
_obj.longestPalindrome("aabbbccc")
