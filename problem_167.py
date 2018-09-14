class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)):
            now_target = target - numbers[i]
            if now_target < 0:
                return [-1, -1]
            index = Solution.binary_search(numbers, i + 1, now_target)
            if index != -1:
                return [i + 1, index + 1]

    @classmethod
    def binary_search(self, numbers, start, target):
        l = start
        r = len(numbers) - 1  # [l...r]
        while l <= r:
            mid = (l + r) // 2
            if numbers[mid] == target:
                return mid
            elif numbers[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1


solution = Solution()
nums = [2, 7, 11, 15]
target = 9
res = solution.twoSum(nums, target)
print(res)
