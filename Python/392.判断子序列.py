#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        index = 0
        for i,j in enumerate(s):
            print(t[index:])
            if j in t[index:] and index+t[index:].index(j)+1>=index:
                index += t[index:].index(j)+1
                if i == len(s)-1:
                    return True
                continue
            return False


# test = Solution()
# result = test.isSubsequence("ab","baab")
# print(result)

# @lc code=end

