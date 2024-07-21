class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = ""
        stack = []
        for i in range(len(s)):
            stack.append(s[i])
            if s[i] == "]":
                stack.pop(-1)
                subs = []
                j = 0
                num = ""
                while True:
                    if stack[-1].isnumeric():
                        if len(stack) >= 2 and stack[-2].isnumeric():
                            num = stack.pop(-1) + num
                            continue
                        else:
                            num = stack.pop(-1) + num
                            subs = int(num) * subs
                            stack.extend(subs)
                            break
                    c = stack.pop(-1)
                    if c != "[":
                        subs.insert(0,c)
        output = ''.join(stack)
        return output
            


# go through all the individual substrings
# for each substring, recurse if 

if __name__ == "__main__":
    s = Solution()
    import ipdb; ipdb.set_trace()
    o = s.decodeString("3[a2[c]]")