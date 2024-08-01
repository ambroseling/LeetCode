class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        numMap = {
            1:None,
            2:['a','b','c'],
            3:['d','e','f'],
            4:['g','h','i'],
            5:['j','k','l'],
            6:['m','n','o'],
            7:['p','q','r','s'],
            8:['t','u','v'],
            9:['w','x','y','z']
        }
        digits = list(digits)
        digitLen = len(digits)
        constructed = []
        combo = ""
        def construct(combo,digits):
            if len(combo) == digitLen:
                constructed.append(combo)
                return 
            if len(digits) > 0:
                lastDigit = digits[-1]
                for letter in numMap[int(lastDigit)]:
                    construct(letter+combo,digits[:-1])
            else:
                return
        construct(combo,digits)

        return constructed
