class Solution:
    ...


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
        s.singleNumber,
        [2,2,1],
        1
    )


if __name__ == "__main__":
    main()
