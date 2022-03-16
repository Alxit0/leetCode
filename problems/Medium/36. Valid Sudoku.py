from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    rose = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 0),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1)
    ]
    square = lambda x, y: [board[x+i][y+j] for i, j in rose]
    for pos in [(1, 1), (1, 4), (1, 7), (4, 1), (4, 4), (4, 7), (7, 1), (7, 4), (7, 7)]:
        temp = ''.join(square(*pos)).replace('.', '')
        print(temp, set(temp))
        if len(temp) != len(set(temp)):
            return False

    for row in board:
        temp = ''.join(row).replace('.', '')
        if len(temp) != len(set(temp)):
            return False

    temp = [[board[i][j]for i in range(9)]for j in range(9)]
    for row in temp:
        t = ''.join(row).replace('.','')
        if len(t) != len(set(t)):
            return False

    return True


def main():
    b = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    c = [["9", ".", ".", "6", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", "6", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "1", ".", "3", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "8"],
         [".", ".", ".", ".", ".", "8", ".", ".", "."],
         [".", ".", ".", "4", ".", ".", "2", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "1"],
         ["6", ".", ".", ".", "1", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."]]
    print(isValidSudoku(c))


if __name__ == '__main__':
    main()