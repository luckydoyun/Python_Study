# codeup _ 100제 
# 기초-종합

# 6077 짝수 합 구하기
# n = int(input())
# sum = 0

# for i in range(1, n + 1):
#     if i % 2 == 0:
#        sum += i

# print(sum)

# 6078 원하는 문자가 입력될 때까지 반복 출력하기
# n = True

# while(n):
#     n = input()
#     print(n)
#     if n == 'q':
#         break

# 6079 언제까지 더해야 할까?
# end = int(input())
# start = 1
# sum = 0

# while(True):
#     sum += start
#     if sum >= end:
#         print(start)
#         break
#     start += 1

# 6080 주사위 2개 던지기(설명)
# n, m = map(int, input().split())

# for i in range(1, n + 1):
#     for k in range(1, m + 1):
#         print(i, k)

# 6081 16진수 구구단 출력하기
# n = input()

# #입력받은 16진수를 10진수로
# n10 = int(n, 16)
# for i in range(1, 16):
#     print('%X*%X=%X' %(n10, i, n10 * i))

# 6082 3 6 9 게임의 왕이 되자(설명)
# 10을 나눴을 때 나머지가 3, 6, 9를 찾으면 된다....
# n = int(input())

# for i in range(1, n + 1):
#     if ('3') in str(i):
#         print('X', end=' ')
#     elif ('6') in str(i):
#         print('X', end=' ')
#     elif ('9') in str(i):
#         print('X', end=' ')
#     else:
#         print(i, end=' ')


# 6083 빛 섞어 색 만들기(설명)
# r, g, b = map(int, input().split())
# for i in range(0, r):
#     for k in range(0, g):
#         for j in range(0, b):
#             print(i, k, j)
# print(r * g * b)