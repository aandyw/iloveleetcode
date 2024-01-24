"""
The idea is turning each word in 'strs' into a index from the specific characters.
If another word shares the same index then that would mean it is an anagram.
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord("a")] += 1
            anagram_map[tuple(counts)].append(s)

        return anagram_map.values()
