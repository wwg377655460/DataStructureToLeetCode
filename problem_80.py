class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        index = 0
        count = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                count += 1
                if count > 2:
                    continue
            else:
                count = 1

            nums[index] = nums[i]
            index += 1

        return index


solution = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
res = solution.removeDuplicates(nums)
print(res)
print(nums)
