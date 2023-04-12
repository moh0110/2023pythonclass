#백준 11659번 문제
print('합을 구할 데이터 수와 질문 갯수 입력 : ')
suNo, quizNo = map(int, input().split())
numbers = list(map(int, input().split()))
pSum = [0]
temp = 0

for i in numbers:
    temp = temp + i
    pSum.append(temp)

print(pSum)

for i in range(quizNo):
    print('질의할 범위를 입력하시오 : ')
    s, e = map(int, input().split())
    print(pSum[e] - pSum[s-1])