#두자리수의 덧셈문제 5개 풀기 프로그램 작성
import random
# 3번 시도했는데 못 맞추면 답을 알려주도록 변경
score = 0
for k in range(5):
    correct = False
    tnum = 0
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    while tnum < 3 and not correct:
        print('%d + %d = ' % (num1, num2), end='')
        ans = int(input())
        if ans == num1 + num2:
            print('Correct!!! %d번만에 성공' % (tnum+1))
            correct : True
            score += (20 - tnum*3)
            break
        else:
            print('Try again ---')
            tnum += 1
        if(tnum == 3):
            print('정답 = ',num1+num2)
print('Score=%d' %score)