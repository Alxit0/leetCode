class Solution:
    def romanToInt(self, s: str) -> int:
        resp = 0
        vals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        ant = s[0]
        temp = vals[ant]
        for i in s[1:]:
            if i == ant:
                temp += vals[i]
            elif vals[i] > vals[ant]:
                resp += vals[i] - temp
                temp = 0
            else:
                resp += temp
                temp = vals[i]
            ant = i
            # print(resp)
        resp += temp
        return resp