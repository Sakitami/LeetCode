#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# 最简单的方法是遍历ransomNote中的每个元素，
# 判断magazine中是否存在该元素，
# 若存在，则删除一个ransomNote中的元素
# 直到最后一个元素遍历结束返回True
# 若期间ransomNote不存在该元素，则返回False


# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        for i in ransomNote:
            if i in magazine:
                magazine.remove(i)
            else:
                return False
                
        return True


# @lc code=end

# test = Solution()
# result = test.canConstruct("aa","aab")
# print(result)