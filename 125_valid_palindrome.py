"""
Done using Two Pointer Method

"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        def condition(c):
            if c.isalpha() or c.isdigit():
                return c.lower()
            else:
                return ""

        filtered_s = "".join(map(condition, s))

        l, r = 0, len(filtered_s) - 1
        while l < r:
            if filtered_s[l] != filtered_s[r]:
                return False
            l += 1
            r -= 1

        return True
