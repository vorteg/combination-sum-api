from typing import List


class Solution:
    @classmethod
    def combination_sum(
        cls, tolerance: float, candidates: List[float], target: float
    ) -> List[List[float]]:
        res = []
        tolerance = tolerance / 100
        tolerance_calc = target * tolerance

        def dfs(i: float, cur: List, total: float):
            dif = target - total
            if dif < 0:
                return
            if dif <= tolerance_calc and total != 0:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
