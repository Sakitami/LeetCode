#
# @lc app=leetcode.cn id=1921 lang=python3
#
# [1921] 消灭怪物的最大数量
#

# @lc code=start
class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        times = sorted((d - 1) // s for d, s in zip(dist, speed))
        for i, t in enumerate(times):
            if t < i:
                return i
        return len(times)



# test = Solution()
# result = test.eliminateMaximum([46,33,44,42,46,36,7,36,31,47,38,42,43,48,48,25,28,44,49,47,29,32,30,6,42,9,39,48,22,26,50,34,40,22,10,45,7,43,24,18,40,44,17,39,36]
# ,[1,2,1,3,1,1,1,1,1,1,1,1,1,1,7,1,1,3,2,2,2,1,2,1,1,1,1,1,1,1,1,6,1,1,1,8,1,1,1,3,6,1,3,1,1])
# print(f"result:{result}")
# @lc code=end

