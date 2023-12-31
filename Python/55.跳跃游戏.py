#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# 尽可能到达最远位置（贪心）。 如果能到达某个位置，那一定能到达它前面的所有位置。

# 方法：
# 初始化最远位置为 0，然后遍历数组，如果当前位置能到达，并且当前位置+跳数>最远位置，就更新最远位置。最后比较最远位置和数组长度。

# 时间复杂度 O(n)，空间复杂度 O(1)。。

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_i = 0       #初始化当前能到达最远的位置
        for i, jump in enumerate(nums):   #i为当前位置，jump是当前位置的跳数
            if max_i>=i and i+jump>max_i:  #如果当前位置能到达，并且当前位置+跳数>最远位置  
                max_i = i+jump  #更新最远能到达位置
        return max_i>=i

# @lc code=end

