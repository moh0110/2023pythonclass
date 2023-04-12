# 문자열 거꾸로 출력하기
# 문자열을 입력하세요 : 행복한 오늘
# 내용을 거꾸로 출력 --> 늘오 한복행

outStr = ""
inStr = input("문자열을 입력하세요 : ")
count = len(inStr)
print("내용을 거꾸로 출력 --> ", end='')
for k in range(count -1, -1, -1):
    print(inStr[k], end= '')