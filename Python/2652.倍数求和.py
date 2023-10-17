#
# @lc app=leetcode.cn id=2652 lang=python3
#
# [2652] 倍数求和
#
#
# 简单题，仅需判断数字为1的特殊条件即可
# 其余数字使用条件判断即可求出 
#

# @lc code=start
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        sum = 0
        if n < 3:
            return 0
        for i in range(1,n+1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                sum += i
        return sum
# @lc code=end
