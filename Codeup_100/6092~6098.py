# codeup _ 100제 
# 기초-리스트

# 6092 이상한 출석 번호 부르기1
# n = int(input())
# s = list(map(int, input().split()))
# d = [0] * 23

# for i in range(0, n):
#     d[s[i] - 1] += 1
# for p in range(0, 23):
#     print(d[p], end=' ')

# 6093 이상한 출석 번호 부르기2
n = int(input())
s = list(map(int, input().split()))
p = [0] * n

for i in range(0, n):
    p[i] = s[n - i - 1]

for k in range(0, n):
    print(p[k], end=' ')

