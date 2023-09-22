class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        idx = len(words) - 1
        while idx >= 0 and not words[-1]:
            words.pop()
            idx -= 1

        return len(words[-1])

