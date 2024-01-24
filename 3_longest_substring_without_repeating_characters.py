class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        l, r = 0, 0
        uniques = set()
        result = 0

        while r < len(s):
            while s[r] in uniques:
                uniques.remove(s[l])
                l += 1

            uniques.add(s[r])
            result = max(result, len(uniques))
            r += 1

        return result
