class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # O(n)时间复杂度
        start = 0
        end = len(numbers) - 1 # numbers[start] and numbers[end]
        while start != end:
            all = numbers[start] + numbers[end]
            if target == all:
                return [start + 1, end + 1]
            elif target > all:
                start += 1
            else:
                end -= 1

        return [-1, -1]






solution = Solution()
nums = [2, 7, 11, 15]
target = 9
res = solution.twoSum(nums, target)
print(res)
