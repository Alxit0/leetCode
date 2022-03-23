from typing import List


def matrixReshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    if len(mat)*len(mat[0]) != r*c:
        return mat
    resp = [[]for _ in range(r)]
    p = 0
    for i in mat:
        for j in i:
            resp[p//c].append(j)
            p += 1
    return resp


def main():
    ma = [[1, 2, 3, 4]]
    a = 2
    b = 2

    print(matrixReshape(ma, a, b))


if __name__ == '__main__':
    main()
