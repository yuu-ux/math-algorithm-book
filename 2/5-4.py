N = int(input())

def is_prime(N):
    if N < 2:
        return False
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            return False
    return True

res = []
for i in range(2, N + 1):
    if is_prime(i):
        res.append(i)

print(*res)
