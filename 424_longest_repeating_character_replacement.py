class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        l, r = 0, 0
        max_c = 0
        result = 0

        while r < len(s):
            seen[s[r]] = 1 + seen.get(s[r], 0)
            max_c = max(max_c, seen[s[r]])

            while (r - l + 1) - max_c > k:
                seen[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1)
            r += 1

        return result
