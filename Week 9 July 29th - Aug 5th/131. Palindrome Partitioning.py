class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            # If we've reached the end of the string, add the current partition to the result
            if i >= len(s):
                res.append(part.copy())
                return
            # Explore every possible end index j for a substring starting at index i
            for j in range(i, len(s)):
                # Check if the substring s[i:j+1] is a palindrome
                if self.isPali(s, i, j):
                    part.append(s[i:j+1])  # Add the palindrome substring to the current partition
                    dfs(j + 1)             # Recur to find the next part of the partition
                    part.pop()             # Backtrack by removing the last added palindrome

        dfs(0)
        return res

    def isPali(self, s: str, l: int, r: int) -> bool:
        # Check if the substring s[l:r+1] is a palindrome
        while l < r:
            if s[l] != s[r]:
                return False  # Fixed typo from 'Fales' to 'False'
            l, r = l + 1, r - 1
        return True