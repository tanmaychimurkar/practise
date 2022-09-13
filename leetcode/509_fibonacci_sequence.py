import functools


class Solution:

    @functools.cache
    def fib(self, n):

        mem = {}
        if n == 0:
            return 0
        if n == 1:
            return 1

        # use caching to avoid recomputing fibonacci sequence everytime

        if n not in mem:
            mem[n] = self.fib(n - 1) + self.fib(n - 2)
        return mem[n]


_obj = Solution()
_obj.fib(6)
