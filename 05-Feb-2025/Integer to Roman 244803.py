# Problem: Integer to Roman - https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        _dict = {1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}   
        ans = []
        
        while num > 0:
            if num//1000 > 0:
                ans.append(_dict[1000] *( num//1000))
                num = num % 1000
            elif num//900 == 1:
                num = num % 900
                ans.append('CM')

            elif num//500 > 0:
                ans.append(_dict[500] * (num//500))
                num = num % 500
            elif num//400 == 1:
                num = num % 400
                ans.append('CD')
            elif num//100 > 0:
                ans.append(_dict[100] * (num//100))
                num = num % 100

            elif num//90 == 1:
                num = num % 90
                ans.append('XC')

            elif num//50 > 0:
                ans.append(_dict[50] * (num//50))
                num = num % 50

            elif num//40 == 1:
                num = num % 40
                ans.append('XL')

            elif num//10 > 0:
                ans.append(_dict[10] * (num//10))
                num = num % 10
            elif num == 9:
                num = 0
                ans.append('IX')
            elif num//5 > 0:
                ans.append(_dict[5] * (num//5))
                num = num % 5
            elif num == 4:
                num = 0
                ans.append('IV')
            else:
                ans.append('I'*num)
                num = 0
        return ''.join(ans)