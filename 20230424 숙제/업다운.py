import random

answer = random.randint(10, 100)
while True:
    user_input = int(input())
    if user_input == answer:
        print("정답입니다.")
        break
    elif user_input < answer:
        print("Up")
    else:
        print("Down")
print("게임이 끝났습니다.")
