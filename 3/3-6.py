from collections import Counter

N = int(input())
A = list(map(int, input().split()))

count = Counter(A)

ans = 0
for x in count:
    y = 100000 - x
    if x == y:
        ans += count[x] * (count[x] - 1) // 2
    elif x < y:
        ans += count[x] * count.get(y, 0)
print(ans)

Answer = 0
for i in range(1, 50000):
	Answer += cnt[i] * cnt[100000 - i]
Answer += cnt[50000] * (cnt[50000] - 1) // 2

# 出力
print(Answer)

# 全探索
# ans = 0
# total = 0
# for i in range(0, N):
#     for j in range(i+1, N):
#         if (A[i] + A[j]) == 100000:
#             ans += 1
# print(ans)
# nC2
# n!/r!(n - r)!
