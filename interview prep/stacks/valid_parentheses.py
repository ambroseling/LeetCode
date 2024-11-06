
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for  i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            elif s[i] == ')' and stack and stack[-1] == '(':
                stack.pop()
            elif s[i] == ']' and stack and stack[-1] == '[':
                stack.pop()
            elif s[i] == '}' and stack and stack[-1] == '{':
                stack.pop()
        if stack:
            return False
        return True


# the closing parentheses must match the last opening parentheses in the stack
