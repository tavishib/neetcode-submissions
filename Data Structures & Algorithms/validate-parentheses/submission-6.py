class Solution:
    def isValid(self, s: str) -> bool:
        stack = ""
        for c in s:
            if c == '[' or c == '{' or c == '(':
                stack = stack + c
            elif c == ']':
                if len(stack) > 0 and stack[len(stack)-1] == '[':
                    stack = stack[:-1]
                else:
                    return False
            elif c == '}':
                if len(stack) > 0 and stack[len(stack)-1] == '{':
                    stack = stack[:-1]
                else:
                    return False
            elif c == ')':
                if len(stack) > 0 and stack[len(stack)-1] == '(':
                    stack = stack[:-1]
                else:
                    return False
            else:
                continue
        if len(stack) == 0:
            return True      
        else:
            return False      