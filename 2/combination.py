N = int(input())
S = int(input())
A = list(map(int, input().split()))

answer = 'No'

# 2のN乗分繰り返す
# 3枚だった場合
# 0 1 2 3 4 5 6 7
# 1 << N で 2 の N乗を表せるということ
loop = 2 ** N
for i in range(loop-1):
# Sと一致するか確認する用の変数
    partsum = 0
# N 回繰り返す
# カードが NマイだからNパターン試すってこと
    for j in range(0, N):
# 0 & 1 << 0 = 0
# 0 & 1 << 1 = 0
# 0 & 1 << 2 = 0
# 1 & 1 << 0 = 1 0001 0001
# 1 & 1 << 1 = 0 0001 0010
# 1 & 1 << 2 = 0 0001 0100
# 2 & 1 << 0 = 0 0010 0001
# 2 & 1 << 1 = 1 0010 0010
# 2 & 1 << 2 = 0 0010 0100
        if (i & (1 << j)) != 0:
            partsum += A[j]
    if partsum == S:
        answer = 'Yes'
        break
print(answer)
