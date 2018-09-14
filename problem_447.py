
class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(points)):
            map_index = {}
            for j in range(len(points)):
                if i == j:
                    continue

                dis = Solution._distance(self, points[i], points[j])
                if dis in map_index:
                    map_index[dis] += 1
                else:
                    map_index[dis] = 1

            for key in map_index:
                if map_index[key] >= 2:
                    res += map_index[key] * (map_index[key] - 1)

        return res

    def _distance(self, point1, point2):
        return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2  # 可能出现整形越界的问题


solution = Solution()
points = [[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]]
res = solution.numberOfBoomerangs(points)
print(res)
