class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0:
            return False
        record = set()
        for i in range(0, len(nums)):
            # [l...i)
            if i < k:
                if nums[i] in record:
                    return True
                record.add(nums[i])
            else:
                if nums[i] in record:
                    return True
                record.add(nums[i])
                record.remove(nums[i-k])

        return False


solution = Solution()
nums = [1,2,3,1,1,2,3]
k = 3
res = solution.containsNearbyDuplicate(nums, k)
print(res)
