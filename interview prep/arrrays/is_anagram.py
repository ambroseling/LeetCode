
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if the two strings are not the same length, they cannot be anagrams
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

# main idea is to use a hash map to count the frequency of each character in both strings and then compare the two hash maps
# hashmaps created for each string to store the frequency of each character
# if the two hashmaps are equal, then the two strings are anagrams of each other
