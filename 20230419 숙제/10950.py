# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성

T = int(input('테스트 케이스를 입력해주세요 : '))  # 테스트 케이스 개수

for i in range(T):  # T만큼 반복하자
    a, b = map(int, input('a,b를 입력해주세요 : ').split())
    print(a+b)
