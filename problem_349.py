class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        new_nums = set(nums1)
        res = set()
        for i in range(len(nums2)):
            if nums2[i] in new_nums:
                res.add(nums2[i])

        return [i for i in res]

solution = Solution()
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
res = solution.intersection(nums1, nums2)
print(res)
