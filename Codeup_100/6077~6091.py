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

# 6084 소리 파일 저장용량 계산하기
# h b(비트) c s 8bit = 1byte
# h, b, c, s = map(int, input().split())

# storage = h * b * c * s / 8 / 1024 / 1024
# print(format(storage,'.1f'), 'MB')

# 6085 그림 파일 저장용량 계산하기
# w, h, b = map(int, input().split())

# storage = w * h * b / 8 / 1024 / 1024
# print(format(storage,'.2f'), 'MB')

# 6086 거기까지! 이제 그만~
# end = int(input())
# start = 0
# sum = 0

# while(True):
#     sum += start
#     if sum >= end:
#         break
#     start += 1
# print(sum)

# 6087 3의 배수는 통과(설명)
# end = int(input())
# start = 1

# while(True):
#     if start > end:
#         break
#     if start % 3 != 0:
#         print(start, end=' ')
#     start += 1

# 6088 수 나열하기1
# s, d, n = map(int, input().split())
# result = s

# for i in range(2, n + 1):
#     result += d
# print(result)

# 6089 수 나열하기2
# s, d, n = map(int, input().split())
# result = s

# for i in range(2, n + 1):
#     result *= d
# print(result)

# 6090 수 나열하기3
# a, m, d, n = map(int, input().split())
# result = a

# for i in range(2, n + 1):
#     result = result * m + d

# print(result)

# 6091 함께 문제 푸는 날(설명)
from math import gcd

a, b, c = map(int, input().split())
result = a * b // gcd(a, b)
result = result * c // gcd(result, c)

print(result)
