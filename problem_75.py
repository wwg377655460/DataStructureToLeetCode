class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 计数排序
        colors = [0, 0, 0]
        for i in range(len(nums)):
            assert 0 <= nums[i] <= 2
            colors[nums[i]] += 1

        index = 0
        num_real = 0
        while num_real <= 2:
            for i in range(colors[num_real]):
                nums[index] = num_real
                index += 1
            num_real += 1

solution = Solution()
nums = [0, 1, 0, 2, 1]
solution.sortColors(nums)
print(nums)
