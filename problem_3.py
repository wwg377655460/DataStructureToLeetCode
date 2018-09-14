class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        word_list = [0] * 256
        i = 0
        j = -1  # [i...j]
        res = 0
        while i < len(s):
            if j + 1 < len(s) and word_list[ord(s[j + 1])] == 0:
                j += 1
                word_list[ord(s[j])] += 1
            else:
                word_list[ord(s[i])] -= 1
                i += 1

            if res < j - i + 1:
                res = j - i + 1

        return res


solution = Solution()
s = "dvdf"
res = solution.lengthOfLongestSubstring(s)
print(res)
