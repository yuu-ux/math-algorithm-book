N = int(input())
S = int(input())

cnt = 0
for i in range(1, N + 1):
    ans = 0
    for j in range(1, N + 1):
        ans = i + j
        if ans <= S:
            cnt += 1

print(cnt)
