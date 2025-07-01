# 一つのシグマは1ループと同じ
# 二重シグマの場合は二重ループと同じ

# 5 シグマ, i=1, i^2 であれば
total = 0
for i in range(1, 6):
    total += i ** 2
print(total)

total = 0
for i in range(2, 6):
    for j in range(1, 6):
        total += i + j
print(total)

