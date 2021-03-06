'''
给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:

输入: [1,2,3,4]
输出: [24,12,8,6]
说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
'''


'''
解题思路：

由于不能使用除号，所以必须只有乘号来计算。维护两个数组dp1和dp2，分别用来保存第i个位置之前所有数的乘积和第i个位置之后所有数的乘积。

代码（Python）：

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dp1 = [1]
        dp2 = [1]
        for i in range(len(nums)-1):
            dp1.append(dp1[i]*nums[i])
            dp2.append(dp2[i]*nums[-i-1])
        
        output = []
        for i in range(len(dp1)):
            output.append(dp1[i]*dp2[-i-1])
        return output
'''
