class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []

        def dfs(start, remain, path):
            if remain == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                if candidates[i] > remain:
                    break

                path.append(candidates[i])
                dfs(i, remain - candidates[i], path)
                path.pop()

        dfs(0, target, [])
        return result