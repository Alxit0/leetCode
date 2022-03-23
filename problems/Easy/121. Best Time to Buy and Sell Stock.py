from typing import List


def maxProfit(prices: List[int]) -> int:
    buy = 0
    resp = 0
    for sell in range(1, len(prices)):
        valor_atual = prices[sell] - prices[buy]
        if valor_atual > 0:
            resp = max(resp, valor_atual)
        else:
            buy = sell
    return resp


def main():
    case = [7, 1, 5, 3, 6, 4]
    print(maxProfit(case))


if __name__ == '__main__':
    main()
