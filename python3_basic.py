# 파이썬에서는 코드의 블록(Block)을 들여쓰기(Indent)로 지정합니다.
# 탭과 공백문자(space)를 여러 번 사용하는 쪽으로 두 진영이 있다.
# 상당수 파이썬 커뮤니티에서는 4개의 공백 문자를 사용하는 것이 사실상의 표준

# 비교 연산자 : 특정한 두 값을 비교할 때 이용할 수 있습니다.
# 파이썬의 기타 연산자 : 여러 개의 데이터를 담는 자료형을 위해 in 연산자와 not in 연산자가 제공됩니다.
# - 리스트, 튜플, 문자열, 딕셔너리 모두에서 사용이 가능
# x in 리스트 : 리스트 안에 x가 들어가 있을 때 참(Ture)이다.
# x not in 문자열 : 문자열 안에 x가 들어가 있지 않을 때 참(Ture)이다.

# 파이썬의 pass 키워드
# 아무것도 처리하고 싶지 않을 때 pass 키워드 사용
# 보통 디버깅 과정에서 일단 조건문의 형태만 만들어 놓고 조건문을 처리하는 부분은 비워놓고 싶은 경우

# 조건문의 간소화 : 소스코드가 한 줄인 경우에만 굳이 줄 바꿈을 하지 않고도 간략하게 표현할 수 있다.
# 조건부 포현식(Conditional Expression)은 if ~ els문을 한줄에 작성할 수 있도록 해준다.
# ex) result = "Success" if score >= 80 else "Fail"

# for i in range(start, end, step):
# 특정 조건을 제외하고 싶다면 if와 continue를 사용하자
# ex)
# scores = [90, 85, 77, 65, 97]
# cheating_student_list = {2, 4} # 2, 4번째 학생 제외 조건

# for i in range(5):
#     if i + 1 in cheating_student_list:
#         continue
#     if scores[i] >= 80:
#         print(i + 1, "번 학생은 합격입니다.")

# 함수 : 함수를 사용하면 소스코드의 길이를 줄일 수 있습니다.
# global 키워드 : 함수 바깥에 선언된 변수를 바로 참조하게 됩니다.

# 람다 표현식 : 함수를 매우 간단하게 작성할 수 있습니다.
# - 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있다는 점이 특징
# print((lambda a, b: a + b)(3, 7))

# 람다 표현식 예시
# array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

# def my_key(x):
#     return x[1]
# print(sorted(array, key=my_key))
# print(sorted(array, key=lambda x: x[1]))

# 유용한 표준 library
# 내장 함수 : pinrt(), input(), sorted()
# itertools : 순열과 조합 라이브러리를 제공
# heapq : 힙 기능을 제공하는 라이브러리, 우선순위 큐 기능을 구현하기 위해 사용
# bisect : 이진 탐색 기능을 제공하는 라이브러리
# collections : 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함하고 있는 라이브러리

