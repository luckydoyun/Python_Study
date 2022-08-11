# codeup _ 100제 
# 기초-산술연산

# a, b = map(int, input().split())

# # if(a < b):
# #     print("True")
# # else:
# #     print("False")
# # if로 하지않고 그냥 print문에서 해결 가능
# print(a != b)

# n = int(input())

# # bool를 사용하면 0이 아닌 나머지 정수는  true 반환
# # not 를 사용하면 논리값을 역으로 바꿀 수 있다.
# print(not bool(n))

# a, b = map(int, input().split())
# c = bool(a)
# d = bool(b)
# 아래 관계는 배타적인 관계이다
# print((c and (not d)) or ((not c) and d))

a, b = map(int, input().split())
c = bool(a)
d = bool(b)

print(not c and not d)