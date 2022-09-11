import bisect


def isBadVersion(version):
    if version > 3:
        return True
    return False


"""
The below implementation uses the __getitem__, which is a bound method. Once this method is set, it is accessible 
everywhere in the self object as well. It is a bound method, and is bound as soon as the object is instantiated. 
"""


class Solution:
    def __getitem__(self, x):
        return isBadVersion(x)

    def firstBadVersion(self, n: int) -> int:

        return bisect.bisect_left(self, True, 1, n)


_obj = Solution()
version = _obj.firstBadVersion(8)
print(version)
