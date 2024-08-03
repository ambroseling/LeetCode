class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_vowels = 0
        vowels = {'a':1,'e':1,'i':1,'o':1,'u':1}
        window = []
        for i in range(len(s)+1):
            if i < k: 
                val = 1 if s[i] in vowels else 0
                window.append(val)
            else:
                vowels_window = sum(window)
                max_vowels = max(vowels_window,max_vowels)
                if i <= len(s)-1:
                    val = 1 if s[i] in vowels else 0
                    window.append(val)
                    window.pop(0)
        return max_vowels