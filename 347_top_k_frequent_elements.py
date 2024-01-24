class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freqs = [[] for i in range(len(nums) + 1)]

        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
        for n, freq in counts.items():
            freqs[freq].append(n)

        out = []
        for i in range(len(freqs) - 1, 0, -1):
            for n in freqs[i]:
                out.append(n)
                if len(out) == k:
                    return out
        return out
