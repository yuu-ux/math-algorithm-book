# 1から100まで加算した結果を返すプログラム
N = 100
total = 0
for i in range(1, N + 1):
    total += i
print(total)

total = 0
total = int((N * (N + 1)) / 2)
print(total)

# N ^ 2 の シグマ
total = 0
for i in range(1, N + 1):
    total += i ** 2
print(total)

total = 0
total = int((N * (N + 1) * (2 * N + 1)) / 6)
print(total)


