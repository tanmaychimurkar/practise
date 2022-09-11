class Solution:
    @staticmethod
    def maxProfit(prices):
        # inefficient solution, memory limit exceeded
        # price_dict = {}
        # max_return = []
        # for index, value in enumerate(prices):
        #     price_dict[value] = prices[index + 1 :]
        #     try:
        #         if max(price_dict[value]) > value:
        #             max_return.append(max(price_dict[value]) - value)
        #     except:
        #         max_return.append(0)
        #
        # # if len(max_return) > 0:
        # #     return max(max_return)
        # return max(max_return)A

        # also inefficient, since I am storing all the returns from combinations
        # returns = []
        # for index, value in enumerate(prices):
        #     if max(prices[index:]) > value:
        #         returns.append(max(prices[index:]) - value)
        #
        # if len(returns) > 0:
        #     return max(returns)
        # return 0

        buy_min = prices[0]
        max_return = 0

        for price in prices[1:]:
            if price <= buy_min:
                buy_min = price
            elif price - buy_min > max_return:
                max_return = price - buy_min
        return max_return


obj = Solution.maxProfit([2, 4, 1])
print(obj)
