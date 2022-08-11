# codeup _ 100제 
# 기초-산술연산

a, b, c = map(int, input().split())

# 가장 작은 값을 찾아보자
if a < b:
    if a < c:
        print(a)
    else:
        print(c)
else:
    if b < c:
        print(b)
    else:
        print(c)