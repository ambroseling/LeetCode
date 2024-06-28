class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        chars1 = set(word1)
        chars2 = set(word2)
        chars1_freq = {}
        chars2_freq = {}
        if chars1 == chars2 and len(chars1) == len(chars2):
            # if there are, check for operation 2
            if len(word1) != len(word2):
                return False
            # if there are no repeats, return true
            if len(chars1) == len(word1):
                return True
            else:
                for char in chars1:
                    chars1_freq[char] = word1.count(char)
                    chars2_freq[char] = word2.count(char)

                if sorted(list(chars2_freq.values())) == sorted(list(chars1_freq.values())):
                    return True
                else:
                    return False
        else:
            return False

            