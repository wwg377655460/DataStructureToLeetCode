class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        map_index = {}
        res = 0
        for i in range(len(C)):
            for j in range(len(D)):
                sum = C[i] + D[j]
                if sum in map_index:
                    map_index[sum] += 1
                else:
                    map_index[sum] = 1

        for i in range(len(A)):
            for j in range(len(B)):
                rest = - (A[i] + B[j])
                if rest in map_index:
                    res += map_index[rest]

        return res

solution = Solution()
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

res = solution.fourSumCount(A, B, C, D)
print(res)
