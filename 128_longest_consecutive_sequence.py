class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for num in s:
            if (num - 1) not in s:
                curr_len = 1
                while (num + curr_len) in s:
                    curr_len += 1
                longest = max(longest, curr_len)
        
        return longest
