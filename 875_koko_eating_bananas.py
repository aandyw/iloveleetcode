class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) + 1
        k = 0
        while l <= r:
            mid = l + (r - l) // 2

            time_taken = 0
            for p in piles:
                time_taken += math.ceil(p / mid)
                if time_taken > h:
                    break

            if time_taken <= h:
                k = mid
                r = mid - 1
            elif time_taken > h:
                l = mid + 1

        return k
