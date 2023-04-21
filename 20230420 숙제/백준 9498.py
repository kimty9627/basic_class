
score = int(input())

# 90~100점은 A
if 90 <= score <= 100:
    print('A')

# 80~89점은 B  80 ~ 89
elif 80 <= score <= 89:
    print('B')

# 70~79점은 C  70 ~ 79
elif 70 <= score <= 79:
    print('C')

# 60~69점은 D 60 ~ 69
elif 60 <= score <= 69:
    print('D')

# 나머지는 F
else:
    print('F')
