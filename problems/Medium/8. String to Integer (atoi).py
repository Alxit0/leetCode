class Solution:
    def myAtoi(self, s: str) -> int:
        s = list(s.strip())
        signal = 1
        if len(s) > 1 and s[0] in "+-":
            if s[0] == '-':
                signal = -1
            del s[0]
        abso = 0
        for i in s:
            if not i.isdigit():
                break
            abso *= 10
            abso += int(i)
        
        resp = abso * signal
        if resp < -2**31:
            resp = -2**31
        elif resp > 2**31-1:
            resp = 2**31-1
            
        return resp

# -91283472332
# -2147483648