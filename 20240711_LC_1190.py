class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ')':
                sec = []
                while stack[-1] != '(':
                    sec.append(stack.pop())
                stack.pop()
                stack.extend(sec)
            else:
                stack.append(c)
        return ''.join(stack)
