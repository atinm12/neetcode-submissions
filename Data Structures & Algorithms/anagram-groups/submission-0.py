class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        uniques = []
        uniquesMap = {}
        for word in strs:
            wordMap = {}
            hasAnagram = False
            #makes map for word
            for char in word:
                if char in wordMap: wordMap[char] += 1
                else: wordMap[char] = 1
            #goes through each unique anagram
            for unique in uniques:
                uniqueMap = {}
                #makes map for each unique anagram
                for char in unique:
                    if char in uniqueMap: uniqueMap[char] += 1
                    else: uniqueMap[char] = 1
                #checks if word and unique are anagrams
                if wordMap == uniqueMap:
                    uniquesMap[unique].append(word)
                    hasAnagram = True
            if hasAnagram == False:
                uniques.append(word)
                uniquesMap[word] = [word]
        total = []
        for key in uniques:
            total.append(uniquesMap[key])
        return total




            
