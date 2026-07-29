from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = defaultdict(int)
        tdict = defaultdict(int)
        for char in s:
            sdict[char] += 1
        for char in t:
            tdict[char] += 1
        return sdict == tdict
        