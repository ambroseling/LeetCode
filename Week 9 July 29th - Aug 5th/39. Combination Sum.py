class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        # i is for which candidate we can choose
        # cur is the current combination
        # total is the total sum of cur 
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return 
            
            # decision one: we aren't adding the candidate, and continuing.
            dfs(i + 1, cur, total)
            # decision two: we include the new candidate
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            # backtracking step
            cur.pop()

        dfs(0, [], 0)
        return res
