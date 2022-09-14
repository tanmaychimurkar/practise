class Solution:
    def isAnagram(self, s, t):

        # todo: we can check if the length of the two strings are different or not. The next step is to created a sorted
        #  list from both the strings and compare them once. For this, we have to use the inbuilt function though, so
        #   not sure how much value this is
        if len(s) != len(t):
            return False
        #
        # string1 = sorted(s)
        # string2 = sorted(t)
        #
        # if string1 == string2:
        #     return True
        #
        # return False

        # todo: one more way it to iterate over all possible alphabets of English and compare their counts to the counts
        #  of each alphabet from the two strings
        # alphabets = 'abcdefghijklmnopqrstuvwxyz'
        #
        # for alphabet in alphabets:
        #     if s.count(alphabet) != t.count(alphabet):
        #         return False
        #
        # return True

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # this is the default way to set a value to 0 if key does not exist
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for key in countS:
            if countS[key] != countT.get(key, 0):
                return False
        return True
