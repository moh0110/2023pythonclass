def palindrom_check2(s):
    qu = []
    st = []
    for x in s:
        if x.isalpha(): # 단어가 알파벳이라면
            qu.append(x.lower())
            st.append(x.lower())

    while qu:
        if qu.pop(0) != st.pop(): # 비효율적인 큐
        # 큐는 선입선출이기 때문에 0값 삭제, 스택은 후입선출이기 때문에 맨 뒤 값 삭제
            return False
    
    return True

pstringList = ['역삼역', '구로구', 'Mom', '기러기', '비둘기', '기특한 특기', 'racer', 'father', '봄', '여름']

for s in pstringList:
    print('{0} = {1}'.format(s, palindrom_check2(s)))