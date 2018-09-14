class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s) - 1  # [l...r]
        while l <= r:
            while not s[l].isalnum():
                l += 1
                if l > r:
                    break

            while not s[r].isalnum():
                r -= 1
                if l > r:
                    break

            if l > r:
                break

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True


solution = Solution()
s = "0P"
res = solution.isPalindrome(s)
print(res)
