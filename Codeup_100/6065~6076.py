# codeup _ 100제 
# 기초-조건/선택실행구조/반복실행구조


# a, b, c = map(int, input().split())

# if a % 2 == 0:
#     print("even")
# else:
#     print("odd")

# if b % 2 == 0:
#     print("even")
# else:
#     print("odd")

# if c % 2 == 0:
#     print("even")
# else:
#     print("odd")


# n = int(input())

# if n < 0 and n % 2 == 0: #음수이면서 짝수
#     print("A")
# elif n < 0 and n % 2 != 0: #음수이면서 홀수
#     print("B")
# elif n > 0 and n % 2 == 0: #양수이면서 짝수
#     print("C")
# elif n > 0 and n % 2 != 0: #양수이면서 음수
#     print("D")
# 위 코드를 음수와 양수부터 나누고 시작하면
# 코드가 간단해진다.


# n = int(input())

# if n <= 100 and n >= 90:
#     print('A')
# elif n >= 70:
#     print('B')
# elif n >= 40:
#     print('C')
# elif n >= 0:
#     print('D')

# n = input()

# if n == 'A':
#     print("best!!!")
# elif n == 'B':
#     print("good!!")
# elif n == 'C':
#     print("run!")
# elif n == 'D':
#     print("slowly~")
# else:
#     print("what?")

# n = int(input())

# if n == 12 or n == 1 or n == 2:
#     print("winter")
# elif n == 3 or n == 4 or n == 5:
#     print("spring")
# elif n == 6 or n == 7 or n == 8:
#     print("summer")
# elif n == 9 or n == 10 or n == 11:
#     print("fall")

# import random
# while(1):
#     n = random.randint(-2147483648 , 2147483648 )
#     #n = random.randint(-111 , 111 )
#     if n == 0:
#         break
#     print(n)

# n = int(input())

# while(n):
#     print(n-1)
#     n-=1

# start = ord('a')
# end = ord(input())

# while(end - start + 1):
#     print(chr(start), end=' ')
#     start+=1

# n = int(input())
# start = 0

# while(n + 1):
#     print(start)
#     start+=1
#     n-=1

n = int(input())
start = 0

for i in range(0,n + 1):
    print(i)
