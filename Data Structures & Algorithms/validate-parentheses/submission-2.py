from collections import defaultdict
class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')': '(', ']': '[', '}': '{'}
        stack = []
        for char in s:
            if char not in hashmap:
                stack.append(char)
            else:
                if len(stack) == 0: return False
                popped = stack.pop()
                if hashmap[char] != popped: return False
        return len(stack) == 0

