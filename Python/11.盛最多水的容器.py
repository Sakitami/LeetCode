#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: list[int]) -> int:
        p_l = 0
        p_r = len(height)-1
        result = 0
        while p_l != p_r:
            if height[p_l] <= height[p_r]:
                water = height[p_l]*(p_r-p_l)
                p_l += 1
            else:
                water = height[p_r]*(p_r-p_l)
                p_r -= 1
            if result <= water:
                result = water
            
        return result

# test = Solution()
# result = test.maxArea([1,8,6,2,5,4,8,3,7])
# print(f"result:{result}")
# @lc code=end

