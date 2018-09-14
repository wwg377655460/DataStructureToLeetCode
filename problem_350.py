class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        new_nums = dict()
        for i in range(len(nums1)):
            if nums1[i] in new_nums:
                new_nums[nums1[i]] += 1
            else:
                new_nums[nums1[i]] = 1

        res = []
        for i in range(len(nums2)):
            if nums2[i] in new_nums and new_nums[nums2[i]] != 0:
                res.append(nums2[i])
                new_nums[nums2[i]] -= 1

        return res

solution = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
res = solution.intersect(nums1, nums2)
print(res)
