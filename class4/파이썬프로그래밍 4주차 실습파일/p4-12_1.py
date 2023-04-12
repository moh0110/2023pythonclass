#백준 11659번 문제
print('합을 구할 데이터 수와 질문 갯수 입력 : ')
suNo, quizNo = map(int, input().split())
numbers = list(map(int, input().split()))
pSum = [0]
temp = 0
slist = []
for i in numbers:
    temp = temp + i
    pSum.append(temp)

print(pSum)
# 구간합 (s, e) 쌍의 list로 해서 출력이 따로되도록
for i in range(quizNo):
    s, e = map(int, input().split())
    slist.append(pSum[e] - pSum[s-1])

for i in range(quizNo):
    print(slist[i])