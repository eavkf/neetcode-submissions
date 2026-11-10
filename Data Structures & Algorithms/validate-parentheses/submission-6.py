class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 != 0:
            return False
        for x in s:
            if x == ')':
                if not stack or stack[-1] != '(':
                    return False
                else:
                    stack.pop()
            elif x == '}':
                if not stack or stack[-1] != '{':
                    return False
                else:
                    stack.pop()
            elif x == ']':
                if not stack or stack[-1] != '[':
                    return False
                else:
                    stack.pop()
            else:
                stack.append(x)
        return (stack == [])