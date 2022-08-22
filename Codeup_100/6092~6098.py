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
# n = int(input())
# s = list(map(int, input().split()))
# p = [0] * n

# for i in range(0, n):
#     p[i] = s[n - i - 1]

# for k in range(0, n):
#     print(p[k], end=' ')

# 6094 이상한 출석 번호 부르기3
# n = int(input())
# s = list(map(int, input().split()))

# min = s[0]
# for i in range(0, n):
#     if s[i] < min:
#         min = s[i]
# print(min)

# 6095 바둑판에 흰 돌 놓기
# n = int(input())

# arr = []

# for i in range(0, 20):
#     arr.append([])
#     for j in range(0, 20):
#         arr[i].append(0)

# for i in range(0, n):
#     a, b = map(int, input().split())        
#     arr[a][b] = 1

# for i in range(1, 20):
#     for j in range(1, 20):
#         print(arr[i][j], end=' ')
#     print()

# # 6096 바둑알 십자 뒤집기(py)
# arr = []
# for i in range(0, 19):
#     arr.append([])
#     arr[i] = list(map(int, input().split()))

# n = int(input())

# for i in range(0, n):
#    a, b = map(int, input().split())

#    for k in range(0, 19):
#     if arr[k][b - 1] == 1:
#         arr[k][b - 1] = 0
#     else:
#         arr[k][b - 1] = 1
    
#     if arr[a - 1][k] == 1:
#         arr[a - 1][k] = 0
#     else:
#         arr[a - 1][k] = 1

# for k in range(0, 19):
#     for j in range(0, 19):
#         print(arr[k][j], end=' ')
#     print()