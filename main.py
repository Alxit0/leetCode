"""
0 -> ''
1 -> '()'
"""


def generate_pare(lvl: int, top=None, rep=0):
    if top is None:
        top = {''}

    if lvl == 0:
        # print(rep)
        return top

    new_set = set()
    for i in top:
        for j in [f'(){i}', f'({i})', f'{i}()']:
            if j not in new_set:
                new_set.add(j)
            rep += 1

    return generate_pare(lvl-1, new_set, rep)


if __name__ == '__main__':
    a = 3

    print(generate_pare2(a), generate_pare(a))

