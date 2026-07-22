class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not (len(s) == len(t)): return False
        first = {}
        for char in s:
            if char in first:
                first[char] += 1
            else: 
                first[char] = 1
        for char in t:
            if char not in first: return False
            first[char] -= 1
            if first[char] == -1: return False
        return True