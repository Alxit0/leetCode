from typing import List




class Solution:
    
    def position_calc(self, n: int):
        # n, n-1, n-1, n-2, n-2, n-3, n-3
        
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        d = 0
        y, x = 0, -1
        
        for _ in range(n):
            y, x = directions[d][0] + y, directions[d][1] + x
            yield y, x
        
        while n:
            n -= 1
            
            d = (d + 1)%4
            for _ in range(n):
                y, x = directions[d][0] + y, directions[d][1] + x
                yield y, x
            
            d = (d + 1)%4
            for _ in range(n):
                y, x = directions[d][0] + y, directions[d][1] + x
                yield y, x


    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for _ in range(n)]

        for i, (y, x) in enumerate(self.position_calc(n)):
            res[y][x] = i + 1
        
        return res


def test(fun, case, res):

    sol = fun(case)

    if sol == res:
        print("OK")
    else:
        print(f"{case = }")
        print(f"{sol = }")
        print(f"{res = }")
        print()

def main():
    s = Solution()

    test(
        s.generateMatrix,
        3,
        [[1,2,3],[8,9,4],[7,6,5]]
    )
    test(
        s.generateMatrix,
        1,
        [[1]]
    )


if __name__ == "__main__":
    main()
