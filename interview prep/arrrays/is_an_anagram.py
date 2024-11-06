class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# just sort the strings and compare them, if they are the same then they are anagrams