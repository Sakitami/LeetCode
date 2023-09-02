#
# @lc app=leetcode.cn id=2511 lang=python3
#
# [2511] 最多可以摧毁的敌人城堡数目
#
# 双指针
# 解法1：
# 定位第一个非0元素位置，并寻找下一个非0位置
# 若两个非0位置元素互为相反数（即-1和1），则记录中间0的个数
# 若两个非0位置元素相同，则更新左指针位置

# 解法2：
# 寻找所有我方军队位置
# 根据我方军队位置，依次向右或向左搜寻非0元素
# 若找到非0元素，则判断是否合法（即是否为相反数）
# 将合法的结果与记录的结果比对，若更大则更新结果


# @lc code=start
class Solution:
    def captureForts(self, forts: list[int]) -> int:
        i = 0  # 标记上一个不为0的位置
        n = len(forts)
        while i < n and forts[i] == 0: i += 1   # 找到首个不为0的位置
        res = 0
        for j in range(i + 1, n):
            if forts[j] != 0:
                if forts[j] == -forts[i]: res = max(res, j - i - 1)    # fort[j]和fort[i]的值互为相反数，更新距离
                i = j  # 只要fort[j]不为0，就更新i，即上一个不为0的位置发生了变化
        return res


        # 解法2
        # my_army = []
        # result = 0

        # # 收集我方军队的位置
        # for i,j in enumerate(forts):
        #     if j == 1:
        #         my_army.append(i)
        
        # for i in my_army:
        #     pointer = i-1
        #     des_l = 0
        #     while pointer >= 0:
        #         if forts[pointer] == 0:
        #             des_l += 1
        #         elif forts[pointer] == 1:
        #             break
        #         else:
        #             if des_l >= result:
        #                 result = des_l
        #             break
        #         pointer -= 1
        # for i in my_army:
        #     pointer = i+1
        #     des_r = 0
        #     while pointer <= len(forts)-1:
        #         if forts[pointer] == 0:
        #             des_r += 1
        #         elif forts[pointer] == 1:
        #             break
        #         else:
        #             if des_r >= result:
        #                 result = des_r
        #             break
        #         pointer += 1
        # return result

# test = Solution()
# result = test.captureForts([1,0,0,-1,0,0,0,0,1])
# print(f"result:{result}")


# @lc code=end

