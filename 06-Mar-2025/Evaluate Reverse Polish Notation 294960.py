# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        op = {'*','/','+','-'}

        for token in tokens:
            if token in op:
                num1 = st.pop()
                num2 = st.pop()
                st.append(int(eval(f'{num2} {token} {num1}')))
            else:
                st.append(token)
        return int(st[0])