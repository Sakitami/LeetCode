#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#


# 解法1：
# 二分查找
import bisect

# 解法2：
# Python作弊法
# 依次遍历数组中的元素，查找改元素右侧数组是否存在合法y（y = target - x）
# 若存在，则返回两下标位置

# @lc code=start
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        for i in range(n - 1):
            x = target - numbers[i]
            j = bisect.bisect_left(numbers, x, lo=i + 1)
            if j < n and numbers[j] == x:
                return [i + 1, j + 1]

        # # 解法2：
        # for i,j in enumerate(numbers):
        #     if j == target:
        #         return [i+1,i+numbers[i+1:].index(0)+2]
        #     if target -j in numbers[i+1:]:
        #         return [i+1,i+numbers[i+1:].index(target -j)+2]


test = Solution()
result = test.twoSum([2,7,11,15],9)
print(f"result:{result}")



# @lc code=end

