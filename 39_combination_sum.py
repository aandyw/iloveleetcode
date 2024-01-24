class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        def dfs(candidate_i, tracked_candidates, total):
            if candidate_i == len(candidates) or total > target:
                return  # didn't find the target sum

            if total == target:
                combinations.append(tracked_candidates.copy())
                return

            tracked_candidates.append(candidates[candidate_i])
            dfs(candidate_i, tracked_candidates, total + candidates[candidate_i])
            tracked_candidates.pop()
            dfs(candidate_i + 1, tracked_candidates, total)

        dfs(0, [], 0)
        return combinations
