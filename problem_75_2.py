class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 三路快速排序
        zero_index = -1  # [0...zero_index] == 0
        two_index = len(nums)  # [two_index...len(nums)] == 2

        index = 0
        while index < two_index:
            if nums[index] == 0:
                zero_index += 1
                nums[index], nums[zero_index] = nums[zero_index], nums[index]
                index += 1
            elif nums[index] == 1:
                index += 1
            else:
                two_index -= 1
                nums[index], nums[two_index] = nums[two_index], nums[index]


solution = Solution()
nums = [2, 0, 2, 1, 1, 0]
solution.sortColors(nums)
print(nums)
