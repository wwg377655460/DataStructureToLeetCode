class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_map = dict({})
        for i in range(len(nums)):
            if target - nums[i] in index_map:
                return [index_map[target - nums[i]], i]
            index_map[nums[i]] = i

solution = Solution()
nums = [2, 7, 11, 15]
target = 9
res = solution.twoSum(nums, target)
print(res)