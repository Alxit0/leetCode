class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        new = ""
        num = self.countAndSay(n-1)
        cur = num[0]
        counter = 1
        for i in num[1:]:
            if i == cur:
                counter += 1
            else:
                new += f"{counter}{cur}"
                cur = i
                counter = 1
        
        new += f"{counter}{cur}"
        # print(n, new)
        return new
