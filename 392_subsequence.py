class Solution:
    def isSubsequence(self, s, t):
        if len(s) > len(t):
            return False

        if len(s) == len(t):
            return s == t
        
        if len(s) == 0:
            return True

        start_index = 0
        for character in t:
            if character == s[start_index]:
                start_index += 1
                if start_index == len(s):
                    return True

        return False

_object = Solution()
_object.isSubsequence(s='ace', t='abcde')
