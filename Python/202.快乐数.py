#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# 若

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        """
        累加num各个位的平方和
        """
        def new_number(n: int) -> int:
            new_num = 0
            while n > 0:
                digit = n % 10
                new_num += digit * digit
                n //= 10
            return new_num
        
        set_ = set()    # 记录循环过程中产生的数
        # 一旦新得到的数已经生成过，说明产生了循环，直接退出
        while n not in set_:
            if n == 1: return True  # 数字已经变为1，返回true
            set_.add(n)         # 记录生成的数
            n = new_number(n)   # 生成新的数
        return False
# @lc code=end

