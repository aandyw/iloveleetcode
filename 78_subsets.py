class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_set = []
        subsets = []

        def dfs(i):
            if i == len(nums):
                power_set.append(subsets.copy())
                return

            subsets.append(nums[i])
            dfs(i + 1)
            subsets.pop()
            dfs(i + 1)

        dfs(0)
        return power_set
