import collections


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0 or t < 0:
            return False
        record = collections.OrderedDict()

        for i in range(0, len(nums)):
            key = nums[i] // max(1, t)
            for j in (record.get(key - 1), record.get(key), record.get(key + 1)):
                if j is not None and abs(nums[i] - j) <= t:
                    return True

            if len(record) == k:
                record.popitem(False)

            record[key] = nums[i]

        return False


solution = Solution()
nums = [2,2]
k = 3
t = 0
res = solution.containsNearbyAlmostDuplicate(nums, k, t)
print(res)
