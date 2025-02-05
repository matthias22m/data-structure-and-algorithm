# Problem: Swap Case - https://www.hackerrank.com/challenges/swap-case?isFullScreen=true

def swap_case(s):
    
    ls = '' 
    for char in s:
        if not char.isalnum():
            ls += char
        elif char.islower():
            ls += char.upper()
        else:
            ls += char.lower()
    return ls

