N = int(input())
A = list(map(int, input().split()))

def Euclidean(A, B):
    if A == 0:
        return B
    if B == 0:
        return A
    if A > B:
        return Euclidean(A % B, B)
    else:
        return Euclidean(A, B % A)

res = Euclidean(A[0], A[1])
for i in range(2, N):
    res = Euclidean(res, A[i])
print(res)
