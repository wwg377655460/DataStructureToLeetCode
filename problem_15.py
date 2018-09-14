class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []

        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            if i == 0 or nums[i] > nums[i-1]:
                j = i + 1
                k = len(nums) - 1  # [j...k]
                while j < k:
                    sum = nums[i] + nums[j] + nums[k]
                    if sum == 0:
                        res.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1
                    elif sum < 0:
                        j += 1
                    else:
                        k -= 1

        return res


solution = Solution()
nums = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
res = solution.threeSum(nums)
print(res)
