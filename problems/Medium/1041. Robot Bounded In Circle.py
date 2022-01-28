class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        rose = [
            (1, 0),  # N
            (0, 1),  # E
            (-1, 0),  # S
            (0, -1)  # W
        ]
        pos = (0, 0)
        dire = 0
        for i in instructions:
            if i == 'G':
                temp = rose[dire]
                pos = (pos[0] + temp[0], pos[1] + temp[1])
            elif i == 'L':
                dire = (dire - 1) % 4
            elif i == 'R':
                dire = (dire + 1) % 4

        # print(pos)
        return pos == (0, 0) or dire != 0