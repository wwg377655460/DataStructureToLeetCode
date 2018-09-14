class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # 滑动窗口
        i = 0
        j = 0 # [i...j)
        all = 0
        min_length = len(nums) + 1
        while j <= len(nums):
            while all >= s:
                min_length = j - i if j - i < min_length else min_length
                all -= nums[i]
                i += 1

            if j >= len(nums):
                break
            all += nums[j]
            j += 1

        if min_length == len(nums) + 1:
            return 0

        return min_length

solution = Solution()
nums = [2, 3, 1, 2, 4, 3]
s = 7
res = solution.minSubArrayLen(s, nums)
print(res)
