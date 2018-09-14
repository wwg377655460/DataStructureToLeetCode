class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        res = []
        for i in range(len(nums)):
            if nums[i] != 0:
                res.append(nums[i])

        for i in range(len(nums)):
            if i < len(res):
                nums[i] = res[i]
            else:
                nums[i] = 0


solution = Solution()
nums = [0, 1, 0, 3, 12]
solution.moveZeroes(nums)
print(nums)
