class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        left = ["{", "[", "("]
        right = ["}", "]", ")"]
        for i in range(len(s)):
            if s[i] in left:
                stack.append(s[i])
            elif s[i] in right:
                if len(stack) == 0 or left.index(stack.pop()) != right.index(s[i]):
                    return False
            else:
                exit(-1)

        if len(stack) != 0:
            return False

        return True



solution = Solution()
s = "]"
res = solution.isValid(s)
print(res)
