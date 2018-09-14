class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last = -1
        index = 0

        if len(nums) == 0:
            return 0

        for i in range(len(nums)):
            if index + 1 == len(nums):
                break
            if nums[i] != last and i != index:
                nums[i], nums[index+1] = nums[index+1], nums[i]
                index += 1
            last = nums[index]

        return index + 1


solution = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
res = solution.removeDuplicates(nums)
print(res)
print(nums)
