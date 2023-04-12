file_path = "C:\python\data\class_colon.txt"

data_dict = {}

with open(file_path, "r") as f:
    for line in f:
        id, *data = line.strip().split(":") #strip() 문자열 공백제거
        data_dict[id] = tuple(data)

# 딕셔너리 출력
print(data_dict)
for k in data_dict:
    print(k, data_dict[k])

# midx = 0으로 하여 최대 수강인원의 강좌정보도 출력되게 하려면

smax = 0; midx = 0
for k in data_dict:
    if(int(data_dict[k][1]) > smax):
        smax = int(data_dict[k][1])
        midx = k
print('최대 수강하는 강좌의 정보 = ', midx, ":", data_dict[midx])

# 리스트에 수강인원을 append하여 max()함수 이용
snumList = []
for k in data_dict:
    idata = int(data_dict[k][1])
    snumList.append(idata)

print('리스트 함수이용: 최대 수강인원은 = ', max(snumList))