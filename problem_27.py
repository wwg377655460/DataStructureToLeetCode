class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        end = len(nums)
        index = 0 # [index...end]
        while index < end:
            if nums[index] == val:
                nums[index], nums[end-1] = nums[end-1], nums[index]
                end -= 1
            else:
                index += 1

        return index

solution = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2
res = solution.removeElement(nums, val)
print(res)
print(nums)
