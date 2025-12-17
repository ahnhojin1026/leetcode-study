from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        # s has to be even to be valid (all parentheses have their pair)
        if len(s) % 2 == 1:
            return False
        
        # ust stack to track parentheses pairs
        stack = deque()
        for i, n in enumerate(s):
            # push opening parentheses onto stack
            if n in ["(","{","["]:
                stack.append(n)
            # if closing parentheses found but stack is empty, return False
            elif not stack:
                return False
            # pop from stack and check if it matches
            elif n == ")":
                top = stack.pop()
                if top != "(":
                    return False
            elif n == "]":
                top = stack.pop()
                if top != "[":
                    return False
            elif n == "}":
                top = stack.pop()
                if top != "{":
                    return False
        # if stack is not empty, return False (means some parentheses are not closed)
        if stack:
            return False
        
        # if all checks passed, return True
        return True