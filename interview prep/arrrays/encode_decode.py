class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # add the length of the string and a # to the result string
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        # loop through the string
        while i < len(s):
            j = i
            # find the length of the string

            while s[j] != '#':
                j += 1
            # convert the length to an integer
            length = int(s[i:j])
            # add the string to the result list
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res