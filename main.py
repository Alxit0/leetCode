import math

prop = 3 * 10 ** 8
dist = 10 * 10**3
tp = dist / prop
print(f"Tp = {dist} / {prop} = {tp}")

tamanho = 25 * 2 ** 23  # 23 - M (nao mexer)
B = 100 * 10 ** 6  # 6 - M
M = 2**8
SNdb = 15
# SN = 10 ** (SNdb / 10)
SN = 15
# C = 2 * B * math.log2(M); print(f"C = 2 * {B} * {math.log2(M)} = {C}")
C = B * math.log2(SN + 1); print(f"SN = 10 ** ({SNdb} / 10) = {SN}"); print(f"C = {B} * {math.log2(1 + SN)} = {C}")
tx = tamanho / C


print(f"Tx = {tamanho} / {C} = {tx}")
print(f"Tx + Tp ~= {round(tx + tp, 3)}")

print(2**( (100 * 2**20) / (2*20*10**6) ))

# teste