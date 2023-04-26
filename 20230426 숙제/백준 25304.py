# 백준 25304번 : 영수증

# 첫번째 줄에 영수증에 적힌 총 금액 X 넣기
total = int(input())

# 둘째줄에 영수증에 적힌 구매한 물건의 종류수인 N 넣기
type = int(input())

# 총금액
sum = 0

# N개의 줄에 각 물건의 가격 a와 개수 b가 공백을 사이에 둔다.
for i in range(type):
    a, b = map(int, input().split())
    sum += a*b

# 총 금액과 영수증 금액 같은지 확인
if total == sum:
    print('Yes')
else:
    print('No')
