# idea is  to shrink the sliding window from the left until there are no duplicates
# then we move the left pointer to the right until the duplicate is removed
# we keep track of the max length of the substring without duplicates



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        res = 0

        for right in range(len(s)):
            # if the character is in the set, we remove the leftmost character from the set
            while s[right] in charSet:
                # remove the leftmost character from the set
                charSet.remove(s[left])
                # everytime you remove a character from the set, you move the left pointer to the right
                left += 1
            # add the current character to the set
            charSet.add(s[right])
            # update the max length of the substring without duplicates
            res = max(res, right - left + 1)
        return res