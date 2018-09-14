class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        index_1 = m - 1
        index_2 = n - 1
        index = m + n - 1
        while index_1 >= 0 and index_2 >= 0:
            if nums1[index_1] > nums2[index_2]:
                nums1[index] = nums1[index_1]
                index_1 -= 1
            else:
                nums1[index] = nums2[index_2]
                index_2 -= 1
            index -= 1

        if index_2 >= 0:
            for i in range(index + 1):
                nums1[i] = nums2[i]



solution = Solution()
nums1 = [0]
m = 0
nums2 = [1]
n = 1

solution.merge(nums1, m, nums2, n)
print(nums1)
