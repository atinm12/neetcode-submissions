from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            order = [0] * 26
            for char in word:
                order[ord(char) - ord('a')] += 1
            order = tuple(order)
            anagrams[order].append(word)
        return list(anagrams.values())

        





            
