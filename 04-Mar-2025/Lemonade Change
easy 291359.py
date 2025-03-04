# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = {5:0,10:0}
        for bill in bills:
            if bill == 5:
                count[5]+=1
            elif bill == 10:
                if count[5] == 0:
                    return False
                count[10] += 1
                count[5] -= 1
            else:
                if count[5] == 0:
                    return False
                if count[5] < 3 and count[10] == 0:
                    return False
                
                if count[5] >=1 and count[10] >= 1:
                    count[10] -= 1
                    count[5] -= 1
                elif count[5] >= 3:
                    count[5] -= 3
                else:
                    return False
                    
        return True

