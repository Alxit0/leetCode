from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        resp = strs[0]
        temp_resp = ""
        for i in range(1, len(strs)):
            temp = strs[i]
            # if "" in (resp, temp):
            #     resp = ""
            #     break
            k=-1
            for k, (i, j) in enumerate(zip(temp, resp)):
                if i != j:
                    break
            else:
                k+=1
            resp = resp[:k]

        return resp
                