# 20230424 복습

# 백준 1000번
# A+B
# a, b = map(int, input().split())
# print(a+b)

# # A-B
# a, b = map(int, input().split())
# print(a-b)

# # A*B
# a, b = map(int, input().split())
# print(a*b)

# # A/B
# a, b = map(int, input().split())
# print(a/b)

# # A%B
# a, b = map(int, input().split())
# print(a % b)

# -----------------------------------------

# 백준 1001번
# a, b = map(int, input().split())
# print(a-b)

# -----------------------------------------

# 백준 10998번
# a, b = map(int, input().split())
# print(a*b)

# -----------------------------------------

# 백준 1008번
# a, b = map(int, input().split())
# print(a/b)

# -----------------------------------------

# 20230424 복습

# 백준 8393 : 합 구하기
# n = int(input())
# sum = 0

# for i in range(n+1):
#     sum += i
# print(sum)

# # -----------------------------------------

# # 백준 10950 : A+B n번
# T = int(input())

# for i in range(T):
#     a, b = map(int, input().split())
#     print(a+b)

# # -----------------------------------------

# 20230424 복습

# 백준 9498번 : 시험성적
a = int(input())

# 90~100점은 A
if 90 <= a <= 100:
    print('A')

# 80~89점은 B  80 ~ 89
elif 80 <= a <= 89:
    print('B')

# 70~79점은 C  70 ~ 79
elif 70 <= a <= 79:
    print('C')

# 60~69점은 D 60 ~ 69
elif 60 <= a <= 69:
    print('D')

# 나머지는 F
else:
    print('F')

# -----------------------------------------

# 튜터님이 내주신 숙제

my_list = [{"이름": "권기현", "나이": 32},  {"이름": "홍서연", "나이": 20},
           {"이름": "박소진", "나이": 20}, {"이름": "이미진", "나이": 19},
           {"이름": "이정현", "나이": 18}, {"이름": "연제건", "나이": 17},
           {"이름": "강유지", "나이": 16}, {"이름": "김태연", "나이": 15}, {"이름": "김주영", "나이": 14}]


for a in my_list:
    if a["이름"] == "김태연":
        pass

    elif a["이름"] == "권기현":
        pass

    else:
        a["나이"] = a["나이"] + 1

# -----------------------------------------

# 20230424 복습

# 백준 10871번 : X보다 작은 수
N, X = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
    if A[i] < X:
        print(A[i], end=" ")
