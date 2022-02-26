from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    tam_tot = len(matrix)*len(matrix[0])
    y = lambda x: matrix[x//len(matrix[0])][x % len(matrix[0])]
    ini, fin = 0, tam_tot-1

    while ini <= fin:
        guess = (ini + fin)//2
        valor = y(guess)
        if valor == target:
            return True
        elif valor < target:
            ini = guess + 1
        else:
            fin = guess - 1
    return False


def main():
    a = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    b = 3
    print(searchMatrix(a, b))


if __name__ == '__main__':
    main()
