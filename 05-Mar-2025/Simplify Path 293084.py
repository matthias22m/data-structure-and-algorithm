# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        ls = path.split('/')
        stack = []
        for d in ls:
            if d=='' or d == '.':
                continue
            if d == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(d)
        return '/'+'/'.join(stack)
