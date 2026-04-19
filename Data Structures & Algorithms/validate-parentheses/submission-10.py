class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for i in s:
            if i in "({[":
                stack.append(i)
            elif i in ")}]":
                if not stack or matches[i] != stack[-1]:
                    return False
                else:
                    stack.pop()
        if stack == []:
            return True
        else:
            return False