#데이터 선택문제

#0에서 99까지의 random number를 20개 만든다.
from random import randrange
#import random

exlist=[]
for k in range(20): #range(20) : 0~19 즉, 20번
    exlist.append(randrange(0,100)) # 0~99까지의 랜덤 숫자를 exlist에 대입

# 오름차순으로 정렬한 후 k번째 수 선택

k = int(input("몇번째 데이터를 원하시나요?"))
print(exlist)
exlist.sort()
print(exlist)
print(k, 'th data = ', exlist[k-1]) #3번째 데이터

count = 1
exlist2 = []
while count < 20: #1~20 즉, 19번 반복
    num = randrange(0, 51) #0~50 사이의 랜덤 숫자
    if num not in exlist2: #exlist2 배열에 없는 숫자일때
        exlist2.append(num) #해당 숫자를 exlist2에 대입
        count += 1

print(exlist2)
#최소값을 구하고 삭제하는 것을 k번 한다

for d in range(k):
    mvalue = min(exlist2)
    di = exlist2.index(mvalue)
    del(exlist2[di])

print(k, 'kth value', mvalue) #exlist2에 3번째로 작은 값
# print(exlist2)