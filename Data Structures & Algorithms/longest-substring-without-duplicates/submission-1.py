class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = []
        current = []
        for char in s:
            if char not in current:
                current.append(char)
            else: 
                index = current.index(char)
                current = current[index + 1 :]
                current.append(char)
            if len(current) > len(longest):
                longest = current
                print(f'current: {current}, longest: {longest}, char: {char}')
        return len(longest)

        