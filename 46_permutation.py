class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(nums, path):
            if len(nums) == 0:
                result.append(path)
                return

            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1 :], path + [nums[i]])

        dfs(nums, [])
        return result
