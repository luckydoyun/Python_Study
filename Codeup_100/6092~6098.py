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

# 6097 설탕과자 뽑기
# 세로(h) 가로(w) 공백을 두고 입력
# 막대의 개수(n)
# 막대의 길이(i), 방향(d)(가로:0, 세로:1), 좌표(x,y)
# h, w = map(int, input().split())

# arr = []

# for j in range(0, h):
#     arr.append([])
#     for k in range(0, w):
#         arr[j].append(0)

# n = int(input())

# for j in range(0, n):
#     i, d, x, y = map(int, input().split())
#     if d == 1: #세로 막대기
#         for k in range(i):
#             arr[x + k - 1][y - 1] = 1
#     else: #가로 막대기
#         for k in range(i):
#             arr[x - 1][y + k - 1] = 1

# for j in range(0, h):
#     for k in range(0, w):
#         print(arr[j][k], end=' ')
#     print()

# 6098 성실한 개미(py)
# 0 : 갈 수 있는 곳
# 1 : 벽 또는 장애물
# 2 : 먹이
# 개미집은 (2, 2) = 출발점

arr = []

for i in range(10):
    arr.append([])
    arr[i] = list(map(int, input().split()))

start_x = 2
start_y = 2
next_x = 2
next_y = 2

while(True):
    # 시작은 항상 개미집(2, 2)
    if arr[start_x - 1][start_y - 1] == 0: #도착한 곳이 갈수있는곳(0)이라면 가자
        if arr[start_x - 1][start_y - 1] == 2: #도착한 곳이 먹이(2)가 있는 곳이라면 그만(오른쪽으로 가다가)
            arr[start_x - 1][start_y - 1] = 9
            break
        arr[start_x - 1][start_y - 1] = 9
        print(start_x, " 오른쪽을 가다가 내가 접수한곳 ", start_y)
        start_y += 1
    else: #도착한 곳이 갈수없는곳(1)이라면 되돌아가서 아래로 가자
        start_y -= 1
        start_x += 1
        if start_x >= 10 or start_y >= 10:
            break
        if arr[start_x - 1][start_y - 1] == 2: #도착한 곳이 먹이(2)가 있는 곳이라면 그만(아래로 가다가)
            arr[start_x - 1][start_y - 1] = 9
            break
        arr[start_x - 1][start_y - 1] = 9
        print(start_x, " 아래로 가다가 내가 접수한곳 ", start_y)
        start_y += 1
    
    if arr[start_x - 1][start_y - 1] == 2: #도착한 곳이 먹이(2)가 있는 곳이라면 그만
            arr[start_x - 1][start_y - 1] = 9
            break 

#print("출력은 아래")
for j in range(10):
    for k in range(10):
        print(arr[j][k], end=' ')
    print()
        