class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        index = 0
        for i in range(len(nums)):
            if nums[i] != 0 and index != i:
                nums[index], nums[i] = nums[i], nums[index]
                index += 1


solution = Solution()
nums = [0, 1, 0, 3, 12]
solution.moveZeroes(nums)
print(nums)
