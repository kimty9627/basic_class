import random

options = ['가위', '바위', '보']
computer_choice = random.choice(options)

while True:
    user_input = input('가위, 바위, 보 중에 선택해주세요 : ')
    if user_input not in options:
        print('잘못된 입력입니다.')
        continue

    print('당신은', user_input, '를 냈습니다.')
    print('컴퓨터는', computer_choice, '를 냈습니다.')

    if user_input == computer_choice:
        print('비겼습니다!')
    elif (user_input == '가위' and computer_choice == '보') or \
        (user_input == '바위' and computer_choice == '가위') or \
            (user_input == '보' and computer_choice == '바위'):
        print('승리')
    else:
        print('패배')

    break
