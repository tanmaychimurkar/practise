import collections


class Solution:
    def groupAnagrams(self, strs):
        # todo: this solution maintains a dictionary of the word pairs matched, and keeps track of which words were
        #  visited by the helper function that compares two anagrams. Brute force method which times out, because of
        #  O(n^2)
        # anagram_dict = {}
        # visited_strings = []
        #
        # def helper(match_word, word_index, array_subset):
        #     match_word_sorted = sorted(match_word)
        #     indexes = []
        #     for index, word in enumerate(array_subset):
        #         if len(word) != len(match_word):
        #             pass
        #         elif sorted(word) == match_word_sorted:
        #             indexes.append(word)
        #     indexes.append(match_word)
        #     return indexes
        #
        # for index, word in enumerate(strs):
        #     if word not in visited_strings:
        #         anagram_dict[word] = helper(word, index, strs[index+1:])
        #         visited_strings.extend(anagram_dict[word])
        #
        # return list(anagram_dict.values())

        # todo: main intuition is that two strings are anagrams if their sorted order or character counts are the same
        #  we can use either one of these as a key for our dictionary and then match words that match that pattern

        # this is the method to create a dictionary with the values being the mentioned datatype
        anagram_dict = collections.defaultdict(list)

        for word in strs:
            anagram_dict[tuple(sorted(word))].append(word)

        return anagram_dict.values()


_obj = Solution()
_obj.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
