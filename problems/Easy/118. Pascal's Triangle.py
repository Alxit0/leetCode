from typing import List


def generate(numRows: int) -> List[List[int]]:
    resp = [[1]]
    for i in range(numRows-1):
        temp = [1]
        for j in range(0, i):
            temp.append(resp[i][j] + resp[i][j+1])
        temp.append(1)
        resp.append(temp)
    return resp


def main():
    n = 8
    print(generate(n))


if __name__ == '__main__':
    main()
