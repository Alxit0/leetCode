from pprint import pprint
from typing import List


class Solution:
    possible_moves = (
        (4, 6),
        (6, 8),
        (7, 9),
        (4, 8),
        (0, 3, 9),
        (),
        (0, 1, 7),
        (2, 6),
        (1, 3),
        (2, 4)
    )

    def knightDialer(self, n: int) -> int:
        memo = [1]*10
        mod = 10**9 + 7

        for _ in range(n-1):
            new_memo = []
            for i in self.possible_moves:
                new_memo.append(
                    sum(map(lambda x:memo[x], i))%mod
                )
            memo = new_memo
        
        return sum(memo)%mod



def main():
    s = Solution()

    print(s.knightDialer(1), 10)
    print(s.knightDialer(2), 20)
    print(s.knightDialer(3131), 136006598)

if __name__ == '__main__':
    main()