from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = defaultdict(list)
        for word in strs:
            index = [0] * 26
            for char in word:
                index[ord(char) - ord('a')] += 1
            index = tuple(index)
            anagramDict[index].append(word)
        return list(anagramDict.values())





            
