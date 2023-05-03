from random import randrange

hap = lambda n1 = 10, n2 = 70, n3 = 50 : n1+n2+n3
print(hap())
print(hap(10, 20))

exList = [10, 20, 30, 40 ,50]
exList2 = exList*2
print(exList2)

def multiplyn(data, n) :
    return data * n

m = randrange(2, 6)
print('m =',m)
for k in range(len(exList)):
    exList[k] = multiplyn(exList[k], m)
print(exList)

# for문 사용하지 않고 함수 multiplyn 사용
m = randrange(2, 6)
print('m =',m)
mlist = [m]*len(exList)
exList = list(map(multiplyn, exList, mlist))                           
print(exList)

# for문 사용하지 않고 람다함수 사용
testf = lambda data, n=m: data *n # 이 부분을 생략하고 아래 testf 부분에 적어줘도 된다.                    
exList = list(map(testf, exList))
print(exList)