print('while문')
print('=== 1부터 n까지의 짝수의 합 구하기 ===')
num = 1
sum = 0
n = int(input('정수를 입력해주세요 : '))

while True:
    if(num <= n):
        if(num % 2 == 0):
            sum += num
            num += 1
        else:
            num += 1
    else:
        break
print('=== 1부터 %d까지의 짝수의 합은 %d 입니다.' %(n, sum))