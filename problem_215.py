class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return Solution._findKthLargest(nums, 0, len(nums) - 1, len(nums) - k)


    @classmethod
    def _findKthLargest(cls, nums, start, end, k):
        res = Solution._parition(nums, start, end)
        if res > k:
            return Solution._findKthLargest(nums, start, res - 1, k)
        elif res < k:
            return Solution._findKthLargest(nums, res + 1, end, k)
        else:
            return nums[res]

    @classmethod
    def _parition(cls, nums, start, end):
        # [start+1...tip] < nums[start] and [tip+1...end] > nums[start]
        tip = start
        value = nums[start]
        for i in range(start + 1, end + 1):
            if nums[i] < value:
                nums[tip + 1], nums[i] = nums[i], nums[tip + 1]
                tip += 1

        nums[tip], nums[start] = nums[start], nums[tip]
        return tip


solution = Solution()
nums = [3,2,1,5,6,4]
k = 2
res = solution.findKthLargest(nums, len(nums) - k)
print(res)
