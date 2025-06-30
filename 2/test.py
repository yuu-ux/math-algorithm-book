N = int(input())
S = int(input())
A = list(map(int, input().split()))

ans = 'No'
for i in range(0, 1 << N):
    partsum = 0
    for j in range(0, N):
        if (i & (1 << j)):
            partsum += A[j]
    if S == partsum:
        ans = 'Yes'
        break
print(ans)
