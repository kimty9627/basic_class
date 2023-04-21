# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성

n = int(input())  # 값을 입력받는 곳
sum = 0  # for문의 값을 넣는 곳

for i in range(1, n+1):  # range는 i 에 담겨있는 값
    sum = sum + i
    print(sum)
