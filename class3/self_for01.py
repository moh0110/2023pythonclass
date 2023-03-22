print('for문')
print('=== 1부터 n까지의 짝수의 합 구하기 ===')
sum = 0
n = int(input('정수를 입력해주세요 : '))

for i in range(1, n+1):
    if(i % 2 == 0):
        sum += i

print('=== 1부터 %d까지의 짝수의 합은 %d 입니다.' %(n, sum))