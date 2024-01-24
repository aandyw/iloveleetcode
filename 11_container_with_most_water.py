class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        area = min(height[l], height[r]) * (r - l)
        while l < r:
            min_h = min(height[l], height[r])
            area = max(area, min_h * (r - l))

            if min_h == height[l]:
                l += 1
            else:
                r -= 1

        return area
