
# # 4월 21일

# a = 'hello world'
# b = 'bye word'
# print(a)

# # format 사용시
# print('해당학색의 성적은 {}점 입니다' .format(a))  # format 함수를 사용해 {} 안에 결과 할당.

# # 더 간단한 방식
# print('해당학생의 점수는', a, '점 입니다', b)

# # 제일 좋은 방법
# print(f'해당학생의 점수는 {a}점 {b} 입니다')  # f가 없으면 다 글자로 인식해서 {}까지 전부 다 그대로 출력해준다.

# ---------------------------------------------------------------------------------------------

# # 실습 1

# my_name = input()     # 인풋을 받아서 마이네임 이라는 변수에 저장
# print(f'{my_name}님 안녕하세요!')     # f스트링을 이용해서 마이네임님 안녕하세요! 라고 프린트하기

# # 내풀이
# # 날짜 나오게하기
# import datetime
# today = 4/21
# print(time.(f'{my_name}님 안녕하세요! 오늘은 {today} 입니다!'))


# # 튜터님풀이
# # 날짜 나오게하기
# #(1)
# import datetime
# today = datetime.date.today()
# my_name = input()
# print(today)

# #(2)
# from datetime import datetime, date
# today = date.today()
# print(today)


# -----------------------------------------------------------

# # 실습 2 / 나이가 20살 이상인 경우 {이름}님 안녕하세요! 프린트하기
# # 내풀이
# my_list = [{"이름": "권기현", "나이": 32},
#            {"이름": "홍서연", "나이": 20},
#            {"이름": "박소진", "나이": 20},
#            {"이름": "이미진", "나이": 19},
#            {"이름": "이정현", "나이": 18},
#            {"이름": "연제건", "나이": 17},
#            {"이름": "강유지", "나이": 16},
#            {"이름": "김태연", "나이": 15},
#            {"이름": "김주영", "나이": 14}]

# for person in my_list:
#     if person["나이"] >= [20]:
#         print(f'{"이름"}님 안녕하세요!')


# # 튜터님 풀이
# for person in my_list:
#     if person["나이"] >= 20:
#         print(f'{person["이름"]}님 안녕하세요!')     # person 안에 있는 "이름"
# ---------------------------------------------------------------------------------------------
# # 실습 3 / 년, 월, 일 한국어로 바꾸기
# # 내풀이
# from datetime import datetime
# now = datetime.now()

# print(f"{년 : ,now.year}")
# print(f"{월 : ,now.month}")
# print(f"{일 : , now.day}")


# # 튜터님 풀이
# from datetime import datetime
# now = datetime.now()

# print(f"{my_name}님 안녕하세요! 오늘은 {npw.year}년 {now.month}월 {now.day}일 입니다.")

# ---------------------------------------------------------------------------------
# # 실습 4 / 20살 이상인 사람들에게 '권기현님 홍서연님 박소진님 안녕하세요' 라고 인사하기
# # 내풀이
# my_list = [{"이름": "권기현", "나이": 32},
#            {"이름": "홍서연", "나이": 20},
#            {"이름": "박소진", "나이": 20},
#            {"이름": "이미진", "나이": 19},
#            {"이름": "이정현", "나이": 18},
#            {"이름": "연제건", "나이": 17},
#            {"이름": "강유지", "나이": 16},
#            {"이름": "김태연", "나이": 15},
#            {"이름": "김주영", "나이": 14}]

# my_name = input()

# for person in my_list:
#     if person["나이"] >= 20:
#         print(f'{my_name}님 안녕하세요!', end="")  #안녕하세요! 가 계속 반복됨...

# 튜터님 풀이

# my_name = input()

# for person in my_list:
#     if person["나이"] >= 20:
#         print(f'{my_name}', end="")

# print("안녕하세요!")  # print 따로 빼주기

# ====================================================================
# # input split
# a, b, c = input().split()
# print(a)

# # map input split
# a = list(int, input().split())
# print(a)
# print(type(a))
# ----------------------------------------------------------------------
# # 실습 5
# # 내 풀이
# a = list(map(int, input().split()))
# print(a)

# for i in a:
#     print(i, end=' ')

# # 튜터님 풀이
# a = list(map(int, input().split()))
# print(a)

# for i in a:
#     print(i, end=' ')

# ------------------------------------------------------------
