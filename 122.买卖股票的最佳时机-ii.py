#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# 贪心算法
# 若遇到上升趋势，则购买上升趋势左端点，从右端点卖出
# 遇到下降趋势则不做任何操作

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        purchased = 0
        for i,j in enumerate(prices):
            if i == len(prices)-1:
                if purchased:
                    profit += j
                return profit
            if j < prices[i+1] and not purchased:
                profit -= j
                purchased += 1
            elif j >= prices[i+1]:
                if purchased:
                    profit += j
                    purchased = 0
# test = Solution()
# print(f"result:{test.maxProfit([7,6,4,3,1])}")

# @lc code=end

