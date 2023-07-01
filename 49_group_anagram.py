class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)

        for word in strs:
            key = [0] * 26
            for c in word:
                key[ord(c) - ord('a')] += 1
            m[tuple(key)].append(word)

        return list(m.values())