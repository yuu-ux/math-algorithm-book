N = int(input())

res = []
i = 2
LIMIT = int(N ** 0.5)
for i in range(2, LIMIT + 1):
    while N % i == 0:
        N /= i
        res.append(i)

if N >= 2:
    res.append(int(N))
print(*res)
